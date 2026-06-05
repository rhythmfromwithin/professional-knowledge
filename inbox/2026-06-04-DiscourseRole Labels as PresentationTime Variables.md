---
interest: medium
link: https://arxiv.org/abs/2606.04109
next_step: skim
priority: high
slack_ts: '1780633552.951439'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Discourse-Role Labels as Presentation-Time Variables for Context Use in Language
  Models
---
# Discourse-Role Labels as Presentation-Time Variables for Context Use in Language Models
> 原文: [https://arxiv.org/abs/2606.04109](https://arxiv.org/abs/2606.04109)

arXiv:2606.04109v1 Announce Type: new
Abstract: Context-augmented language model systems often wrap supplied content with labels such as Reference:, Evidence:, Instruction:, Note:, or Example:, but the effect of these labels on reader-model behavior remains underexplored. We introduce a paired fixed-content probe over 500 MMLU-Pro items: each item receives the same misleading answer-bearing assertion under different discourse-role labels, and adoption is measured by whether the model outputs the injected wrong option. Across GPT-5.5, DeepSeek V4 Pro, Llama-3-8B-Instruct, and Qwen2.5-7B-Instruct, Misleading Adoption Rate shifts by 56-84 percentage points. Binding or source-like labels such as Instruction: and Reference: produce high adoption, whereas Example: consistently suppresses it. Paired tests, bootstrap intervals, final-instruction ablations, and Qwen final-step log-probability probes support a label-conditioned candidate preference. Boundary probes show where the effect weakens or persists: arithmetic tasks reduce adoption, passage-shaped external context preserves smaller label gaps, short-answer evaluation rules out option-letter copying, and nested-label conflicts suggest that illustrative framing can delimit adoption scope. A 200-case single-author manual audit confirms that the short-answer contrasts are stable under conservative adjudication. The resulting claim is bounded but practical: context-utilization and reader-side RAG benchmarks should report and control wrapper labels, because presentation choices can change measured reliance on supplied context.
