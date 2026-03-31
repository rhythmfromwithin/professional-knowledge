---
title: "UCAgent: An End-to-End Agent for Block-Level Functional Verification"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.25768
priority: low
status: unread
interest: medium
next_step: skim
---
# UCAgent: An End-to-End Agent for Block-Level Functional Verification
> 原文: [https://arxiv.org/abs/2603.25768](https://arxiv.org/abs/2603.25768)

arXiv:2603.25768v1 Announce Type: new
Abstract: Functional verification remains a critical bottleneck in modern IC development cycles, accounting for approximately 70% of total development time in many projects. However, traditional methods, including constrained-random and formal verification, struggle to keep pace with the growing complexity of modern semiconductor designs.
While recent advances in Large Language Models (LLMs) have shown promise in code generation and task automation, significant challenges hinder the realization of end-to-end functional verification automation. These challenges include (i) limited accuracy in generating Verilog/SystemVerilog verification code, (ii) the fragility of LLMs when executing complex, multi-step verification workflows, and (iii) the difficulty of maintaining verification consistency across specifications, coverage models, and test cases throughout the workflow.
To address these challenges, we propose UCAgent, an end-to-end agent that automates hardware block-level functional verification based on three core mechanisms. First, we establish a pure Python verification environment using Picker and Toffee to avoid relying on LLM-generated SystemVerilog verification code. Second, we introduce a configurable 31-stage fine-grained verification workflow to guide the LLM, where each stage is verified by an automated checker. Furthermore, we propose a Verification Consistency Labeling Mechanism (VCLM) that assigns hierarchical labels to LLM-generated artifacts, improving the reliability and traceability of verification.
Experimental results show that UCAgent can complete end-to-end automated verification on multiple modules, including the UART, FPU, and integer divider modules, achieving up to 98.5% code coverage and up to 100% functional coverage. UCAgent also discovers previously unidentified design defects in realistic designs, demonstrating its practical potential.
