---
title: "ES-AHD: An Evolution Strategy Framework for Automatic Heuristic Design"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2609.00023
priority: low
status: unread
interest: medium
next_step: skim
---
# ES-AHD: An Evolution Strategy Framework for Automatic Heuristic Design
> 原文: [https://arxiv.org/abs/2609.00023](https://arxiv.org/abs/2609.00023)

arXiv:2609.00023v1 Announce Type: new
Abstract: In this paper, we introduce ES-AHD, a novel framework that fundamentally integrates Evolution Strategy (ES) into Large Language Model (LLM)-driven Automatic Heuristic Design (AHD). Existing evolutionary approaches predominantly rely on random, individual-level mutation, leading to blind search and an imbalance between exploration and exploitation. To address these issues, ES-AHD introduces two core mechanisms. First, Semantic Recombination via LLMs discards traditional point-to-point reproduction. By leveraging the LLM's contextual reasoning to explicitly extract core insights from top-performing individuals, the algorithm establishes a promising semantic search direction. This transforms random code mutation into targeted, center-guided sampling inspired by ES. Second, Stochastic Covariance Adaptation via Temperature Sampling dynamically addresses the exploration-exploitation dilemma. By mapping the covariance matrix in ES to the LLM's sampling temperature, the framework employs a stochastic random walk mechanism with momentum. This approach primarily shrinks the search radius for micro-level code refinement, while retaining the critical ability to occasionally sample higher temperatures to escape semantic local optima. Ultimately, ES-AHD provides a highly directional, robust, and efficient search paradigm, significantly accelerating the generation of high-quality heuristic algorithms. The source code is available at: https://github.com/Mriya0306/ES-AHD.
