---
interest: medium
link: https://arxiv.org/abs/2610.20667
next_step: skim
priority: high
slack_ts: '1792123825.995549'
source: cs.AI - Artificial Intelligence
status: unread
title: Evaluating Model Capabilities After Benchmark Saturation
---
# Evaluating Model Capabilities After Benchmark Saturation
> 原文: [https://arxiv.org/abs/2610.20667](https://arxiv.org/abs/2610.20667)

arXiv:2610.20667v1 Announce Type: new
Abstract: Rapid advances in AI capabilities are causing benchmarks to saturate. Once several models approach perfect scores, a benchmark loses its power to differentiate between them, and with it its utility for informing AI safety cases and frontier policies. Yet benchmark items produce far more information than the scores we typically extract from them: a full transcript of how each model solved the task. We investigate whether these transcripts can be used to assess model capabilities even after benchmark scores have saturated. We simulate saturation retrospectively using historical benchmark and model releases, and test whether protocols that access only correctly solved transcripts from saturated benchmarks can predict capabilities measured on held-out, unsaturated items. We evaluate representative contemporary approaches for extracting information from model transcripts: pairwise judging, single-transcript absolute scoring, and predictions from deterministic transcript features or embeddings. We find that saturated transcripts retain capability information beyond benchmark accuracy. Amongst our evaluated protocols, pairwise judging performs best, reducing prediction error by 5.3 times compared to a baseline using only saturated benchmark scores. This capability-relevant information is distributed across transcript sections, but concentrated in specific channels of information such as reasoning and tool-calls. However, the predictive power of protocols does not always generalise across distribution shifts -- for example by underestimating the capabilities of the first reasoning models introduced in early 2025. Saturated benchmarks thus retain capability-predicting signal in their task transcripts, but extending the lifetime of existing benchmarks requires methods designed to extract these signals robustly.
