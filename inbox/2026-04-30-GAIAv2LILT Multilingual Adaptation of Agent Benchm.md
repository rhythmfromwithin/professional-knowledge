---
title: "GAIA-v2-LILT: Multilingual Adaptation of Agent Benchmark beyond Translation"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2604.24929
priority: high
status: unread
interest: medium
next_step: skim
---
# GAIA-v2-LILT: Multilingual Adaptation of Agent Benchmark beyond Translation
> 原文: [https://arxiv.org/abs/2604.24929](https://arxiv.org/abs/2604.24929)

arXiv:2604.24929v1 Announce Type: new
Abstract: Agent benchmarks remain largely English-centric, while their multilingual versions are often built with machine translation (MT) and limited post-editing. We argue that, for agentic tasks, this minimal workflow can easily break benchmark validity through query-answer misalignment or culturally off-target context. We propose a refined workflow for adapting English benchmarks into multiple languages with explicit functional alignment, cultural alignment, and difficulty calibration using both automated checks and human review. Using this workflow, we introduce GAIA-v2-LILT, a re-audited multilingual extension of GAIA covering five non-English languages. In experiments, our workflow improves agent success rates by up to 32.7% over minimally translated versions, bringing the closest audited setting to within 3.1% of English performance while substantial gaps remain in many other cases. This indicates that a substantial share of the multilingual performance gap is benchmark-induced measurement error, motivating task-level alignment when adapting English benchmarks across languages. The data is available as part of the MAPS package at https://huggingface.co/datasets/Fujitsu-FRE/MAPS/viewer/GAIA-v2-LILT. We also release the code used in our experiments at https://github.com/lilt/gaia-v2-lilt.
