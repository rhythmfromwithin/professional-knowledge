---
interest: medium
link: https://arxiv.org/abs/2607.00394
next_step: skim
priority: low
slack_ts: '1782965373.282089'
source: cs.DB - Databases
status: unread
title: 'When Classic Cache Policies Fail: Learning-Augmented Replacement for Semantic
  Retrieval Buffers'
---
# When Classic Cache Policies Fail: Learning-Augmented Replacement for Semantic Retrieval Buffers
> 原文: [https://arxiv.org/abs/2607.00394](https://arxiv.org/abs/2607.00394)

arXiv:2607.00394v1 Announce Type: new
Abstract: LLM agents increasingly rely on retrieval buffers to store and reuse past experience, yet the cache management policies governing these buffers remain largely ad-hoc. We formalize this as an online semantic cache replacement problem with switching costs, where items are matched by embedding similarity and hit quality is continuous rather than binary. Through experiments on two datasets from MemoryBench-Full (LoCoMo, DialSim) with 8 replacement policies, we reveal a surprising finding: classic heuristics (LRU, LFU) \emph{consistently underperform} the naive FIFO baseline on semantic workloads, due to the absence of temporal locality and frequency concentration. We propose SOLAR, a learning-augmented framework that derives modification timing from regret accumulation (achieving $\sim$17\% modification rate) and content selection from Bayesian online learning over implicit retrieval feedback. We prove SOLAR achieves a constant competitive ratio $\leq 3$, independent of cache size and horizon (vs.\ $\Omega(K)$ for FIFO), and eviction regret $O(\sqrt{KT\log T})$, matching the $\Omega(\sqrt{KT})$ lower bound up to logarithmic factors. Experiments demonstrate 5--75\% relative improvement over FIFO at tight cache sizes, with a clearly characterized phase transition at the working set boundary. Synthetic experiments with 5000-item pools further reveal an inverted-U relationship between pool size and retrieval quality, justifying capacity constraints as a retrieval noise phenomenon rather than a storage limitation.
