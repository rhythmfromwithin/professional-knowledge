---
title: "Can AI Evaluate AI Scientists? A Benchmarking Study of Autonomous Research Generation Systems Using Automated Multi-Model Review"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2607.28631
priority: high
status: unread
interest: medium
next_step: skim
---
# Can AI Evaluate AI Scientists? A Benchmarking Study of Autonomous Research Generation Systems Using Automated Multi-Model Review
> 原文: [https://arxiv.org/abs/2607.28631](https://arxiv.org/abs/2607.28631)

arXiv:2607.28631v1 Announce Type: new
Abstract: AI Scientist systems capable of autonomous research have the potential to significantly accelerate scientific discovery. However, evaluating and comparing the quality of AI-generated papers remains an open challenge. We propose and implement a rigorous benchmarking protocol using an automated peer-review system that harnesses frontier large language models to assess scientific papers across four core dimensions: originality, scientific rigor, clarity, and significance. We evaluate four leading AI Scientist frameworks: \textit{Sakana AI (v1 & v2)}, \textit{CycleResearcher}, and \textit{Data-to-Paper}. Each framework was run on a consistent set of 15 research proposals published by a commercial autonomous AI scientist company (FARS), generating 60 papers that we evaluate alongside 15 FARS benchmark papers. Using three independent LLM reviewers (GPT-5.4, Gemini, and Claude), we find that FARS benchmark papers significantly outperform all competing frameworks, achieving mean scores of 2.14--2.47 on a 1--5 scale compared to 1.00--1.87 for other systems. Notably, FARS scores are more than 2$\times$ higher than the next-best systems on Gemini and Claude evaluations. We find strong agreement among Gemini and Claude ($\rho$ = 0.907, $p < 0.001$), and both correlate extremely strongly with the synthesis score ($\rho$ = 0.961, $p < 0.001$), validating the reliability of automated evaluation. However, GPT-5.4 exhibits weaker agreement ($\rho \approx 0.32$), suggesting it evaluates papers using different criteria. These results establish the first quantitative benchmark for AI Scientist systems and demonstrate that multi-model LLM evaluation provides a scalable, consistent framework for assessing autonomous research quality.
