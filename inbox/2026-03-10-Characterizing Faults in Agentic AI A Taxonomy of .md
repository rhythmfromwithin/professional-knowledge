---
interest: medium
link: https://arxiv.org/abs/2603.06847
next_step: skim
priority: low
slack_ts: '1773132500.406839'
source: cs.SE - Software Engineering
status: unread
title: 'Characterizing Faults in Agentic AI: A Taxonomy of Types, Symptoms, and Root
  Causes'
---
# Characterizing Faults in Agentic AI: A Taxonomy of Types, Symptoms, and Root Causes
> 原文: [https://arxiv.org/abs/2603.06847](https://arxiv.org/abs/2603.06847)

arXiv:2603.06847v1 Announce Type: new
Abstract: Agentic AI systems combine large language model (LLM) reasoning with external tool invocation and long-horizon task execution. Although these systems are increasingly deployed in practice, their architectural composition introduces reliability challenges that differ from those in traditional software systems and standalone LLM applications. However, there is limited empirical understanding of how faults originate, manifest, and propagate in real-world agentic AI systems. To address this gap, we conduct a large-scale empirical study of faults in agentic AI systems. We collect 13,602 issues and pull requests from 40 open-source agentic AI repositories and apply stratified sampling to select 385 faults for in-depth qualitative analysis. Using grounded theory, we derive taxonomies of fault types, observable symptoms, and root causes. We further apply Apriori-based association rule mining to identify statistically significant relationships among faults, symptoms, and root causes, revealing common fault propagation patterns. Finally, we validate the taxonomy through a developer study with 145 practitioners. Our analysis identifies 37 distinct fault types grouped into 13 higher-level fault categories, along with 13 classes of observable symptoms and 12 categories of root causes. The results show that many failures originate from mismatches between probabilistically generated artifacts and deterministic interface constraints, frequently involving dependency integration, data validation, and runtime environment handling. Association rule mining further reveals recurring propagation pathways across system components, such as token management faults leading to authentication failures and datetime handling defects causing scheduling anomalies. Practitioners rated the taxonomy as representative of real-world failures (mean = 3.97/5), and 83.8% reported that it covered faults they had encountered.
