---
title: "CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2606.04072
priority: medium
status: unread
interest: medium
next_step: skim
---
# CADET: A Modular Platform for Evaluating Distributed Cooperative Autonomy in Connected Autonomous Vehicles
> 原文: [https://arxiv.org/abs/2606.04072](https://arxiv.org/abs/2606.04072)

arXiv:2606.04072v1 Announce Type: new
Abstract: Deep learning models are increasingly central to autonomous vehicle (AV) pipelines, yet their integration has traditionally followed a monolithic design where perception, planning, and control execute on a single onboard computer. This design overlooks the emerging paradigm of cooperative autonomy, where vehicles interact with roadside units (RSUs), edge servers, and cloud-hosted intelligence through vehicle-to-everything (V2X) connectivity. Cooperative perception and control improve safety and efficiency, but also introduce systems-level challenges: network latency, compute heterogeneity, and multi-tenant contention, all critically affect real-time decision-making. These challenges are further amplified by the increasing reliance on large foundation models, whose scale necessitates cloud deployment.
We present CADET (Cooperative Autonomy through Distributed Experimentation Toolkit), a modular platform for systematic and reproducible evaluation of distributed cooperative autonomy systems under realistic deployment conditions. CADET decouples the AV stack into composable modules that can be flexibly deployed across vehicles, infrastructure, and edge/cloud tiers. The framework integrates state-of-the-art models, incorporates trace-driven network and workload emulation, and provides synchronized model-, system-, and task-level instrumentation. Through V2V and V2I experiments, we show that distributed deployment choices fundamentally shape safety, with V2V intent packets outperforming cloud-based perception and RSU-assisted perception sustaining safety until overloaded by concurrent requests. Although designed for AV pipelines, CADET also supports dataset-driven experimentation, enabling systems and ML researchers to benchmark distributed inference workloads independently of full vehicle simulation. CADET is open source, with code and demo available at https://nesl.github.io/cadet-web.
