---
interest: medium
link: https://arxiv.org/abs/2607.13038
next_step: skim
priority: medium
slack_ts: '1784344399.549809'
source: cs.CY - Computers and Society
status: unread
title: Designing Safety-Constrained LLM Systems for Public Health Information Access
---
# Designing Safety-Constrained LLM Systems for Public Health Information Access
> 原文: [https://arxiv.org/abs/2607.13038](https://arxiv.org/abs/2607.13038)

arXiv:2607.13038v1 Announce Type: new
Abstract: We present the design and implementation of a safety constrained large language model (LLM) system for public health information access, focusing on maternal and child health (MCH) resource navigation. While LLM based systems offer flexible and natural interfaces for information retrieval, their deployment in healthcare contexts introduces risks related to safety, trust, and uncontrolled generation. This work explores practical design patterns for constraining LLM behavior in safety critical environments. We introduce a multi-layered architecture that integrates domain-restricted retrieval augmented generation (RAG), strict boundary enforcement to prevent medical advice, anonymous multiuser session management, and comprehensive audit logging for monitoring and compliance. A key aspect of the design is a controlled data pipeline that grounds all responses in curated public health resources, avoiding reliance on the model pretrained medical knowledge. We implement the system in a real world public health setting and conduct scenario-based validation across in scope, out of scope, and emergency queries. Results show consistent enforcement of safety constraints, reliable resource grounding, and stable system performance, with an average response time of 5.3 seconds. Beyond the specific application, we discuss design trade offs and lessons learned in balancing safety, usability, and system flexibility. Our findings provide practical guidance for deploying LLM based systems in healthcare and other domains where strict information boundaries and accountability are required.
