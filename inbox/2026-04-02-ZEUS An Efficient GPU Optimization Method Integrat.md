---
interest: medium
link: https://arxiv.org/abs/2603.28770
next_step: skim
priority: medium
slack_ts: '1775098547.196919'
source: cs.DC - Distributed Computing
status: unread
title: 'ZEUS: An Efficient GPU Optimization Method Integrating PSO, BFGS, and Automatic
  Differentiation'
---
# ZEUS: An Efficient GPU Optimization Method Integrating PSO, BFGS, and Automatic Differentiation
> 原文: [https://arxiv.org/abs/2603.28770](https://arxiv.org/abs/2603.28770)

arXiv:2603.28770v1 Announce Type: new
Abstract: We introduce a novel, efficient computational method, ZEUS, for numerical optimization, and provide an open-source implementation. It has four key ingredients: (1) particle swarm optimization (PSO), (2) the use of the Broyden-Fletcher-Goldfarb-Shanno (BFGS) method, (3) automatic differentiation (AD), and (4) GPUs. Our approach addresses the computational challenges inherent in high-dimensional, non-convex optimization problems. In the first phase of the algorithm, we get a potentially good set of starting points using PSO. Thereafter, we run BFGS independently in parallel from these starting points. BFGS is one of the best-performing algorithms for numerical optimization. However, it requires the gradient of the function being optimized. ZEUS integrates automatic differentiation into BFGS thus avoiding the need for the user to calculate derivatives explicitly. The use of GPUs allows ZEUS to speed up the calculations substantially. We carry out systematic studies to explore the trade-offs between the number of PSO iterations taken, starting points, and BFGS iteration depth. We show that a handful of iterations of PSO can improve global convergence when combined with BFGS. We also present performance studies using common test functions. The source code can be found at https://github.com/fnal-numerics/global-optimizer-gpu.
