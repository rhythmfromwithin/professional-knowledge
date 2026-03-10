---
title: "Progressive Refinement Regulation for Accelerating Diffusion Language Model Decoding"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2603.04514
priority: high
status: unread
interest: medium
next_step: skim
---
# Progressive Refinement Regulation for Accelerating Diffusion Language Model Decoding
> 原文: [https://arxiv.org/abs/2603.04514](https://arxiv.org/abs/2603.04514)

arXiv:2603.04514v1 Announce Type: new
Abstract: Diffusion language models generate text through iterative denoising under a uniform refinement rule applied to all tokens. However, tokens stabilize at different rates in practice, leading to substantial redundant refinement and motivating refinement control over the denoising process. Existing approaches typically assess refinement necessity from instantaneous, step-level signals under a fixed decoding process. In contrast, whether a token has converged is defined by how its prediction changes along its future refinement trajectory. Moreover, changing the refinement rule reshapes future refinement trajectories, which in turn determine how refinement rules should be formulated, making refinement control inherently dynamic. We propose \emph{Progressive Refinement Regulation} (PRR), a progressive, trajectory-grounded refinement control framework that derives a token-level notion of empirical convergence progress from full decoding rollouts. Based on this signal, PRR learns a lightweight token-wise controller to regulate refinement via temperature-based distribution shaping under a progressive self-evolving training scheme. Experiments show that PRR substantially accelerates diffusion language model decoding while preserving generation quality.
