---
title: "Maximizing mutual information between user-contexts and responses improve LLM personalization with no additional data"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.19294
priority: high
status: unread
interest: medium
next_step: skim
---
# Maximizing mutual information between user-contexts and responses improve LLM personalization with no additional data
> 原文: [https://arxiv.org/abs/2603.19294](https://arxiv.org/abs/2603.19294)

arXiv:2603.19294v1 Announce Type: new
Abstract: While post-training has successfully improved large language models (LLMs) across a variety of domains, these gains heavily rely on human-labeled data or external verifiers. Existing data has already been exploited, and new high-quality data is expensive to collect. More fundamentally, true intelligence goes far beyond tasks that are easily verifiable. Therefore, we need self-improvement frameworks that allow models to improve without external oversight. We propose \*Mutual Information Preference Optimization (MIPO)\*, a contrastive data augmentation method that constructs preference pairs by generating a positive response conditioning on the correct prompt, and a negative response by conditioning on a random, unrelated prompt. We show that using Direct Preference Optimization (DPO) to learn from this paired data maximizes pointwise conditional mutual information (MI) (under the base LLM) between prompts and model responses. Empirical results with various-sized Llama- and Qwen-Instruct models show that when used to maximize MI between user context and response, MIPO provides an effective personalization technique, achieving 3-40% improvements on personalization tasks using real-user datasets compared to strong baselines. Surprisingly, MIPO can also be applied to improve performance on math and multiple-choice problems, yielding 1-18% \*\*without any additional data or human supervision\*\*. These results suggest a promising direction for self-improvement.
