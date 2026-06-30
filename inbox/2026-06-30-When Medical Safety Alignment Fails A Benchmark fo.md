---
title: "When Medical Safety Alignment Fails: A Benchmark for Evaluating LLMs on High-Risk Medical Queries"
source: "cs.CY - Computers and Society"
link: https://arxiv.org/abs/2606.28332
priority: medium
status: unread
interest: medium
next_step: skim
---
# When Medical Safety Alignment Fails: A Benchmark for Evaluating LLMs on High-Risk Medical Queries
> 原文: [https://arxiv.org/abs/2606.28332](https://arxiv.org/abs/2606.28332)

arXiv:2606.28332v1 Announce Type: new
Abstract: Large language models (LLMs) are increasingly used for medical and health-related questions, yet their safety in high-risk medical scenarios remains poorly understood. We introduce \textsc{MedHarm}\footnote{Code and data will be released upon acceptance. Due to the sensitive nature of high-risk medical queries, data access will be available to qualified researchers upon request.}, a high-risk medical safety benchmark with 1,100 medically grounded queries across 10 safety-critical categories, including toxicology, pharmacology, covert poisoning, anesthesia, and fetal harm. Unlike broad medical QA benchmarks, \textsc{MedHarm} targets realistic clinical, educational, and technical prompts that require refusal, caution, or safe redirection rather than direct helpfulness. We evaluate 15 LLMs spanning general-purpose, medical-purpose, closed-source, and downstream SFT models, together with 4 representative guardrail models. Results reveal a substantial gap between apparent alignment and medical safety: aligned models can still produce unsafe or actionable responses, medical fine-tuning can amplify harmful specificity, and external guardrails reduce some failures while introducing brittle blocking and weak safe helpfulness. These findings show that medical safety cannot be inferred from general alignment or medical capability alone, highlighting the need for domain-specific stress testing before deploying LLMs in safety-critical medical applications.
