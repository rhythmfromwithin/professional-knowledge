---
title: "How Language Models Process Negation"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2605.03052
priority: high
status: unread
interest: medium
next_step: skim
---
# How Language Models Process Negation
> 原文: [https://arxiv.org/abs/2605.03052](https://arxiv.org/abs/2605.03052)

arXiv:2605.03052v1 Announce Type: new
Abstract: We study how Large Language Models (LLMs) process negation mechanistically. First, we establish that even though open-weight models often provide wrong answers to questions involving negation, they do possess internal components that process negation correctly. Their poor accuracy is due to late-layer attention behavior that promotes simple shortcuts; ablating those attention modules greatly improves accuracy on negation-related questions. Second, we uncover how models process negation. We consider two hypotheses: models could use attention heads that attend to the phrase being negated and suppress related concepts, or they could directly construct a representation of the entire negative phrase (e.g., representing "not gas" as a vector that promotes liquids and solids). We apply a range of observational and causal interpretability techniques on Mistral-7B and Llama-3.1-8B to show that models implement both mechanisms, with the "constructive" mechanism being more prominent. Combined, our work deepens the understanding of LLMs' internals, highlighting construction-dominant computations and the coexistence of competing mechanisms within LLMs.
