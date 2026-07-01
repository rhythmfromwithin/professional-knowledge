---
interest: medium
link: https://arxiv.org/abs/2606.30686
next_step: skim
priority: medium
slack_ts: '1782880936.136119'
source: cs.RO - Robotics
status: unread
title: 'Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical
  Reasoning'
---
# Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning
> 原文: [https://arxiv.org/abs/2606.30686](https://arxiv.org/abs/2606.30686)

arXiv:2606.30686v1 Announce Type: new
Abstract: Vision-Language-Action (VLA) systems, built on pretrained vision-language models (VLMs), have shown rapidly improving performance on robot manipulation benchmarks. These gains are commonly interpreted as evidence that semantic representations learned from internet-scale data transfer to physical execution generalization. This position paper argues that the assumption underlying this interpretation -- that semantic generalization is sufficient to support physical action decisions -- has not been independently verified and cannot be tested under current evaluation protocols. We support this claim by decomposing VLA policies into semantic mapping and physical action decision, and showing that task success rate -- the dominant evaluation metric -- cannot distinguish between these two sources of capability. As a result, improvements in benchmark performance are consistent with multiple competing explanations, including semantic matching, distributional overlap, and genuine physical generalization. We further argue that this identifiability gap has been reinforced through narrative drift, whereby successive systems inherit and strengthen prior interpretations of performance gains without isolating the underlying causal mechanism. To address this limitation, we propose a research direction based on evaluation designs that introduce controlled variation to separately measure semantic and physical generalization. Such designs make it possible to causally attribute performance without requiring access to model internals, and to empirically assess the role of VLM backbones as semantic interfaces rather than implicit sources of physical competence. Our goal is not to refute the role of VLMs in robotics, but to clarify the conditions under which claims of physical generalization can be meaningfully evaluated.
