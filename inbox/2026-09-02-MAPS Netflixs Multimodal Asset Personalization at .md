---
link: https://netflixtechblog.com/maps-netflixs-multimodal-asset-personalization-at-scale-32f96320785e?source=rss
slack_ts: '1788408231.864199'
source: Netflix Tech Blog
title: 'MAPS: Netflix’s Multimodal Asset Personalization at Scale'
----2615bd06b42e---4
priority: high
status: unread
interest: medium
next_step: skim
---
# MAPS: Netflix’s Multimodal Asset Personalization at Scale
> 原文: [https://netflixtechblog.com/maps-netflixs-multimodal-asset-personalization-at-scale-32f96320785e?source=rss----2615bd06b42e---4](https://netflixtechblog.com/maps-netflixs-multimodal-asset-personalization-at-scale-32f96320785e?source=rss----2615bd06b42e---4)

*By* [*Emma Yanyang Kong*](https://www.linkedin.com/in/emma-yanyang-kong-6904b457/)*,* [*Aditya Deshpande*](https://www.linkedin.com/in/aditya-deshpande8/)*,* [*Asad Abbasi*](https://www.linkedin.com/in/asad-abbasi-364a37158/)*,* [*Bowei Yan*](https://www.linkedin.com/in/bowei-yan-0080a326/)*,* [*David Fagnan*](https://www.linkedin.com/in/dfagnan/)*,* [*Ashish Rastogi*](https://www.linkedin.com/in/ashish-rastogi-11362a/)*,* [*Dhaval Patel*](https://www.linkedin.com/in/dhaval-patel-1a23aa8/)*,* [*Ray Zhang*](https://www.linkedin.com/in/ray-zhang-a7168a32/)

### **Introduction**

The Netflix experience is a journey of discovery. Every visual cue, from the artwork on a title to the video previews that autoplay while you browse, is there to connect you with a story you will love. We call these visual cues *assets*, and choosing the right one for each member is a personalization problem of its own. But which image or video preview of *Squid Game* should we show you? And what do we do right after a title launches, when there’s far too little interaction data to know which asset we should recommend to each member?

For years, our models answered the first question well and the second poorly. They learned which assets members interacted with, but treated every asset as an opaque ID, blind to what was actually *in* the artwork or video preview. Right after a title launched, its assets had no history, so we dialed up exploration on its assets to gather interaction data, and otherwise fell back to popularity heuristics that ignore your taste. Only once enough interactions had piled up could personalization take over. This is the classic **cold-start** problem.

This post shares how **multimodal embeddings** let our models see and hear the assets they recommend, so personalization can kick in far sooner, close to a title’s launch. Because a new asset arrives with its embedding the model already understands, that embedding carries member taste signals from related assets immediately. Consequently, the model needs far less interaction history before it can personalize. We cover three production systems, artwork personalization, query-aware artwork ranking, and video preview personalization, plus a cheap trick for choosing new embeddings before committing to full end-to-end integration and A/B testing.

### **Artwork Personalization**

A single image is often a member’s first touchpoint with a title, so we create a diverse set of artworks for each title to appeal to different member tastes. We already use [personalized artwork](https://netflixtechblog.com/artwork-personalization-c589f074ad76) based on members’ interaction histories, but this approach breaks down for newer titles and their assets, where there is little or no behavioral data to learn from.

**Making the Model See the Artwork**

Our solution is to let the model “look” at the picture. We encode each artwork with [**CLIP**](https://arxiv.org/abs/2103.00020), a pretrained image-text embedding model, and fold the result into how the model represents that asset, concatenating the per-asset CLIP image embedding, a 768-dimensional vector, with the asset’s learned ID embedding to give an asset representation:

![](https://cdn-images-1.medium.com/max/332/1*Tm2AJHCkMfTwtedhfmIAwA.png)

*e\_id(a) is the asset’s learned ID embedding, and e\_a is its CLIP image embedding. The two are concatenated and passed through an MLP layer to give h\_a, the representation the model scores against a member.*

This single change transforms how the model handles a brand-new artwork. Instead of treating it as an unseen ID, the model now receives a CLIP embedding the moment the asset is created. That allows a member’s preferences over visual themes, talent, and color palettes to be applied immediately, long before the asset accumulates any interactions of its own. Because those preferences are expressed in image-embedding space rather than tied to specific asset IDs, they **transfer seamlessly across titles**. If you consistently engage with artwork featuring a particular comedian, the model can carry that signal to their new title and prioritize the asset that places them front and center, even if it has never shown you that exact image before, as in the figure below. In this way, cold-start shifts from being a blind spot to something the embedding space already has an informed opinion about.

![](https://cdn-images-1.medium.com/max/1024/1*0fIbem23tXHGovlfOeJrEQ.jpeg)

Knowledge transfer through CLIP embeddings. A member who has interacted with a comedian’s past stand-up artwork (left) leads the model to favor the new-title asset that features that comedian prominently (green check) over one that does not, even though it has never seen that specific image before.

**From Five Models to One**

That shift, from scoring an asset by the ID it happens to carry to scoring it by what the image actually contains, powers a second big win, model consolidation. Each title’s artwork spans multiple canvases with different croppings (billboard, vertical-box, horizontal-panel, short-panel, landscape-panel), and historically we trained a separate model per canvas, since an ID-based model has no way to know that the cropped and resized renderings of one scene are related, so signal could not flow between canvases and each faced its own cold-start.

CLIP embeddings break that barrier. Because they are largely invariant to crop, resize, and aspect ratio, those near-identical renderings map to nearly the same vector, as the figure further below shows. A single unified model can therefore pool interaction signal across every canvas, so a member’s affinity learned on a high-traffic canvas immediately informs the artwork we pick on a sparse one. The result is one model in place of five, with the largest gains on the canvases that have the least interaction data.

![](https://cdn-images-1.medium.com/max/1024/1*zq18aAkc5jC0ThC6ohYUfQ.jpeg)

*One source image, many canvases. The same* Running Point *artwork is cropped and resized across billboard, TV, mobile, and out-of-home placements, each with a different asset ID. Because CLIP embeddings barely change under crop and resize, a single unified model can personalize all of them.*

**Mixing Five Canvases of Training Data**

Consolidation introduced a challenge that the per-canvas models never faced: *how to effectively mix data across disparate canvases?* The canvases differ widely in impression volume, and the interactions they log are not all worth the same to a member’s long-term experience. Training on pooled raw counts would let the highest-volume canvas and the most frequent interaction types dominate, so the low-data canvases we were trying to help would benefit least. Hand-tuning a weight per canvas would just trade that problem for a set of arbitrary hyperparameters and endless online sweeps to tune them.

Instead we use **reward-based weighting**, building on Netflix’s[*long-term reward modeling*](https://netflixtechblog.com/recommending-for-long-term-member-satisfaction-at-netflix-ac15cada49ef). Each training example is weighted by the long-term reward score attached to its interaction type:

![](https://cdn-images-1.medium.com/max/248/1*3NE1H9JefoSIkdW6Q0o58g.png)

*a\_ti is a training example, a positive interaction on asset i of title t. Its weight is set by the interaction type e observed on it, scored by ρ, that type’s long-term reward.*

where *e*(·) is the type of the observed positive interaction and *ρ* is that type’s long-term reward score. Because interaction types are not distributed evenly across canvases, weighting by long-term value rebalances the canvas mixture on its own, with no weight set by hand. A canvas contributes in proportion to the long-term value of the interactions it drives rather than to how many impressions it happens to get. Consolidation becomes feasible, and the unified model optimizes for long-term member satisfaction instead of whichever short-term action is most frequent.

**A Note on Offline Evaluation**

Every result presented here must clear two bars: an offline metric evaluation followed by a large-scale online A/B test. The offline metric is the subtle one. Judging a new model on logs from the current production policy is biased, because that policy shows some assets far more often than others. The logged rewards describe what the *policy* preferred, not what members would have chosen from the full candidate set, so a new model that disagrees with the logging policy looks worse than it is, because the impressions it would have picked are barely represented in the data.

We handle this with [**inverse propensity scoring**](https://arxiv.org/abs/1602.05352) (IPS) computed on a dedicated slice of *exploration* traffic. A small fraction of traffic is served by a randomized policy that samples among a title’s candidate assets from a known distribution, so the propensity of showing a given asset in a given context is logged exactly at serving time rather than estimated after the fact. Reweighting every observation by the inverse of its logged propensity gives:

![](https://cdn-images-1.medium.com/max/372/1*Dy62e8ZB50jK-L1eDCBGbQ.png)

where *D* is the exploration slice and *r*(*x*, *a*) is the observed reward, such as a play. Impressions that exploration made rare are upweighted accordingly, and the estimator becomes an unbiased estimate of the reward a candidate policy would have earned had we actually deployed it. Having propensities that are known by construction, rather than modeled after the fact, is in our experience the single biggest reason our offline numbers track online outcomes. We report IPS as a ratio against the production baseline, and a candidate has to win there before it gets any A/B traffic.

**Combining Both Ideas Works Better**

Two ideas are bundled together here, so we ablated them separately against the old five-model production system.

* **V1, image embeddings only.** The five per-canvas models kept as they were, each one augmented with image embeddings.
* **V2, unified model only.** A single model trained over all five canvases, but with learned ID embeddings alone and no image content.
* **V3, both together.** One unified model over all five canvases, with image embeddings in its asset representation.

As the chart below shows, each idea helped exactly where we expected: on the data-starved short-panel canvas and landscape-panel canvas. V3 was the clear winner. A change inside ±1% is not significant for this offline metric, and those bars are hatched in the chart. Most of what V1 and V2 do on their own sits inside that band.

![](https://cdn-images-1.medium.com/max/1024/1*Bibqjv_YU0t_jFxkrhVS2A.png)

*Relative offline IPS lift by canvas for the three variants, each measured against the prior per-canvas model on that same canvas. Both ideas help where interaction data is scarcest, and V3 is strongest. Hatched bars fall inside the ±1% band, where the change in the offline metric is not significant; V3 values are labeled on the plot.*

In the online A/B test across all device platforms, which ran for at least four weeks, the results drew a much clearer line: *Neither idea moved our online core member metrics on its own.* V1 and V2 were both flat and non-significant, and only V3 won a statistically significant lift. It is what runs in production today.

The two ingredients need each other. V1 tells a per-canvas model what an asset looks like, but one sparse canvas has too few examples to teach it how to *use* that. V2 supplies plenty of data, but only ID-based data, which a new asset lacks. V3 has both, so mature canvases teach the shared model how CLIP embeddings map to member preference and that mapping transfers straight to the sparse ones. The effects compound rather than add, since the V3 short-panel lift (5.691%) exceeds V1 and V2 combined. The lesson is to look for a second blocking factor before concluding that content features do not help.

**Cold-Start Challenge from a New UI Launch**

The real test came from the product change that motivated the work. Netflix was preparing [its largest TV home-screen redesign in a decade](https://www.nytimes.com/2025/05/07/business/media/netflix-new-home-screen.html), which would make short-panel the dominant artwork canvas effectively overnight. This was a cold-start problem in its sharpest form. The canvas about to receive the most impressions had the least historical data, and waiting for short-panel interactions to accumulate would have degraded the user experience. Consolidation lets short-panel selection draw on signal pooled from every canvas, and CLIP embeddings let the unified model personalize a short-panel asset that has gathered very few interactions of its own.

We shipped V3 ahead of the launch and measured it with a month-long holdback A/B test, keeping a small control group on the prior per-canvas model. V3 absorbed the shift immediately, with statistically significant gains on both our core discovery metric and streaming hours, and larger gains than in the steady-state ablation. That stronger result is what we expected, since a sudden shift in which canvas dominates is exactly where V3 should help most.

#### **Query-Aware Artwork Personalization**

Your general taste is the right signal when browsing, but not when *searching*. For example, when searching for a specific actor, you want artwork that features them, even if your broader taste says otherwise. On the Netflix Search Page, the member’s intent is explicit and stated in the query, and the displayed artwork should reflect it.

The same CLIP embeddings we added for cold-start hand us this almost for free. Because CLIP projects text and images into one shared embedding space, we can measure how well a query matches a candidate artwork directly by the cosine similarity between the CLIP text embedding of the query and the CLIP image embedding of the asset. We blend that alignment term with the usual personalization score:

![](https://cdn-images-1.medium.com/max/684/1*WBqt_B0JKOtGAb-TJAe9rQ.png)

Here the personalization term is the score the artwork model above already produces for a member and asset, the second term compares the text embedding of the query against the image embedding of the asset, and the mixing weight *α* between 0 and 1 is tuned through online A/B testing. The first term is “what we think you like”; the second is “what you just asked for,” and *α* sets how much each matters.

Crucially, this took no extra modeling effort. The CLIP embeddings already sit in the asset representation from the artwork work above, so they carry the text-image alignment for free, and we get a query-aware ranker by adding a single similarity term at scoring time. The effect is visible in the search results themselves.

![](https://cdn-images-1.medium.com/max/1024/1*1PKHM3acogKz3mqtcvTNMg.jpeg)

*Query-aware artwork for a search for a specific actor. Each result surfaces an asset that visually features the searched actor, aligning the artwork with the member’s explicit intent.*

### **Personalizing Video Previews via MediaFM**

Video previews raise the bar over still artwork. A video preview unfolds over time, and its appeal comes as much from motion, pacing, dialogue, and soundtrack as from any single frame. Our older video preview personalization models saw none of that. Like the early artwork models, they treated each preview as an opaque ID. Our first content-aware attempt, *SeqCLIP*, described a video preview by its frames, encoding each with a CLIP embedding and then averaging them into one vector. That captured what a video preview *looked* like, but a mean of still frames still misses what it *sounds* like, the dialogue and music that carry so much of a preview’s tone.

To capture the rest, we turned to [**MediaFM**](https://netflixtechblog.com/mediafm-the-multimodal-ai-foundation-for-media-understanding-at-netflix-e8c28df82e2d), Netflix’s first in-house multimodal foundation model. Trained on 80 million shots, MediaFM fuses the following three signals per shot into a single embedding:

* **Visual:** SeqCLIP
* **Audio:** Apretrained speech and audio embedding model
* **Text:** Captions encoded via a large-scale text model

Adopting MediaFM required no new infrastructure, since we simply integrate its shot embeddings into the asset representation, exactly as we did with CLIP embeddings for artwork.

The added modalities paid off. We evaluated both embeddings against the ID-only baseline offline with IPS and then in a five-week online A/B test across all device platforms, and both signals gave the same ordering, MediaFM > SeqCLIP > ID-only, and each step of added content awareness helped, with the gains largest on TV. Offline, both content-aware embeddings beat the ID-only baseline on IPS and MediaFM beat SeqCLIP, as the chart below shows. Online, MediaFM came out on top too, delivering a statistically significant lift in our core streaming metric over the ID-only baseline and outperforming SeqCLIP. This shows that the audio and timed-text signals, which a visual-only encoder like SeqCLIP cannot capture, add real value. We have since shipped MediaFM as the default video preview embedding across all platforms.

![](https://cdn-images-1.medium.com/max/1024/1*xSEADRKgr_tl-ukj5G0jWQ.png)

*Relative offline IPS lift for the two content-aware video preview embeddings, each measured against the ID-only baseline at the zero rule. Adding visual content awareness helps, and adding audio and timed text on top of it helps further.*

#### **Choosing Embeddings Cheaply with a Proxy Task**

New embeddings arrive constantly, but end-to-end trials are expensive, which cost data engineering, model retraining, and weeks of A/B test traffic. We couldn’t afford to run the full pipeline for every candidate, so we gated the funnel with a cheap question:

*From the content embedding alone, can you predict which asset wins under a plain, unpersonalized policy?*

We first select a fixed set of titles. For each title we use exploration data to find its debiased popularity winner, the asset with the highest interaction rate after we adjust for how often it was shown using its propensity score. We mark this winner with a binary label, 1 for the winner and 0 otherwise. We then train a linear probe to recover that label from the asset embedding alone, with no title, cast, or metadata, by minimizing the standard binary cross-entropy loss:

![](https://cdn-images-1.medium.com/max/740/1*xy3qKnj9Dbnl8_bD1E69gg.png)

Keeping the probe linear and embedding-only is intentional, since it isolates how much of an asset’s popularity is actually encoded in the embedding. If the embedding captures the semantic drivers of popularity, a simple linear classifier should be able to identify likely winners. If it does not, the probe performs no better than random guessing, which is the baseline we score it against.

We first used the linear probe to screen and prune a broad set of candidate embeddings before modifying any production pipeline, narrowing the field to two finalists, SeqCLIP and the leading MediaFM variant. We then carried both through full offline evaluation and online A/B testing. All three signals, the linear probe accuracies, the offline IPS lifts, and the online A/B results, ranked MediaFM ahead of SeqCLIP, as the chart below shows. That alignment is why the linear probe now gates every new MediaFM version before release.

![](https://cdn-images-1.medium.com/max/1024/1*tNTPjIK7UQ4RbzFvshqNww.png)

*Linear probe Δaccuracy, offline IPS lift, and online A/B metric lift for the two finalists. All three agree that MediaFM beats SeqCLIP. The online panel is measured against the ID-based baseline, with its values withheld.*

### **The Netflix Embedding Store**

None of this would be practical without shared infrastructure. Every embedding in this post, CLIP for artwork, SeqCLIP and MediaFM for video previews, lives in the **Netflix Embedding Store**, a component of Netflix’s AI Platform that hosts dense embeddings for titles, games, member profiles and multimedia assets. A foundation model encodes raw asset content into a dense vector once, and the Embedding Store serves that vector to every downstream system, the artwork model, the query-aware ranker, the video preview model, and others, through the same interface. Crucially, it serves the exact same embeddings at training time and at online inference time, so there is no skew between what a model learns from and what it sees in production.

Its key property is that it *decouples foundation-model updates from personalization-model deployments*. A new embedding, or a new version of an existing one, can be registered, backfilled across the catalog, and validated entirely on its own, without touching the training or serving code of any model that consumes it. Once it is in the Embedding Store, it becomes available to every ranking and personalization model through configuration alone, no downstream code changes, no coordinated release. This is what let us swap CLIP into the artwork model, stand up the query-aware ranker on the same vectors, and roll MediaFM through the video preview model, each as an independent change rather than a cross-team migration.

![](https://cdn-images-1.medium.com/max/1024/1*FpXX9LHddIpQiHwx7PNDqQ.png)

*Foundation-model embeddings (CLIP, SeqCLIP, MediaFM) are stored once and consumed by every downstream system: artwork, query-aware artwork, video previews, and other rankers.*

### **What We Learned, and What’s Next**

Three lessons stood out.

1. **Pretrained CLIP embeddings** let us consolidate five artwork models into one while boosting performance on data-starved canvases. This benefit became especially clear when the redesigned TV home screen rolled out.
2. **For video, multimodality wins decisively.** The audio and text signals that a purely visual encoder cannot access pushed MediaFM past SeqCLIP.
3. **A cheap proxy task yields big savings**, efficiently pruning the candidate set before running full end-to-end experiments and online A/B tests.

Next, we aim to extend the Embedding Store toward a single **shared semantic space for image, text, and video**. Such a unified representation would enable cross-modal retrieval, such as matching a video preview to a search query, or a static artwork to the video preview it was derived from, as well as unified asset ranking across surface types and a more cohesive, intuitive discovery experience for members everywhere.

### Acknowledgements

We thank [Aneesh Vartakavi](https://www.linkedin.com/in/aneeshvartakavi/), [Santiago Castro](https://www.linkedin.com/in/santiagocastroserra/), and [Avneesh Saluja](https://www.linkedin.com/in/avneesh/) for the CLIP embedding and MediaFM work that made the content-aware models described here possible, and [Ratna Kavuri](https://www.linkedin.com/in/rkavuri/) for the backend systems that serve multimedia personalization in production.

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=32f96320785e)

---

[MAPS: Netflix’s Multimodal Asset Personalization at Scale](https://netflixtechblog.com/maps-netflixs-multimodal-asset-personalization-at-scale-32f96320785e) was originally published in [Netflix TechBlog](https://netflixtechblog.com) on Medium, where people are continuing the conversation by highlighting and responding to this story.
