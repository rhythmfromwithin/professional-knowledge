---
title: "DeepEye: A Steerable Self-driving Data Agent System"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.28889
priority: low
status: unread
interest: medium
next_step: skim
---
# DeepEye: A Steerable Self-driving Data Agent System
> 原文: [https://arxiv.org/abs/2603.28889](https://arxiv.org/abs/2603.28889)

arXiv:2603.28889v1 Announce Type: new
Abstract: Large Language Models (LLMs) have revolutionized natural language interaction with data. The "holy grail" of data analytics is to build autonomous Data Agents that can self-drive complex data analysis workflows. However, current implementations are still limited to linear "ChatBI" systems. These systems struggle with joint analysis across heterogeneous data sources (e.g., databases, documents, and data files) and often encounter "context explosion" in complex and iterative data analysis workflows. To address these challenges, we present DeepEye, a production-ready data agent system that adopts a workflow-centric architecture to ensure scalability and trustworthiness. DeepEye introduces a Unified Multimodal Orchestration protocol, enabling seamless integration of structured and unstructured data sources. To mitigate hallucinations, it employs Hierarchical Reasoning with context isolation, decomposing complex intents into autonomous AgentNodes and deterministic ToolNodes. Furthermore, DeepEye incorporates a database-inspired Workflow Engine (comprising a Compiler, Validator, Optimizer, and Executor) that guarantees structural correctness and accelerates execution via runtime topological optimization. In this demonstration, we showcase DeepEye's ability to orchestrate complex workflows to generate diverse multimodal outputs -- including Data Videos, Dashboards, and Analytical Reports -- highlighting its advantages in transparent execution, automated optimization, and human-in-the-loop reliability.
