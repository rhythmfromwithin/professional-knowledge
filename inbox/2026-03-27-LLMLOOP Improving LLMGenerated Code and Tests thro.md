---
title: "LLMLOOP: Improving LLM-Generated Code and Tests through Automated Iterative Feedback Loops"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.23613
priority: low
status: unread
interest: medium
next_step: skim
---
# LLMLOOP: Improving LLM-Generated Code and Tests through Automated Iterative Feedback Loops
> 原文: [https://arxiv.org/abs/2603.23613](https://arxiv.org/abs/2603.23613)

arXiv:2603.23613v1 Announce Type: new
Abstract: Large Language Models (LLMs) are showing remarkable performance in generating source code, yet the generated code often has issues like compilation errors or incorrect code. Researchers and developers often face wasted effort in implementing checks and refining LLM-generated code, frequently duplicating their efforts. This paper presents LLMLOOP, a framework that automates the refinement of both source code and test cases produced by LLMs. LLMLOOP employs five iterative loops: resolving compilation errors, addressing static analysis issues, fixing test case failures, and improving test quality through mutation analysis. These loops ensure the generation of high-quality test cases that serve as both a validation mechanism and a regression test suite for the generated code. We evaluated LLMLOOP on HUMANEVAL-X, a recent benchmark of programming tasks. Results demonstrate the tool's effectiveness in refining LLM-generated outputs.
