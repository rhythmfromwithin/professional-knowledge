---
title: "An End-to-End Framework for Building Large Language Models for Software Operations"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.02906
priority: high
status: unread
interest: medium
next_step: skim
---
# An End-to-End Framework for Building Large Language Models for Software Operations
> 原文: [https://arxiv.org/abs/2605.02906](https://arxiv.org/abs/2605.02906)

arXiv:2605.02906v1 Announce Type: new
Abstract: In the field of software operations, Large Language Models (LLMs) have attracted increasing attention. However, existing research has not yet achieved efficient and effective end-to-end intelligent operations due to low-quality data, fragmented knowledge and insufficient learning. To explore the potential of LLMs in software operations, we propose OpsLLM, a domain-specific LLM that supports both knowledge-based question answering (QA) and root cause analysis (RCA). Moreover, we disclose the detailed workflow for building LLMs specifically in the software operations domain. First, a Human-in-the-Loop mechanism is introduced to curate highquality data from a large collection of operational raw data and construct a fine-tuning dataset. Then, based on the data, supervised fine-tuning is conducted to achieve a base model. Furthermore, we introduce a domain process reward model (DPRM) during the reinforcement learning stage to optimize the accuracy and reliability of the fine-tuned model on RCA tasks. Experimental results on the tasks with diverse difficulties demonstrate that OpsLLMs effectively learns and aligns with the operational domain knowledge infused, outperforming existing open-source and closed-source LLMs in accuracy with improvements of 0.2%~5.7% on QA tasks and 2.7% ~70.3% on RCA tasks, while exhibiting strong transferability. Moreover, we will open-source three versions of OpsLLM with 7B, 14B and 32B parameters, along with a 15K fine-tuning dataset.
