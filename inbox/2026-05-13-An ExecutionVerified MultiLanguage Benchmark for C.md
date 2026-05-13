---
interest: medium
link: https://arxiv.org/abs/2605.11006
next_step: skim
priority: low
slack_ts: '1778644954.566359'
source: cs.SE - Software Engineering
status: unread
title: An Execution-Verified Multi-Language Benchmark for Code Semantic Reasoning
---
# An Execution-Verified Multi-Language Benchmark for Code Semantic Reasoning
> 原文: [https://arxiv.org/abs/2605.11006](https://arxiv.org/abs/2605.11006)

arXiv:2605.11006v1 Announce Type: new
Abstract: Evaluating whether large language models (LLMs) can recover execution-relevant program structure, rather than only produce code that passes tests, remains an open problem. Existing code benchmarks emphasize test-passing outputs, from standalone programming tasks (HumanEval, MBPP, LiveCodeBench) to repository repair (SWE-Bench); this is useful, but offers limited diagnostic signal about which program semantics a model can recover from source. We introduce TraceEval, to our knowledge the first execution-verified, multi-language benchmark for code semantic reasoning: recovering a program's runtime call structure from source code. Unlike prior call-graph benchmarks that rely on static-tool output or hand-annotated ground truth, every positive edge in TraceEval is mechanically witnessed by validation execution, eliminating annotator disagreement and label noise for observed behavior. TraceEval consists of (i) 10,583 real-world programs (2,129 test, 8,454 train) extracted from 1,600+ open-source repositories across Python, JavaScript, and Java via an LLM-assisted harness-generation pipeline with tracer validation; and (ii) a reproducible pipeline that converts any open-source repository into new verified benchmark instances. We evaluate 10 LLMs at zero-shot on the held-out test split. The strongest model, Claude-Opus-4.6, reaches an average F1 of 72.9% across the three languages. To demonstrate the train split's utility as a supervision substrate, we fine-tune the Qwen2.5-Coder family on it: lifts of up to +55.6 F1 bring tuned Qwen2.5-Coder-32B to 71.2%, within 1.7 F1 of zero-shot Claude-Opus-4.6. We release the benchmark, pipeline, baselines, and a datasheet at https://github.com/yikun-li/TraceEva
