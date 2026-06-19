---
interest: medium
link: https://arxiv.org/abs/2606.19364
next_step: skim
priority: high
slack_ts: '1781847257.943239'
source: cs.LG - Machine Learning
status: unread
title: 'Closing the Social-Semantic Gap: SPSD for Edge-Based Prompt Compression in
  Cloud LLM Inference'
---
# Closing the Social-Semantic Gap: SPSD for Edge-Based Prompt Compression in Cloud LLM Inference
> 原文: [https://arxiv.org/abs/2606.19364](https://arxiv.org/abs/2606.19364)

arXiv:2606.19364v1 Announce Type: new
Abstract: The prefill stage of Large Language Model (LLM) inference is a growing contributor to cloud-scale energy cost. Many consumer-support and conversational prompts contain social scaffolding: politeness markers, apologetic preamble, repetition, and rapport-building language that is important for human communication but carries low marginal information for machine reasoning. We call this discrepancy the Social-Semantic Gap. We present SPSD (Sentiment Preserving Semantic Distillation), an edge-based pipeline that compresses user prompts using a 4-bit quantised Small Language Model before transmission to a cloud-deployed LLM. Evaluation on a 248-prompt corpus using Gemma-2-2B-Instruct (Q4\_K\_M) as the SLM and Llama-3.1-8B-Instruct as the cloud evaluation model yields a mean input token saving of 99.9 tokens per distilled call, with all 146 distilled calls yielding positive savings. Response quality, assessed by blind LLM-as-judge scoring across 121 pairs, is non-inferior to the raw path within a pre-specified 1-point margin on a 15-point rubric; the judge awarded 43 percent ties, 28 percent distilled wins, and 29 percent raw wins. Cosine similarity is mixed: mean 0.682, median 0.712, with 54.1 percent of pairs above the 0.70 reference threshold. Safety-critical domains are conservatively routed to passthrough via rule-based gates. Per-call net energy saving is estimated at 70-270 uWh under stated assumptions. SPSD shows that on-device prompt distillation can reduce cloud LLM input-token cost while preserving response quality within a practical non-inferiority margin.
