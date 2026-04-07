---
interest: medium
link: https://arxiv.org/abs/2604.02392
next_step: skim
priority: medium
slack_ts: '1775531920.921809'
source: cs.CV - Computer Vision
status: unread
title: 'Beyond Fixed Inference: Quantitative Flow Matching for Adaptive Image Denoising'
---
# Beyond Fixed Inference: Quantitative Flow Matching for Adaptive Image Denoising
> 原文: [https://arxiv.org/abs/2604.02392](https://arxiv.org/abs/2604.02392)

arXiv:2604.02392v1 Announce Type: new
Abstract: Diffusion and flow-based generative models have shown strong potential for image restoration. However, image denoising under unknown and varying noise conditions remains challenging, because the learned vector fields may become inconsistent across different noise levels, leading to degraded restoration quality under mismatch between training and inference. To address this issue, we propose a quantitative flow matching framework for adaptive image denoising. The method first estimates the input noise level from local pixel statistics, and then uses this quantitative estimate to adapt the inference trajectory, including the starting point, the number of integration steps, and the step-size schedule. In this way, the denoising process is better aligned with the actual corruption level of each input, reducing unnecessary computation for lightly corrupted images while providing sufficient refinement for heavily degraded ones. By coupling quantitative noise estimation with noise-adaptive flow inference, the proposed method improves both restoration accuracy and inference efficiency. Extensive experiments on natural, medical, and microscopy images demonstrate its robustness and strong generalization across diverse noise levels and imaging conditions.
