---
title: "TSA: Temporal Slot Activation for Persistent Object-Centric Video Representation"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2606.13714
priority: medium
status: unread
interest: medium
next_step: skim
---
# TSA: Temporal Slot Activation for Persistent Object-Centric Video Representation
> 原文: [https://arxiv.org/abs/2606.13714](https://arxiv.org/abs/2606.13714)

arXiv:2606.13714v1 Announce Type: new
Abstract: Unsupervised video object-centric learning aims to decompose dynamic scenes into temporally persistent entity representations. Existing recurrent video slot-attention methods propagate a fixed set of slots across frames, but typically assume unconditional slot propagation: every slot is updated and decoded at every frame, regardless of whether its corresponding object is visible. We show that this design violates a basic lifecycle requirement for persistent slots: when an object is absent or fully occluded, its slot should preserve its previous state and avoid explaining unrelated visible content. Instead, unconditional propagation creates two failure pathways: update-induced state drift, where current-frame evidence overwrites the absent object's representation, and decoder-induced reconstruction interference, where the inactive slot remains coupled to reconstruction through decoder attention. We propose Temporal Slot Activation (TSA), a mechanism that learns a per-slot, per-frame activation score $\alpha\_{k,t} \in (0, 1)$ without visibility supervision. TSA uses this activation as a shared latent control variable for slot lifecycle modeling. When a slot is inactive, TSA anchors its state to the previous slot via activation-gated updating and suppresses its decoder participation through an activation-dependent additive bias on attention logits before softmax normalization. This jointly reduces state drift and reconstruction-driven interference. To improve decisions under partial occlusion and gradual reappearance, TSA further conditions activation prediction on a per-slot temporal memory produced by a Temporal Context Encoder. We evaluate TSA on MOVi-C/E, YT-VIS, and OVIS benchmarks using both standard and tracking-based metrics (FG-ARI, mBO, IDF1, HOTA). TSA consistently improves object decomposition and temporal identity preservation, with large gains on long, heavily occluded videos.
