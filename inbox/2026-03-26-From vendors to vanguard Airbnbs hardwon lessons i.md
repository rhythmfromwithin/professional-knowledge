---
title: "From vendors to vanguard: Airbnb’s hard-won lessons in observability ownership"
source: "Airbnb Engineering"
link: https://medium.com/airbnb-engineering/from-vendors-to-vanguard-airbnbs-hard-won-lessons-in-observability-ownership-3811bf6c1ac3?source=rss----53c7c27702d5---4
priority: medium
status: unread
interest: medium
next_step: skim
---
# From vendors to vanguard: Airbnb’s hard-won lessons in observability ownership
> 原文: [https://medium.com/airbnb-engineering/from-vendors-to-vanguard-airbnbs-hard-won-lessons-in-observability-ownership-3811bf6c1ac3?source=rss----53c7c27702d5---4](https://medium.com/airbnb-engineering/from-vendors-to-vanguard-airbnbs-hard-won-lessons-in-observability-ownership-3811bf6c1ac3?source=rss----53c7c27702d5---4)

![](https://cdn-images-1.medium.com/max/1024/1*7z8dKfmBs_h7_oXXNhx-PQ.jpeg)

*How a complex, large-scale migration to an in-house observability platform led to superior tooling, consistent data, and a fundamental reset of the developer experience.*

**By:** [Callum Jones](https://www.linkedin.com/in/callumj/), [Rong Hu](https://www.linkedin.com/in/rong-hu-0751408/)

Observability — the function of providing visibility into the performance and reliability of applications using metrics, logs and traces — is one of the most important tools of the Infrastructure group at any company. Without a reliable, cost-effective, and user-friendly observability platform, you limit an organization’s ability to empower engineers to assess, support, and improve the reliability of their application.

Like many of its peers, Airbnb started out by outsourcing its observability needs to vendors. But, as the company matured, our needs diverged from the typical vendor’s incentives. Vendors charge by the amount of data ingested, so Airbnb’s costs were rising, but more data does not automatically lead to faster insights or reduced mean time to detect (MTTD) or repair (MTTR). Also, by being out of the feedback loop of how observability data is consumed, our ability to enhance the monitoring workflows of our customers or pursue cost optimizations on observability spend was severely hampered.

To meet our objectives, Airbnb embarked on a complex migration, overhauling every part of our metrics infrastructure. This challenging journey involved replacing our instrumentation, collection, storage, and visualization systems as we transitioned from a third-party, vendor-managed observability platform to a custom, in-house solution built on open-source technology based on Prometheus.

This transition enabled us to gain end-to-end ownership over metrics collection, storage, and querying. Through this project, we successfully utilized our automation tooling to migrate a massive volume of data across 1,000 services: 300 million timeseries, 3,100 dashboards, and more than 300,000 alerts. While one does not undertake a project of this scope lightly, the restrictions around what we could do with our own data left us with little alternative.

Though there’s no one-size-fits-all migration guide, we have some learnings from this specific migration that we believe will be helpful to others. We will first describe a simplistic, but ultimately flawed, approach to migration, and then detail the successful strategy we ultimately employed. Our plans for this migration, begun five years ago, evolved significantly as we proceeded. This journey provided us with valuable, hard-won lessons, offering clear insights into the best practices and pitfalls for executing a large-scale migration.

### Migration v1

#### Climbing Everest on day one

When approaching a large-scale migration, the general strategy is to aim for the largest, most impactful service first. Tackling the biggest challenge upfront allows the project team to demonstrate immediate, significant progress, build confidence in the new infrastructure, and prove the migration strategy’s viability to the wider team and stakeholders. This high-visibility win then sets the tone for the rest of the rollout.

With this approach in mind, it (initially) made sense to take a complex service — for example, something that has sparse data, or emits metrics in a way not standard to the new system — and make this the first service to migrate onto our new system. That would expose the differences between the two systems and allow us to design solutions that mimicked the behavior of the old system, ensuring that the dashboards and alerts would look the same.

When following this strategy, a team will spend a lot of time getting the first service to work, and is likely to have false alarms, dashboards that don’t align between the systems, and a lot of education to get the first customer on board; all to prove to the wider company that the overall migration is worthwhile.

#### Same baggage, thinner air

When migrating systems, a smooth transition for your customers is paramount, as enough is already changing for them. Even if the legacy system has led to flawed or inaccurate queries that could be fixed, it’s important to approach fixes strategically. For example, avoid trying to resolve issues with existing dashboarding and alerting patterns all at once.

Instead, focus on a complete migration to the new system first. Once everyone is brought over and centralized, you can address and solve these dashboard and alerting improvements in a subsequent, second set of changes. Customers want the initial migration completed first. If moving to the new system already presents friction, we shouldn’t exacerbate the difficulties involved by also altering the functionality of their queries.

#### The documentation explains everything, for those who stop to study it.

To facilitate customer adoption of the new system, which likely includes extensive changes, it’s crucial to provide comprehensive documentation on the new query language and interfaces. This should be paired with extensive training to ensure user proficiency.

Even for infrequent users, familiarity with the observability query language is important, similar to any programming language. This knowledge, supported by the documentation and training materials, will be particularly valuable for quickly diagnosing problems during incidents.

### Migration v2

#### Start with an achievable target

Choosing an initial service to migrate that aligns closely with your destination system can eliminate much of the distraction and noise that typically accompanies a complex migration. When your initial goal is to prove (to your team and to the broader company) that the migration is worthwhile (in terms of cost reduction, capabilities, etc.), it’s crucial to focus on a tractable, high‑leverage service.

This allows your team to:

* Validate that the storage engine can handle the required scale and observe how it behaves during incidents
* Deliver translator tooling to migrate existing dashboards and alerts to the new system
* Invest in customer‑facing documentation, education, and training
* Introduce the new visualization tool to a small set of users, giving them time to adjust to the new experience while your team gathers feedback on UX gaps before rolling the service out at scale

Successfully migrating this less complex service achieves two things: it demonstrates to your team that the migration is technically and operationally feasible; and, by narrowing the scope and collaborating closely with the customer, it helps you validate the migration strategy to the entire company.

Switching vendors will often necessitate a new visualization tool, so this is also a good opportunity to surface any UX differences early. The feedback your team collects from this initial cohort will prove invaluable when rolling the new tooling out to the rest of the organization.

#### Migrate the intent of query

With any long‑running system, you eventually accumulate a wide variance in how latency, error rates, and other signals are measured across dashboards. In a democratized observability environment, this is almost guaranteed: some metrics will be computed incorrectly — for example, averaging a result that should be a p95, or summing total latency. Customers can easily construct flawed queries and, without guardrails, the results of those queries get treated as ground truth.

A migration puts your team back in the loop. It’s an opportunity to correct these patterns — not by erasing or resetting them, but by understanding the original intent and mapping it to a preferred, standardized query.

![](https://cdn-images-1.medium.com/max/1024/1*-SS6XenH2zP8ON5LtPEcEA.png)

With this in mind, we adapted our translation system to focus on intent rather than one‑to‑one query translation. For example, if a query included a p95 calculation, we would ignore any additional aggregations layered on top and instead return a canonical histogram query for that metric.

In practice, this required introducing a dedicated metadata engine. In Prometheus, metric types are often inferred from naming conventions (for example, a \_total suffix indicating a counter). But, because we chose to preserve existing metric names to avoid divergence between code and observed data, naming alone was no longer reliable.

To address this, we built a metadata engine directly into the translation layer. It periodically scans all known metrics and uses an internal label (*otel\_metric\_type*) to construct and maintain a reliable mapping from metric to type.

With this change in place, we’re now significantly more confident that teams have accurate, consistent visibility into the performance of their applications.

#### A new query language can be daunting

Customers are, understandably, going to need some time to reset the muscle memory they have developed for the old system. In some cases, your new system may not provide the same polish for easily crafting queries.

During our migration, our users’ lack of familiarity with the new query language was solved by using our translation tooling, which could map a given query to the new system to help bootstrap a self-service migration. But, post-migration, we didn’t want to continue providing a shim between the old language and the new, as that would slow down or inhibit the needed reset of muscle memory.

By adopting PromQL as the query language for our new system, we benefit from a mature ecosystem and a well-documented query language that is widely understood by both humans and modern LLMs.

We further reduced the barrier to entry by pairing this with in-house skills for our AI tooling, which supplies rich semantic metadata about each metric — for example, whether it is a counter or histogram, or what units it is reported in. Together, these capabilities allow agents to generate correct PromQL with far less manual effort, enabling developers to bootstrap their understanding more quickly and explore metrics more effectively. This has become critical for incident debugging.

![](https://cdn-images-1.medium.com/max/1024/1*PuJrwIdLl83tZJw7Z8LVBw.png)

Consequently, customers can now complete many common tasks, such as diagnosing incidents or creating dashboards, in a matter of minutes, a significant reduction from the hours these tasks previously required.

#### Now is the time to correct outdated patterns

Over time, old systems may be neglected, and their (lack of) functionality may become a drag on productivity. Thus, the benefit of any large migration is that you get to take a step back, reflect on how your product is being used, and identify additional areas for improvement.

While initially we were afraid of introducing new concepts, as our initial set of customers began using the new system, it became clear to us that the existing alert framework was in need of a replacement. We made the choice to pull forward the investment our sister team, Reliability Experience, had been making in the alert authoring space, and promote their work as the preferred alert-authoring experience.

This new alert experience replaced the outdated system with a new alert-authoring experience that treated each alert as a development workflow, rather than as a sparsely documented config file. Alerts are authored as code, with autocomplete and builder-style assistance for writing queries, built-in backtesting to understand when an alert would have fired historically, and diffing to clearly reason about the impact of changes, all before deployment.

This was a change from our original strategy of maintaining dashboards and alerting unchanged by the initial, major migration. But we found that the migration’s success was significantly amplified by the improved alerting framework. This change helped customers recognize the inherent value of the migration, beyond just control and cost objectives, shifting the perception of the project. Furthermore, the centralized nature of the new alerts streamlined the process by reducing the overall migration effort. This centralization lowered the amount of work customers needed to spend on migration tasks.

### Conclusion

This migration ultimately became much more than a change in which storage engine to use and where it was hosted. What began as an effort to “just port the system” evolved into a reset of how we think about observability, ownership, and the developer experience.

By owning the full lifecycle of our metrics, from emission through querying, we materially improved our reliability posture. We moved from fragile, hand-crafted queries toward more intentional patterns, better tooling, and higher-confidence alerts and dashboards. The investment in metadata, AI tooling, and modern authoring workflows paid dividends not only in correctness, but in how quickly engineers can explore possibilities and respond during incidents.

Equally important, the migration reshaped our relationship with our internal customers. Instead of outsourcing core observability concerns, we were forced to engage deeply with how teams actually use metrics under real operational pressure. That feedback loop has been invaluable, and it continues to guide where we invest next.

Automation played a key role in making this migration feasible, but we learned that automation alone is not enough. Blindly translating existing patterns (especially flawed patterns) simply transfers technical debt into a new system. The most impactful moments came when we deliberately chose to break compatibility in favor of better defaults, even when that caused short-term friction.

Finally, this effort produced a repeatable blueprint. For future migrations, we are clear about what we want to own: the experience and interfaces for how engineers write, read, and reason about their data. Storage engines and backends may change, but the responsibility for making observability usable, trustworthy, and evolvable should remain firmly in our hands.

Even for teams not facing an imminent migration, there are steps worth taking now to reduce future friction. The most impactful is to **own the interaction layer**: the frontend, authoring tools, and workflows engineers use to explore and act on observability data. During our migration, we not only had to change the backend system, but also had to move every team to a new visualization tool and to our new alerting framework, significantly increasing the switching cost. Had we already controlled those touchpoints, the backend transition would have been far simpler and more incremental.

While every organization’s constraints are different, we hope these lessons help others view large-scale migrations not as a necessary burden, but as a rare opportunity to meaningfully improve systems and, as a result, your observability posture.

If this type of work interests you, check out some of our [open roles](https://careers.airbnb.com/).

### Acknowledgements

We would like to express our gratitude to the following teams for their essential contributions to this migration:

**Observability Team**

Abdurrahman Allawala, Rishabh Kumar, Eugene Ma, Natasha Aleksandrova, Suman Karumuri, Wei Song, Yann Ramin, and Xuan Lu. This team was instrumental in migrating Airbnb to the new observability system.

**Reliability XP Team**

Doug Smith, Kevin Goodier, Harry Shoff, Rich Unger, and Vlad Vassiliouk. This team developed our new Alerting framework.

Finally, a thank you to everyone across Airbnb who helped successfully migrate onto our new observability system.

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=3811bf6c1ac3)

---

[From vendors to vanguard: Airbnb’s hard-won lessons in observability ownership](https://medium.com/airbnb-engineering/from-vendors-to-vanguard-airbnbs-hard-won-lessons-in-observability-ownership-3811bf6c1ac3) was originally published in [The Airbnb Tech Blog](https://medium.com/airbnb-engineering) on Medium, where people are continuing the conversation by highlighting and responding to this story.
