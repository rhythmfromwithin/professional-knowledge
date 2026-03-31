---
title: "Consistency Amplifies: How Behavioral Variance Shapes Agent Accuracy"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.25764
priority: low
status: unread
interest: medium
next_step: skim
---
# Consistency Amplifies: How Behavioral Variance Shapes Agent Accuracy
> 原文: [https://arxiv.org/abs/2603.25764](https://arxiv.org/abs/2603.25764)

arXiv:2603.25764v1 Announce Type: new
Abstract: As LLM-based agents are deployed in production systems, understanding their behavioral consistency (whether they produce similar action sequences when given identical tasks) becomes critical for reliability. We study consistency in the context of SWE-bench, a challenging software engineering benchmark requiring complex, multi-step reasoning. Comparing Claude~4.5~Sonnet, GPT-5, and Llama-3.1-70B across 50 runs each (10 tasks $\times$ 5 runs), we find that across models, higher consistency aligns with higher accuracy: Claude achieves the lowest variance (CV: 15.2\%) and highest accuracy (58\%), GPT-5 is intermediate (CV: 32.2\%, accuracy: 32\%), and Llama shows the highest variance (CV: 47.0\%) with lowest accuracy (4\%). However, within a model, consistency can amplify both correct and incorrect interpretations. Our analysis reveals a critical nuance: \textbf{consistency amplifies outcomes rather than guaranteeing correctness}. 71\% of Claude's failures stem from "consistent wrong interpretation": making the same incorrect assumption across all runs. Interestingly, GPT-5 achieves similar early strategic agreement as Claude (diverging at step 3.4 vs.\ 3.2) but exhibits 2.1$\times$ higher variance, suggesting that divergence timing alone does not determine consistency. These findings suggest that for production deployment, interpretation accuracy matters more than execution consistency, with implications for agent evaluation and training.
