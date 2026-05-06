---
title: "E-MIA: Exam-Style Black-Box Membership Inference Attacks against RAG Systems"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.00955
priority: low
status: unread
interest: medium
next_step: skim
---
# E-MIA: Exam-Style Black-Box Membership Inference Attacks against RAG Systems
> 原文: [https://arxiv.org/abs/2605.00955](https://arxiv.org/abs/2605.00955)

arXiv:2605.00955v1 Announce Type: new
Abstract: Retrieval-Augmented Generation (RAG) equips large language models (LLMs) with external evidence by retrieving documents at inference time, but it also turns the retrieval corpusinto a sensitive asset. Under a black-box setting, an adversary given a candidate document can infer whether it has been ingested into the RAG knowledge base (i.e., document-level membership inference) solely from query response interactions, thereby leaking corpus coverage and the existence of sensitive topics. Existing RAG MIA methods either rely on soft signals such as semantic similarity, which often yield overlapping member/non-member score distributions and unstable thresholds, or employ explicit confirmation probes whose intent is conspicuous and thus prone to refusal and detection. We propose E-MIA, which converts verifiable hard evidence in the target document (e.g., fine-grained details, proper nouns/technical terms, definitional statements, metadata cues, and causal/constraint relations) into an exam with four objectively gradable question types (FB/SC/MC/T/F), and uses the aggregated exam score across multiple evidence targeted questions as the membership signal. Experiments across multiple datasets and diverse RAG configurations demonstrate that E-MIA improves member/non-member separability in stringent settings while preserving natural, stealthy queries, and we further analyze the impact of question composition and exam length on attack effectiveness.
