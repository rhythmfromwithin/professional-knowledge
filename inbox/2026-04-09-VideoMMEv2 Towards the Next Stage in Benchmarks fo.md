---
title: "Video-MME-v2: Towards the Next Stage in Benchmarks for Comprehensive Video Understanding"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2604.05015
priority: medium
status: unread
interest: medium
next_step: skim
---
# Video-MME-v2: Towards the Next Stage in Benchmarks for Comprehensive Video Understanding
> 原文: [https://arxiv.org/abs/2604.05015](https://arxiv.org/abs/2604.05015)

arXiv:2604.05015v1 Announce Type: new
Abstract: With the rapid advancement of video understanding, existing benchmarks are becoming increasingly saturated, exposing a critical discrepancy between inflated leaderboard scores and real-world model capabilities. To address this widening gap, we introduce Video-MME-v2, a comprehensive benchmark designed to rigorously evaluate the robustness and faithfulness of video understanding. To systematically evaluate model capabilities, we design a \textbf{progressive tri-level hierarchy} that incrementally increases the complexity of video comprehension, ranging from multi-point visual information aggregation, to temporal dynamics modeling, and ultimately to complex multimodal reasoning. Besides, in contrast to conventional per-question accuracy, we propose a \textbf{group-based non-linear evaluation} strategy that enforces both consistency across related queries and coherence in multi-step reasoning. It penalizes fragmented or guess-based correctness and assigns credit only to answers supported by valid reasoning. To guarantee data quality, Video-MME-v2 is constructed through a rigorously controlled human annotation pipeline, involving 12 annotators and 50 independent reviewers. Backed by \textbf{3,300 human-hours} and up to \textbf{5 rounds} of quality assurance, Video-MME-v2 aims to serve as one of the most authoritative video benchmarks. Extensive experiments reveal a substantial gap between current best model Gemini-3-Pro and human experts, and uncover a clear hierarchical bottleneck where errors in visual information aggregation and temporal modeling propagate to limit high-level reasoning. We further find that thinking-based reasoning is highly dependent on textual cues, improving performance with subtitles but sometimes degrading it in purely visual settings. By exposing these limitations, Video-MME-v2 establishes a demanding new testbed for the development of next-generation video MLLMs.
