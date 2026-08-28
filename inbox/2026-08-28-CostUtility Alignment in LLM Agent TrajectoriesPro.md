---
interest: medium
link: https://arxiv.org/abs/2608.26195
next_step: skim
priority: low
slack_ts: '1787914974.715779'
source: cs.SE - Software Engineering
status: unread
title: Cost-Utility Alignment in LLM Agent Trajectories:Profiling,Attribution,Diagnosis,Adaptation,and
  Evaluation
---
# Cost-Utility Alignment in LLM Agent Trajectories:Profiling,Attribution,Diagnosis,Adaptation,and Evaluation
> 原文: [https://arxiv.org/abs/2608.26195](https://arxiv.org/abs/2608.26195)

arXiv:2608.26195v1 Announce Type: new
Abstract: LLM agents execute tasks through multi-step trajectories that accumulate cost in tokens, latency, monetary fees, and environmental risk while producing utility only at the aggregate task level. Prior surveys address inference optimization, agent capabilities, or evaluation in isolation, leaving practitioners without principled tools to determine whether a trajectory's resource expenditure is justified by its task contribution. We address this gap by developing a trajectory-centric cost-utility alignment framework that treats resource consumption and task contribution as dual ledgers over the same execution, organized around five analytical stages: cost profiling, utility attribution, misalignment diagnosis, targeted adaptation, and evaluation. Utility attribution is central to this structure: rather than relying on aggregate outcomes, it organizes contribution methods by evidential strength, from process proxies and information dependency to counterfactual replay, supplying the causal evidence that grounds diagnosis and guides adaptation. Using this framework, we analyze recent agent systems, attribution methods, and evaluation protocols covering efficiency, reliability, and economic value, as well as five forms of misalignment spanning cognitive and context use, external interaction, recovery-loop control, resource-capability allocation, and multi-agent coordination, together with their targeted adaptations. The result is a closed analytical loop connecting the cost side of agent execution to its utility side, providing a structured basis for resource-aware agent design and deployment.
