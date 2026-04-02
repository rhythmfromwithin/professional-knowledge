---
interest: medium
link: https://arxiv.org/abs/2603.26469
next_step: skim
priority: medium
slack_ts: '1775098517.278459'
source: cs.DC - Distributed Computing
status: unread
title: 'UNIFERENCE: A Discrete Event Simulation Framework for Developing Distributed
  AI Models'
---
# UNIFERENCE: A Discrete Event Simulation Framework for Developing Distributed AI Models
> 原文: [https://arxiv.org/abs/2603.26469](https://arxiv.org/abs/2603.26469)

arXiv:2603.26469v1 Announce Type: new
Abstract: Developing and evaluating distributed inference algorithms remains difficult due to the lack of standardized tools for modeling heterogeneous devices and networks. Existing studies often rely on ad-hoc testbeds or proprietary infrastructure, making results hard to reproduce and limiting exploration of hypothetical hardware or network configurations. We present UNIFERENCE, a discrete-event simulation (DES) framework designed for developing, benchmarking, and deploying distributed AI models within a unified environment. UNIFERENCE models device and network behavior through lightweight logical processes that synchronize only on communication primitives, eliminating rollbacks while preserving the causal order. It integrates seamlessly with PyTorch Distributed, enabling the same codebase to transition from simulation to real deployment. Our evaluation demonstrates that UNIFERENCE profiles runtime with up to 98.6% accuracy compared to real physical deployments across diverse backends and hardware setups. By bridging simulation and deployment, UNIFERENCE provides an accessible, reproducible platform for studying distributed inference algorithms and exploring future system designs, from high-performance clusters to edge-scale devices. The framework is open-sourced at https://github.com/Dogacel/Uniference.
