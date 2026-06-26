---
interest: medium
link: https://arxiv.org/abs/2606.26101
next_step: skim
priority: high
slack_ts: '1782447550.401979'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Know2Guess: A Contamination-Aware Multi-Zone Benchmark for Knowledge-Boundary
  Evaluation in Large Language Models'
---
# Know2Guess: A Contamination-Aware Multi-Zone Benchmark for Knowledge-Boundary Evaluation in Large Language Models
> 原文: [https://arxiv.org/abs/2606.26101](https://arxiv.org/abs/2606.26101)

arXiv:2606.26101v1 Announce Type: new
Abstract: Reliable evaluation of large language models should separate supported answering from unsupported guessing without conflating either with data contamination, prompt idiosyncrasy, or generic refusal behavior. We present a contamination-aware, multi-zone benchmark for measuring the transition from answerable knowledge to abstention-expected unknowns under frozen build-time labels. The benchmark contains 1,200 items across five domains, explicit abstention expectations, contamination-risk metadata, and dual parsing with an official strict parser plus a normalized robustness parser. We evaluate FLAN-T5, Qwen2.5-Instruct, and Llama-3-Instruct models under locked answer-or-abstain prompts, answer-only controls, and prompt-template variants. The benchmark is not solved by generic non-answer behavior: FLAN baselines remain weak on productive abstention, while stronger instruction-tuned models expose a selective but incomplete transition from answering to abstaining. Qwen2.5-3B-Instruct achieves the best overall reliability, but answer-expected zones remain difficult, calibration remains poor, and benign-item refusal persists. Prompt and parser robustness analyses preserve the main ranking and qualitative conclusions. The benchmark therefore provides a reproducible protocol for auditing answerability, abstention, refusal, and contamination as distinct but interacting dimensions of LLM reliability.The dataset is publicly available at https://github.com/renweimeng/Know2Guess-A-Contamination-Aware-Multi-Zone-Benchmark.
