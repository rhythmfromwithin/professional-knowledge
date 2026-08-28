---
interest: medium
link: https://arxiv.org/abs/2608.23568
next_step: skim
priority: high
slack_ts: '1787914968.232699'
source: cs.AI - Artificial Intelligence
status: unread
title: 'RENDER: Controlling Reader-Facing Evidence in LLM Memory Evaluation'
---
# RENDER: Controlling Reader-Facing Evidence in LLM Memory Evaluation
> 原文: [https://arxiv.org/abs/2608.23568](https://arxiv.org/abs/2608.23568)

arXiv:2608.23568v1 Announce Type: new
Abstract: Memory and RAG evaluations often treat the answering model's input as an implementation detail, even though systems may render the same history as a memory entry, summary, typed record, or raw excerpt. We introduce RENDER, a benchmark control that fixes the conversation while varying the reader-facing artifact. RENDER combines a five-level packet ladder, localizing when answer-bearing content enters the input, with deterministic templates approximating ChatGPT-style entries, LangChain summaries, MemGPT-style typed records, and raw conversation. On 500 LongMemEval questions and nine models, matched-budget resolved packets beat recency-truncated raw dialogue by 42.4-72.6 points. In deployed-style templates, best-worst spread is 24.6-48.8 points per model; under the primary scorer, ChatGPT-style entries have higher point estimates than raw conversation on 7 of 9 models. Judge rescoring preserves the positive aggregate effect, but model-specific significance is mixed. Three models scoring 0 percent on formal ledger packets answer the same facts from natural-language entries at 45.4-53.4 percent. The effect persists under retrieval noise and transfers to HotpotQA, suggesting that memory/RAG evaluations should report or control the reader-facing artifact.
