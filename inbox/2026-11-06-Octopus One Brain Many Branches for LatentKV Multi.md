---
interest: medium
link: https://arxiv.org/abs/2611.06956
next_step: skim
priority: high
slack_ts: '1794116481.511229'
source: cs.LG - Machine Learning
status: unread
title: 'Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement
  Learning'
---
# Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement Learning
> 原文: [https://arxiv.org/abs/2611.06956](https://arxiv.org/abs/2611.06956)

arXiv:2611.06956v1 Announce Type: new
Abstract: Multi-agent LLM systems explore in parallel by spawning sub-agents with isolated context windows, whereas single-agent systems append every search and verification step into one growing trajectory. However, existing multi-agent frameworks duplicate prefix KV caches across branches, exchange findings by re-prefilling text summaries, and flatten or drop cross-branch dependencies during reinforcement learning (RL).
We introduce Octopus, a single-model multi-agent RL framework in which all threads share one backbone and coordinate over a GPU-resident directed acyclic graph (DAG) of KV states through five primitives (fork, read\_thread, wait\_threads, rewind, commit). Octopus combines three co-designed mechanisms: (1) Zero-Copy Radix Forking, which spawns branches as $\mathcal{O}(1)$ cursor views over shared physical KV pages; (2) Attention-Only KV Mounting, which mounts a sibling thread's terminal KV blocks directly into full-attention layers while bypassing linear-recurrent states (Gated DeltaNet / Mamba-2), cutting off-task hijacking by $21\times$ ($57.9\% \to 2.7\%$) while retaining $92.2\%$ of full-text mutual information at zero extra KV allocation; and (3) a Packed DAG-GRPO Trainer, which packs all episode branches into one block-sparse attention pass and assigns counterfactual branch credit via leave-one-branch-out marginal rewards.
Trained end-to-end with GRPO on Qwen3.5-4B over a sparse BM25 corpus, Octopus reaches $49.6\%$ accuracy on BrowseComp-Plus ($+17.5$ points over single-agent GRPO at 143K context and $+12.5$ points over text-summary multi-agent RL) and $51.2\%$ on OpenResearcher, outperforming dense-retrieval agents up to $250\times$ larger while increasing training throughput $3.3\times$ and cutting peak KV memory $2.8\times$.
