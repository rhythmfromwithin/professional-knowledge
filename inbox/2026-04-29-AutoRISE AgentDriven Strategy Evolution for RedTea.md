---
interest: medium
link: https://arxiv.org/abs/2604.22871
next_step: skim
priority: low
slack_ts: '1777521046.658239'
source: cs.CR - Cryptography and Security
status: unread
title: 'AutoRISE: Agent-Driven Strategy Evolution for Red-Teaming Large Language Models'
---
# AutoRISE: Agent-Driven Strategy Evolution for Red-Teaming Large Language Models
> 原文: [https://arxiv.org/abs/2604.22871](https://arxiv.org/abs/2604.22871)

arXiv:2604.22871v1 Announce Type: new
Abstract: Automated red-teaming methods for large language models typically optimize attack prompts within a fixed, human-designed strategy, leaving the attack strategy itself unchanged. We instead optimize the strategy. We propose AutoRISE, a method that searches over executable attack programs rather than individual prompts. At each iteration, a coding agent edits a strategy and a fixed evaluation harness scores the resulting attacks, returning both a scalar objective and per-example diagnostics that guide subsequent edits. This allows structural changes, including new attack components and altered control flow, that prompt-level methods do not directly express. We also release two benchmark suites developed on disjoint target sets and evaluate on 11 models from five families against seven established jailbreak datasets. Across held-out models, AutoRISE improves average attack success rate by 17.0 points over the strongest baseline, and improves attack success by up to 16 points on frontier targets with low baseline success rates. Ablations against parametric and strategy-library baselines suggest that these gains arise from unrestricted program search, particularly compositional techniques and control-flow edits. AutoRISE operates in a black-box, inference-only setting, requiring no fine-tuning, human annotation, or GPU compute.
