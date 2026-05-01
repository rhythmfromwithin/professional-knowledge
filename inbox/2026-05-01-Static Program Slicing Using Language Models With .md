---
title: "Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2604.26961
priority: low
status: unread
interest: medium
next_step: skim
---
# Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding
> 原文: [https://arxiv.org/abs/2604.26961](https://arxiv.org/abs/2604.26961)

arXiv:2604.26961v1 Announce Type: new
Abstract: Static program slicing is a fundamental software engineering technique for isolating code relevant to specific variables. While recent learning-based approaches using language models (LMs) show promise in automating slice prediction, they suffer from inaccurate dependency modeling and unconstrained generation, where LMs fail to capture precise data flow relations and produce slices containing hallucinated tokens and statements. To address these challenges, we propose Sliceformer, a novel approach that reformulates static program slicing as a sequence-to-sequence task using small language models such as CodeT5+. Sliceformer introduces two key innovations that directly target the identified limitations. First, to improve dependency modeling, we design dataflow-aware pretraining objectives that leverage data flow graphs (DFG) to teach models data dependencies through dataflow-preserving statement permutation and dataflow-aware span corruption. Second, to eliminate hallucination, we develop a constrained decoding mechanism that enforces both lexical and syntactic constraints. We evaluate Sliceformer on Java and Python program slicing benchmarks, demonstrating consistent improvements over state-of-the-art baselines with up to 22% gain in ExactMatch.
