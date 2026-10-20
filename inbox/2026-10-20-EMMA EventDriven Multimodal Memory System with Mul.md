---
title: "EMMA: Event-Driven Multimodal Memory System with Multi-Agent Retrieval"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.23892
priority: medium
status: unread
interest: medium
next_step: skim
---
# EMMA: Event-Driven Multimodal Memory System with Multi-Agent Retrieval
> 原文: [https://arxiv.org/abs/2610.23892](https://arxiv.org/abs/2610.23892)

arXiv:2610.23892v1 Announce Type: new
Abstract: Long video understanding requires reasoning over hours of content that far exceed the context window of multimodal large language models (MLLMs). Existing approaches compress video into fixed-length clips, yet events are fragmented and unrelated content is merged, yielding noisy retrieval. To overcome this challenge, we propose EMMA, an Event-driven Multimodal Memory system with Multi-Agent retrieval, which organizes memory around semantic events in three stages: (1) Event segmentation: a dual-stream detector adaptively locates event boundaries by fusing visual semantic drift with spoken transitions, rather than fixed windows. (2) Memory construction: built on the detected events, a three-level hierarchy of raw video, clip-level memory, and event-level memory stores content at progressively higher semantic abstraction. (3) Memory retrieval: a multi-agent framework collaboratively queries this hierarchy through query decomposition, tiered search, evidence validation, and answer generation, narrowing evidence from coarse events to precise clips. Extensive experiments on three challenging benchmarks demonstrate substantial improvements, showing the effectiveness of our event-aligned memory system. Code, prompt templates, and reproduction scripts are available at https://github.com/BAI-LAB/EMMA.
