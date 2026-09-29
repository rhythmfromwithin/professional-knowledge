---
interest: medium
link: https://arxiv.org/abs/2609.30393
next_step: skim
priority: medium
slack_ts: '1790659452.550939'
source: cs.CV - Computer Vision
status: unread
title: 'LiTe-GS: Oracle-Efficient Next Best View Selection for 3D Gaussian Splatting'
---
# LiTe-GS: Oracle-Efficient Next Best View Selection for 3D Gaussian Splatting
> 原文: [https://arxiv.org/abs/2609.30393](https://arxiv.org/abs/2609.30393)

arXiv:2609.30393v1 Announce Type: new
Abstract: Selecting informative camera views is critical for efficient training and adaptive refinement in 3D Gaussian Splatting, where each observation significantly influences model parameters. However, information-driven view-selection strategies can require repeated evaluations of expensive information-gain oracles as the number of candidate views increases. We propose LiTe-GS, an oracle-efficient method for next best view selection in 3D Gaussian Splatting. LiTe-GS reduces the number of information-oracle evaluations by performing randomized subset evaluation of candidate views rather than exhaustively scoring the full candidate pool. The resulting approach achieves expected $O(M\log(1/\epsilon))$ oracle complexity with respect to the number of candidate views $M$, independent of the selection cardinality $K$, while providing an explicit trade-off between oracle efficiency and approximation quality through $\epsilon$. We provide theoretical guarantees on oracle complexity and approximation performance under the proposed selection scheme. Experiments on Blender and Mip-NeRF 360 demonstrate that LiTe-GS maintains reconstruction quality comparable to Fisher-information-based baselines while substantially reducing the number of Fisher-oracle evaluations across different acquisition settings.
