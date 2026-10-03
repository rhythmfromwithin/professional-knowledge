---
link: https://medium.com/airbnb-engineering/personalization-without-user-identity-8e7891a1d486?source=rss
slack_ts: '1791003466.896259'
source: Airbnb Engineering
title: Personalization without user identity
----53c7c27702d5---4
priority: medium
status: unread
interest: medium
next_step: skim
---
# Personalization without user identity
> 原文: [https://medium.com/airbnb-engineering/personalization-without-user-identity-8e7891a1d486?source=rss----53c7c27702d5---4](https://medium.com/airbnb-engineering/personalization-without-user-identity-8e7891a1d486?source=rss----53c7c27702d5---4)

#### How Airbnb uses proximity signals to personalize without relying on individual user history.

![Aerial view of a residential neighborhood with lakes, tree-lined streets, and green spaces.](https://cdn-images-1.medium.com/max/1024/1*dluIy8gak-FybuiuGcqXLw.png)

**By**:[Wei Jiang](http://www.linkedin.com/in/wei-jiang-5713b91b/), [Bin Xu](https://www.linkedin.com/in/bin-xu-96253aa5/), [Bharathi Thangamani](https://www.linkedin.com/in/bharathipriyaa/), [Weiwei Guo](https://www.linkedin.com/in/weiwei-guo/), [Sundar Srinivasavaradhan](https://www.linkedin.com/in/sundar-srini/), [Tracy Yu](https://www.linkedin.com/in/tracy-xiaoxi-yu/), [Huiji Gao](https://www.linkedin.com/in/huiji-gao/), [Swapnil Ghike](https://www.linkedin.com/in/swapnilghike/), [Michael Kinoti](https://www.linkedin.com/in/michael-kinoti-7a309215/)

Great personalization starts with knowing your user. But what happens when the user is a stranger?

A significant share of Airbnb users arrive without a login, without a recent search history, or without any prior booking — especially those landing from paid advertising or organic search. For these users, the ML models that power search ranking, destination recommendations, and marketing landing pages face the **cold-start problem**: there is little to no user signal available.

In this blog post, we describe **Proximity Features** — a new class of ML features that addresses both the cold-start problem and evolving privacy constraints simultaneously. The core hypothesis: aggregate activity patterns within a proximity bucket can provide useful signals for cold-start personalization without relying on individual user identity. By grouping nearby users into buckets and aggregating their collective signals, we can construct rich, location-aware features available immediately for *any user whose IP can be geo-located* — no login, no prior history, and no persistent user identifier required.

### The challenge: serving users without individual signals

Personalization at Airbnb has historically relied heavily on a user’s identifier to link together past searches, bookings, and browsing patterns. This works well for returning, logged-in users. But on marketing and acquisition surfaces, many users are logged out or visiting for the first time, and standard user identifiers are unavailable. In other cases, users are logged in, and standard user identifiers are available, but the features derived from them are stale or too sparse to carry meaningful signals.

Privacy regulations compound the challenge. Under GDPR, non-essential tracking for marketing personalization requires an appropriate legal basis and, in many contexts, user consent. Separately, browser restrictions and the deprecation of third-party cookies reduce the availability of cross-site identifiers. Any feature system targeting this traffic must work *without relying on persistent user identifiers for model inference*.

The result: users on these surfaces were receiving little to no personalization.

### The solution: proximity features

#### The proximity key

The key insight behind Proximity Features is geographic correlation. Users browsing Airbnb from the same city or neighborhood tend to search for similar destinations, prefer similar price ranges, and often share travel patterns and local context. A user in Seoul is far more likely to book Jeju Island, the largest island that’s part of South Korea, or Osaka, Japan, than is a user in New York. This pattern holds however much Airbnb does or doesn’t know about the individual user.

![From any user’s IP address, the system derives a coarse geographic location, groups nearby users into an adaptive proximity bucket, and aggregates their collective signals into features for model scoring, with no persistent user identifier required.](https://cdn-images-1.medium.com/max/1024/1*goze5ASOJxX7OoQJXg2O7g.png)

*From any user’s IP address, the system derives a coarse geographic location, groups nearby users into an adaptive proximity bucket, and aggregates their collective signals into features for model scoring, with no persistent user identifier required.*

We operationalize this insight through a **proximity key**: a compact group key representing a local geographic cluster of approximately 1,000 users. The key encodes a quantized latitude/longitude tile and, for densely populated areas, an IP hash bucket index within that tile — fine-grained for a city center, coarser for a rural location. In either case, the key identifies a neighborhood, not an individual.

This proximity key functions as an **aggregation key** analogous to *user\_id*: any ML model that currently conditions on a user identifier can instead condition on a proximity key to serve cold-start users (e.g., logged-out, anonymous, or first-time). Even logged-in users with meaningful historical information available can benefit from the additional information that use of the proximity key enables. However, unlike logged-in user information, the features associated with a key reflect the collective behavior of the local group, not the actions of any single user. No persistent user identifier is required at inference time.

So what are the actual features? Once users are grouped into a bucket, features are computed daily across three categories: **short-term engagement** (e.g., top destinations, room types, and median prices from recent searches); **long-term booking patterns** (e.g., booked destinations and travel party signals); and **aggregate bucket metadata** (e.g., bucket size and geographic density). A user who has never searched on Airbnb gets a feature vector derived from approximately 1,000 nearby users, effectively borrowing signals from the crowd.

#### Adaptive clustering

Computing proximity keys requires grouping all global users into stable buckets of approximately 1,000 each. The challenge is that the geographic density of Airbnb users varies by orders of magnitude: a single coordinate near a major airport can represent vastly more daily users than a rural location with only a handful. A fixed geographic grid (like a standard geohash at one resolution) fails at both extremes — too coarse for cities, too fine for rural areas.

![Illustrative example: the adaptive clustering algorithm zooms in for dense areas (left) — using fine geographic tiles subdivided further by IP hash buckets — and zooms out for sparse areas (right), merging coordinates into coarser tiles until each bucket reaches ~1,000 users.](https://cdn-images-1.medium.com/max/1024/1*sXnbUPybSLk6HRj-bzjCIA.png)

*Illustrative example: the adaptive clustering algorithm zooms in for dense areas (left) — using fine geographic tiles subdivided further by IP hash buckets — and zooms out for sparse areas (right), merging coordinates into coarser tiles until each bucket reaches ~1,000 users.*

We solve this with a **two-phase adaptive clustering algorithm**. For any coordinate dense enough to fill a bucket on its own, we subdivide further using IP hash buckets, which preserves fine granularity in city centers. For the remaining coordinates, we apply multi-pass coarsening, progressively widening the geographic tile until enough users accumulate. The result is a zoom-adaptive map: fine-grained tiles over major cities, coarser groupings in rural areas. This runs efficiently at global scale on geo-IP coordinate data.

Proximity keys are also **stable over time**: the key partition bootstrapped in 2023 has remained valid in production without re-clustering, with a daily refresh handling new IPs and coordinate shifts. At serving time, a user’s IP is resolved to a proximity key in real time and features are fetched from a distributed key-value store. The lookup is a *soft dependency*. If it times out, the model proceeds without it, so personalization never blocks the core request path.

#### Privacy design

Privacy is built in at every layer. Every feature reflects a group of ~1,000 users, not an individual. The clustering input excludes users who have not provided consent. Geo-IP coordinates are coarse and group-level, aggregated around population centers rather than specific addresses. The pipeline is also integrated with consent management and data-governance deletion controls throughout.

### The benefits: what proximity features unlock

Proximity Features have now launched across multiple Airbnb surfaces, with measurable results from production A/B experiments.

![Selected lifts from production A/B experiments.](https://cdn-images-1.medium.com/max/1024/1*FLYFot0BPN_KBAuk9DFV_w.png)

*Selected lifts from production A/B experiments.*

**Marketing landing pages**. Pages where users arrive from paid advertising and organic search have especially high cold-start rates. Before this work, the listing recommender had severely sparse feature vectors for much of this traffic and served static listing cards. Adding proximity features gave the model access to booking and browsing patterns from nearby users, enabling meaningful personalization for cold-start traffic.

**Homepage AutoSuggest**. For users without history, the AutoSuggest feature on the Homepage previously fell back to a static global list (e.g., Paris, Barcelona, London, Rome), regardless of where the user was browsing from. Proximity features replace this generic fallback with location-aware signals: a new user browsing from Beijing now sees Hong Kong and Tokyo instead.

![Illustrative AutoSuggest example: for a new user without history, AutoSuggest v1 showed a generic global list (left). With proximity features, location-aware suggestions replace the generic defaults (right).](https://cdn-images-1.medium.com/max/1024/1*1DSjruOVe-khmum7uXUajA.png)

*Illustrative AutoSuggest example:* *for a new user without history, AutoSuggest v1 showed a generic global list (left). With proximity features, location-aware suggestions replace the generic defaults (right).*

The experiment showed directional gains concentrated among **never-booked and dormant users** on Airbnb, exactly the population proximity features are designed to serve. The diversity shift corroborates this: destinations like Kuala Lumpur, Dubai, and Jeju Island, which in the past had rarely been displayed to users in relevant regions, appeared consistently in the treatment arm.

**Engagement emails**. The same serving layer is being extended to personalized email campaigns using recent coarse location signals. Experiment validation is underway.

### Conclusion

Proximity Features show that the cold-start problem does not require a persistent user identity to solve. By grouping users geographically and aggregating their collective signals, we can construct features immediately available for any user whose IP can be geo-located, without relying on persistent user identifiers. The design is intentionally reusable; any model conditioned on a user identifier can be extended to cold-start users by conditioning on a proximity key instead.

For the full technical details, see our [paper](https://arxiv.org/abs/2607.12246) accepted to [the TSMO Workshop at KDD 2026](https://sites.google.com/view/tsmo2026/accepted-papers). The paper includes the system architecture, clustering algorithm, privacy design, and complete experiment results.

If this type of work interests you, check out some of our [related positions](https://careers.airbnb.com/)!

### Acknowledgments

The authors thank the Relevance & Personalization, Marketing Technology, and Infrastructure teams at Airbnb for their collaboration, feedback, and support in bringing Proximity Features to production.

We also want to thank Hui Gao for his support in authoring this post during his time at Airbnb.

*All product names, logos, and brands are property of their respective owners. All company, product, and service names used in this website are for identification purposes only. Use of these names, logos, and brands does not imply endorsement.*

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=8e7891a1d486)

---

[Personalization without user identity](https://medium.com/airbnb-engineering/personalization-without-user-identity-8e7891a1d486) was originally published in [The Airbnb Tech Blog](https://medium.com/airbnb-engineering) on Medium, where people are continuing the conversation by highlighting and responding to this story.
