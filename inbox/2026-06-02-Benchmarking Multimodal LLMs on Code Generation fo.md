---
title: "Benchmarking Multimodal LLMs on Code Generation for Complex Interactive Webpages"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2606.00154
priority: low
status: unread
interest: medium
next_step: skim
---
# Benchmarking Multimodal LLMs on Code Generation for Complex Interactive Webpages
> 原文: [https://arxiv.org/abs/2606.00154](https://arxiv.org/abs/2606.00154)

arXiv:2606.00154v1 Announce Type: new
Abstract: Recent advancements in multimodal large language models (MLLMs) have achieved remarkable progress in multimodal reasoning and code generation, catalyzing a new paradigm for front-end development. In particular, these models can directly transform visual designs into executable code, significantly improving the efficiency and adaptability of web development. Modern web applications are dynamic and interactive, featuring frequent user-page interactions. However, existing benchmarks largely evaluate the code generation of static webpages, ignoring the complex interactive behaviors in real-world applications. Besides, their evaluation criteria remain confined to visual fidelity and code structure, overlooking the interaction consistency between the generated and the reference webpages. To address these limitations, we introduce WebIGBench, the first benchmark designed to evaluate code generation for interactive webpages with complex interactions. By combining manually designed interaction paths with UI automation, we collected 103 complex webpages from real-world websites. This benchmark covers 5 popular interactive action types (e.g., click, input) involving 871 distinct interactive actions. Moreover, we propose a novel evaluation pipeline to address the gap in automated assessment of interactive actions. Extensive experiments on several representative MLLMs reveal the performance boundaries of current models in interactive webpage code generation using WebIGBench. The proposed benchmark is available at https://github.com/anoa12159-hue/WebIGBench\_eval.
