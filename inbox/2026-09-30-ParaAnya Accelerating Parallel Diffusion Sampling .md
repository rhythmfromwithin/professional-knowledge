---
interest: medium
link: https://arxiv.org/abs/2609.36522
next_step: skim
priority: medium
slack_ts: '1790918085.248839'
source: cs.DC - Distributed Computing
status: unread
title: 'ParaAnya: Accelerating Parallel Diffusion Sampling with Plug-and-Play Output
  Caching'
---
# ParaAnya: Accelerating Parallel Diffusion Sampling with Plug-and-Play Output Caching
> 原文: [https://arxiv.org/abs/2609.36522](https://arxiv.org/abs/2609.36522)

arXiv:2609.36522v1 Announce Type: new
Abstract: Diffusion models have achieved remarkable success in generative tasks, but their inherently sequential sampling process introduces a severe computational bottleneck. Recent Parallel-in-Time (PinT) solvers attempt to mitigate this by parallelizing generation across a sliding window of timesteps, advancing the window only when step-wise changes stabilize. However, this overlapping window mechanism forces the network to repeatedly evaluate the same timesteps. When the input variations between iterations are minimal, these redundant evaluations lead to significant computational waste. To address this inefficiency, we propose ParaAnya, an output cache mechanism agnostic to the parallel sampling algorithm that can reduce the number of function evaluations (NFE). ParaAnya caches input-output pairs of diffusion models and reuses the cached output at overlapping timesteps. By dispatching only cache-miss timesteps to GPU workers, our approach eliminates redundant computation while preserving the structure of the underlying algorithms' update rules. We integrate ParaAnya into four representative parallel sampling algorithms and evaluate its performance on Stable Diffusion v1.5. Across four parallel samplers evaluated with DDIM on eight GPUs, ParaAnya provides $1.30$--$2.43\times$ speedups over their uncached counterparts and reduces NFE by up to 70.1\%, reaching up to a $5.62\times$ speedup over single-GPU serial sampling while maintaining comparable CLIP scores.
