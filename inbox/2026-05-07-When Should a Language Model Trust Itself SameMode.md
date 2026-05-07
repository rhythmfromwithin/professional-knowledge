---
title: "When Should a Language Model Trust Itself? Same-Model Self-Verification as a Conditional Confidence Signal"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2605.02915
priority: high
status: unread
interest: medium
next_step: skim
---
# When Should a Language Model Trust Itself? Same-Model Self-Verification as a Conditional Confidence Signal
> 原文: [https://arxiv.org/abs/2605.02915](https://arxiv.org/abs/2605.02915)

arXiv:2605.02915v1 Announce Type: new
Abstract: Same-model self-verification, prompting a model to audit its own predicted answer, is a plausible confidence signal for selective prediction, but its practical value remains unclear once strong likelihood-based baselines are taken seriously. We evaluate self-verification against two such baselines, LL-AVG and LL-SUM, on ARC-Challenge and TruthfulQA-MC across multiple model families, scales, and prompt variants. We measure not only correctness ranking, but also abstention quality through AURC and operating-point analyses. The results are sharply task- and model-dependent. On ARC-Challenge, self-verification substantially improves over LL-AVG for Phi-2 and the Qwen models, with the largest gains appearing in Qwen-7B. On TruthfulQA-MC, however, the signal is less reliable: smaller models can become prompt-sensitive, DeepSeek-R1-Distill-8B degrades relative to LL-AVG, and LL-SUM often remains the stronger practical baseline. We therefore do not treat self-verification as a general-purpose uncertainty estimator. In this setting, it is better understood as a conditional confidence signal whose value depends on task type, model family, prompt formulation, and, crucially, the baseline it must beat.
