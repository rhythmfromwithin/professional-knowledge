---
title: "iScript: A Domain-Adapted Large Language Model and Benchmark for Physical Design Tcl Script Generation"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.04476
priority: low
status: unread
interest: medium
next_step: skim
---
# iScript: A Domain-Adapted Large Language Model and Benchmark for Physical Design Tcl Script Generation
> 原文: [https://arxiv.org/abs/2603.04476](https://arxiv.org/abs/2603.04476)

arXiv:2603.04476v1 Announce Type: new
Abstract: Modern EDA flows rely heavily on Tcl scripting, yet general LLMs perform poorly in this domain due to extreme data scarcity, domain-specific semantics, and the high reliability required in physical design. We present iScript, a domain-adapted Qwen3-8B model for Innovus Tcl script generation, and iScript-Bench, a comprehensive benchmark covering five task categories and three difficulty levels. To overcome the lack of training data, we introduce a multi-stage data synthesis pipeline that integrates command extraction, static linting, requirement back-inference, and Chain-of-Thought generation, producing a 10K-tuple (requirement, CoT, script) dataset. iScript is trained through a two-stage strategy combining domain-adaptive pretraining and supervised fine-tuning. To evaluate script correctness efficiently, we further propose a two-step verification framework consisting of static syntax verification and LLM-based functional evaluation. On our benchmark, iScript shows higher pass@k scores than currently state-of-the-art LLMs on average. These results demonstrate the effectiveness of domain adaptation and data synthesis for EDA scripting tasks.
