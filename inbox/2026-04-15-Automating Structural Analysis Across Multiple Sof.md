---
interest: medium
link: https://arxiv.org/abs/2604.09866
next_step: skim
priority: low
slack_ts: '1776223659.057249'
source: cs.SE - Software Engineering
status: unread
title: Automating Structural Analysis Across Multiple Software Platforms Using Large
  Language Models
---
# Automating Structural Analysis Across Multiple Software Platforms Using Large Language Models
> 原文: [https://arxiv.org/abs/2604.09866](https://arxiv.org/abs/2604.09866)

arXiv:2604.09866v1 Announce Type: new
Abstract: Recent advances in large language models (LLMs) have shown the promise to significantly accelerate the workflow by automating structural modeling and analysis. However, existing studies primarily focus on enabling LLMs to operate a single structural analysis software platform. In practice, structural engineers often rely on multiple finite element analysis (FEA) tools, such as ETABS, SAP2000, and OpenSees, depending on project needs, user preferences, and company constraints. This limitation restricts the practical deployment of LLM-assisted engineering workflows. To address this gap, this study develops LLMs capable of automating frame structural analysis across multiple software platforms. The LLMs adopt a two-stage multi-agent architecture. In Stage 1, a cohort of agents collaboratively interpret user input and perform structured reasoning to infer geometric, material, boundary, and load information required for finite element modeling. The outputs of these agents are compiled into a unified JSON representation. In Stage 2, code translation agents operate in parallel to convert the JSON file into executable scripts across multiple structural analysis platforms. Each agent is prompted with the syntax rules and modeling workflows of its target software. The LLMs are evaluated using 20 representative frame problems across three widely used platforms: ETABS, SAP2000, and OpenSees. Results from ten repeated trials demonstrate consistently reliable performance, achieving accuracy exceeding 90% across all cases.
