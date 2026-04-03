---
interest: medium
link: https://arxiv.org/abs/2603.26775
next_step: skim
priority: high
slack_ts: '1775185054.842139'
source: cs.LG - Machine Learning
status: unread
title: Learning to Select Visual In-Context Demonstrations
---
# Learning to Select Visual In-Context Demonstrations
> 原文: [https://arxiv.org/abs/2603.26775](https://arxiv.org/abs/2603.26775)

arXiv:2603.26775v1 Announce Type: new
Abstract: Multimodal Large Language Models (MLLMs) adapt to visual tasks via in-context learning (ICL), which relies heavily on demonstration quality. The dominant demonstration selection strategy is unsupervised k-Nearest Neighbor (kNN) search. While simple, this similarity-first approach is sub-optimal for complex factual regression tasks; it selects redundant examples that fail to capture the task's full output range. We reframe selection as a sequential decision-making problem and introduce Learning to Select Demonstrations (LSD), training a Reinforcement Learning agent to construct optimal demonstration sets. Using a Dueling DQN with a query-centric Transformer Decoder, our agent learns a policy that maximizes MLLM downstream performance. Evaluating across five visual regression benchmarks, we uncover a crucial dichotomy: while kNN remains optimal for subjective preference tasks, LSD significantly outperforms baselines on objective, factual regression tasks. By balancing visual relevance with diversity, LSD better defines regression boundaries, illuminating when learned selection is strictly necessary for visual ICL.
