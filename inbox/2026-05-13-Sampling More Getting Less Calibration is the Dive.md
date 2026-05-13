---
title: "Sampling More, Getting Less: Calibration is the Diversity Bottleneck in LLMs"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2605.11128
priority: high
status: unread
interest: medium
next_step: skim
---
# Sampling More, Getting Less: Calibration is the Diversity Bottleneck in LLMs
> 原文: [https://arxiv.org/abs/2605.11128](https://arxiv.org/abs/2605.11128)

arXiv:2605.11128v1 Announce Type: new
Abstract: Diversity is essential for language-model applications ranging from creative generation to scientific discovery, yet modern LLMs often collapse into a narrow subset of plausible outputs. While prior work has developed benchmarks for measuring this lack of diversity, less is known about how the step-by-step probability distributions at inference time cause the problem. We introduce a validity--diversity framework that attributes diversity collapse to how an LLM allocates probability mass across valid and invalid continuations during decoding. This framework decomposes the bottleneck into two complementary forms of miscalibration. First, order calibration: valid tokens are not reliably ranked above invalid tokens, so rank-based cutoff rules must trade off between recovering valid continuations and admitting invalid ones. Second, shape calibration: probability mass is overly concentrated only on few valid continuations while having a heavy-tail of mixed valid and invalid tokens, so maintaining high validity limits diversity. We formalize both mechanisms and show that local failures compound across decoding steps, producing strong sequence-level losses in diversity. Empirically, we develop controlled diagnostics for probing these bottlenecks, including tasks with exactly known valid sets and oracle cutoff baselines. Across 14 language models spanning multiple families and scales, we find that diversity collapse is not merely a limitation of particular sampling heuristics, but a consequence of order and shape miscalibration in the LLM distribution.
