---
interest: medium
link: https://arxiv.org/abs/2606.24889
next_step: skim
priority: high
slack_ts: '1782360761.405699'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Graph-Based Phonetic Error Correction of Noisy ASR
---
# Graph-Based Phonetic Error Correction of Noisy ASR
> 原文: [https://arxiv.org/abs/2606.24889](https://arxiv.org/abs/2606.24889)

arXiv:2606.24889v1 Announce Type: new
Abstract: Automatic speech recognition (ASR) systems, despite low overall word error rates, produce residual lexical errors that disproportionately affect semantically critical tokens such as named entities, negations, and sentiment-bearing words. These errors are often structured, arising from phonetic similarity rather than random noise, making naive token-level correction insufficient. We propose a structured ASR correction framework, that we call G-SPIN, that combines phonetic graph modeling with contextual language understanding. A graph neural network (GNN) first constructs acoustically plausible candidate neighborhoods for flagged tokens, explicitly restricting the correction search space to phonetic alternatives. A masked language model (MLM) then provides local contextual scoring, and an instruction-tuned large language model (LLM) performs final context-aware re-ranking over this compact candidate set. By decoupling structured phonetic reasoning from contextual semantic selection, our method avoids unconstrained generation while improving correction accuracy. The framework is lightweight, modular, and operates entirely at inference time.
