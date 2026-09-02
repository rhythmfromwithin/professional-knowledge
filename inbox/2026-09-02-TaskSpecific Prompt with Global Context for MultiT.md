---
interest: medium
link: https://arxiv.org/abs/2609.00047
next_step: skim
priority: high
slack_ts: '1788321945.580629'
source: cs.LG - Machine Learning
status: unread
title: Task-Specific Prompt with Global Context for Multi-Task Graph Pre-Training
---
# Task-Specific Prompt with Global Context for Multi-Task Graph Pre-Training
> 原文: [https://arxiv.org/abs/2609.00047](https://arxiv.org/abs/2609.00047)

arXiv:2609.00047v1 Announce Type: new
Abstract: Graph prompt learning is an effective paradigm to adapt pre-trained graph models to downstream tasks in low-resource scenarios. However, existing multi-task graph pre-training frameworks generally use randomly initialized prompts, leading to poor alignment between the prompt space, pretext objectives and graph structural characteristics. This greatly weakens the task relevance, structural awareness and transferability of prompt representations. To address this challenge, we propose TPGC, a dual-prior prompt initialization solution that explicitly models the synergy between task prior and structural prior. Specifically, the Task-Prior Injection Module first conducts a short homologous multi-task pre-training on an auxiliary graph, enabling prompt initialization to inherit optimization preferences associated with multiple pretext tasks. Built on the task-aware representations, the Structure-Prior Injection Module further extracts transferable global structural context from the auxiliary graph, converting it into layer-wise prompt vectors by aggregating structurally informative node embeddings. Extensive experiments on 6 mainstream benchmarks covering node and graph classification show that TPGC achieves consistently better performance under few-shot settings than state-of-the-art baselines, with fewer downstream tunable parameters and lower runtime. The code is available at https://github.com/Virgilqiu/TPGC
