---
title: "Vectorization Of Narrow Matrix Multiplication for Ascend AI Inference Acceleration"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.16009
priority: medium
status: unread
interest: medium
next_step: skim
---
# Vectorization Of Narrow Matrix Multiplication for Ascend AI Inference Acceleration
> 原文: [https://arxiv.org/abs/2609.16009](https://arxiv.org/abs/2609.16009)

arXiv:2609.16009v1 Announce Type: new
Abstract: This research proposes and evaluates a novel approach to optimizing matrix multiplication (MatMul) on Huawei Ascend NPUs, motivated by a key insight: during matrix-vector multiplication (narrow MatMul), the Cube Unit (AIC) is often underutilized, while the Vector Unit (AIV) remains idle for most of the operator runtime. In this paper, we introduce the MatMul algorithm, which uses vector instructions of AscendC to effectively offload computations from the Cube Unit to the Vector Unit. The algorithm was tested and applied to accelerating the inference of MLA DeepSeek-V3 operator. By successfully overlapping AIV and AIC computations, our optimization showed a mean performance gain of 20% for a single token processing scenario. Our work addresses a significant gap in the literature on practical optimization techniques for AscendC, despite the availability of documentation and the active CANN community.
