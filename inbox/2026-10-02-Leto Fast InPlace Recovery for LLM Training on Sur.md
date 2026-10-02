---
title: "Leto: Fast In-Place Recovery for LLM Training on Surviving Hardware"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.00687
priority: medium
status: unread
interest: medium
next_step: skim
---
# Leto: Fast In-Place Recovery for LLM Training on Surviving Hardware
> 原文: [https://arxiv.org/abs/2610.00687](https://arxiv.org/abs/2610.00687)

arXiv:2610.00687v1 Announce Type: new
Abstract: Hardware-operable failures (HOFs) interrupt large language model (LLM) training but permit recovery on the same hardware without reset, repair, or replacement. Existing recovery systems nevertheless reload checkpoints, recompute lost progress, and rebuild process state, idling GPUs that could otherwise continue training.
We present Leto, a fault-tolerant training system that leverages surviving hardware to enable efficient in-place recovery. Our key insight is that the state needed to resume training can be retained or prepared outside the active training process while remaining on the same hardware. Leto retains the working model state and the reusable process state, and preinitializes the remaining state in a shadow trainer. We devise two-tier erasure protection and chunk-level transactional updates to keep the retained model state recoverable and consistent, and reclaim the shadow state when active training needs its GPU memory. Evaluation on 6- and 72-GPU NVIDIA A100 clusters shows that Leto recovers 3.6--6.5$\times$ faster than the best-performing checkpointing baselines and improves productive training time by up to 13.7 percentage points. Large-scale simulation shows over 95% productive training time on a 131,072-GPU cluster.
