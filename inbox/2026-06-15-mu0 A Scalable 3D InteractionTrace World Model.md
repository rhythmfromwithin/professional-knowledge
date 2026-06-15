---
title: "$\mu_0$: A Scalable 3D Interaction-Trace World Model"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2606.13769
priority: medium
status: unread
interest: medium
next_step: skim
---
# $\mu_0$: A Scalable 3D Interaction-Trace World Model
> 原文: [https://arxiv.org/abs/2606.13769](https://arxiv.org/abs/2606.13769)

arXiv:2606.13769v1 Announce Type: new
Abstract: World models that capture how actions induce physical change enable scalable robot learning without reliance on embodiment-specific action labels. Pixel-space video models provide broad visual priors but expend model capacity on dense appearance reconstruction, while direct action models require embodiment-specific labels that hinder scalability. We present $\mu\_0$, a scalable world model based on 3D traces. Rather than predicting dense pixels or directly modeling actions, $\mu\_0$ forecasts smooth 3D trajectories for salient interaction points such as objects, tools, hands, and contact regions, yielding a compact, embodiment-agnostic motion interface. To enable training from diverse video sources, our TraceExtract system automatically extracts 3D supervision by selecting keypoints, constructing globally aligned traces, and associating motion segments with hierarchical language captions. This TraceExtract supervision pretrains $\mu\_0$ by combining a pretrained vision-language backbone with a modular trace expert, which represents each query via B-spline control points and predicts future traces. Experiments show that $\mu\_0$ outperforms baselines in both 2D and 3D trace prediction, including trace prediction models and tokenized VLM methods. Because $\mu\_0$ is frozen and reusable, it can be paired with action experts for downstream robot embodiments. Despite action-free pretraining, the resulting trace-conditioned policies achieve performance competitive with VLA models pretrained with action supervision, such as $\pi\_0$. These results establish 3D traces as a scalable and transferable representation for cross-embodiment manipulation.
