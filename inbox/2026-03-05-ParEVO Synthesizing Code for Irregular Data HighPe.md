---
title: "ParEVO: Synthesizing Code for Irregular Data: High-Performance Parallelism through Agentic Evolution"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2603.02510
priority: low
status: unread
interest: medium
next_step: skim
---
# ParEVO: Synthesizing Code for Irregular Data: High-Performance Parallelism through Agentic Evolution
> 原文: [https://arxiv.org/abs/2603.02510](https://arxiv.org/abs/2603.02510)

arXiv:2603.02510v1 Announce Type: cross
Abstract: The transition from sequential to parallel computing is essential for modern high-performance applications but is hindered by the steep learning curve of concurrent programming. This challenge is magnified for irregular data structures (such as sparse graphs, unbalanced trees, and non-uniform meshes) where static scheduling fails and data dependencies are unpredictable. Current Large Language Models (LLMs) often fail catastrophically on these tasks, generating code plagued by subtle race conditions, deadlocks, and sub-optimal scaling.
We bridge this gap with ParEVO, a framework designed to synthesize high-performance parallel algorithms for irregular data. Our contributions include: (1) The Parlay-Instruct Corpus, a curated dataset of 13,820 tasks synthesized via a "Critic-Refine" pipeline that explicitly filters for empirically performant algorithms that effectively utilize Work-Span parallel primitives; (2) specialized DeepSeek, Qwen, and Gemini models fine-tuned to align probabilistic generation with the rigorous semantics of the ParlayLib library; and (3) an Evolutionary Coding Agent (ECA) that improves the "last mile" of correctness by iteratively repairing code using feedback from compilers, dynamic race detectors, and performance profilers.
On the ParEval benchmark, ParEVO achieves an average 106x speedup (with a maximum of 1103x) across the suite, and a robust 13.6x speedup specifically on complex irregular graph problems, outperforming state-of-the-art commercial models. Furthermore, our evolutionary approach matches state-of-the-art expert human baselines, achieving up to a 4.1x speedup on specific highly-irregular kernels. Source code and datasets are available at https://github.com/WildAlg/ParEVO.
