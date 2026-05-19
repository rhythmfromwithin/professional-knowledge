---
interest: medium
link: https://arxiv.org/abs/2605.16299
next_step: skim
priority: low
slack_ts: '1779164082.707349'
source: cs.SE - Software Engineering
status: unread
title: 'ACE: Self-Evolving LLM Coding Framework via Adversarial Unit Test Generation
  and Preference Optimization'
---
# ACE: Self-Evolving LLM Coding Framework via Adversarial Unit Test Generation and Preference Optimization
> 原文: [https://arxiv.org/abs/2605.16299](https://arxiv.org/abs/2605.16299)

arXiv:2605.16299v1 Announce Type: new
Abstract: Large Language Models (LLMs) excel at code generation but remain heavily reliant on large-scale annotated solutions and verification-based supervision, which constrains scalability and hinders sustained self-improvement. Recent solver--verifier frameworks exploit program execution as an automatic supervision signal, but their effectiveness degrades as solvers become moderately strong: verifier-generated tests increasingly confirm semantic correctness rather than exposing the remaining failure modes. We propose \textbf{ACE}, a self-evolving code generation framework based on a solver--adversary architecture that prioritizes active failure discovery through execution-centric supervision. A single LLM alternates between generating candidate programs and producing adversarial unit test inputs optimized to induce execution-level failures, such as runtime errors, exceptions, or non-termination. Supervision is derived solely from execution outcomes: robust programs are selected for supervised fine-tuning, while adversarial tests are optimized via Kahneman--Tversky Optimization using execution-derived preferences. Notably, the entire training loop requires no ground-truth code or external reward models. Experiments on CodeContests, MBPP, and LiveCodeBench demonstrate that ACE consistently outperforms strong solver--verifier baselines, achieving 3--7\% absolute gains in pass@1, with larger improvements on out-of-distribution benchmarks, while maintaining competitive or improved inference efficiency.
