---
interest: medium
link: https://arxiv.org/abs/2605.00043
next_step: skim
priority: low
slack_ts: '1777952334.648539'
source: cs.DB - Databases
status: unread
title: 'SiriusHelper: An LLM Agent-Based Operations Assistant for Big Data Platforms'
---
# SiriusHelper: An LLM Agent-Based Operations Assistant for Big Data Platforms
> 原文: [https://arxiv.org/abs/2605.00043](https://arxiv.org/abs/2605.00043)

arXiv:2605.00043v1 Announce Type: new
Abstract: Big data platforms are widely used in modern enterprises, and an in-production intelligent assistant is increasingly important to help users quickly find actionable guidance and reduce operational burden. While recent LLM+RAG assistants provide a natural interface, they face practical challenges in real deployments: limited scenario coverage across both general consultation and domain-specific troubleshooting workflows, inefficient knowledge access due to inadequate multi-hop retrieval and flat knowledge organization, and high maintenance cost because escalated tickets are unstructured and hard to convert into assistant improvements and reusable SOPs.
In this paper, we present SiriusHelper, a deployed intelligent assistant for big data platforms. SiriusHelper serves as a unified online assistant that automatically identifies user intent and routes queries to the right handling path, including dedicated expert workflows for specialized scenarios (e.g., SQL execution diagnosis). To support complex troubleshooting, SiriusHelper combines a DeepSearch-driven mechanism with a priority-based hierarchical knowledge base to enable multi-hop retrieval without context overload, thus improving answer reliability and latency. To reduce expert overhead, SiriusHelper further introduces automated ticket understanding and SOP distillation: it diagnoses the assistant failure reason (e.g., missing knowledge or wrong routing) and extracts domain-specific SOPs to continuously enrich the knowledge base. Experiments and online deployment on Tencent Big Data platform show that SiriusHelper outperforms representative alternatives and reduces online ticket volume by 20.8\%.
