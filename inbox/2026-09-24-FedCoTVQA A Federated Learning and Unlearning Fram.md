---
title: "FedCoT-VQA: A Federated Learning and Unlearning Framework for Chain-of-Thought Planners in VideoQA"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2609.26814
priority: low
status: unread
interest: medium
next_step: skim
---
# FedCoT-VQA: A Federated Learning and Unlearning Framework for Chain-of-Thought Planners in VideoQA
> 原文: [https://arxiv.org/abs/2609.26814](https://arxiv.org/abs/2609.26814)

arXiv:2609.26814v1 Announce Type: new
Abstract: Chain-of-Thought (CoT) planners have emerged as an effective design for VideoQA, where a lightweight planner first generates intermediate reasoning steps to guide temporal evidence selection before answer prediction. This modularity makes CoT-based VideoQA attractive for federated learning, since only the planner side needs collaborative adaptation while the heavy vision-language backbone can remain fixed. However, in decentralized settings, the planner must not only be trained efficiently across heterogeneous clients but also support later client deletion requests. This is challenging because deleted-client influence is reflected both in model parameters and the planner's reasoning-trace behavior. We present FedCoT-VQA, a federated learning and unlearning framework for CoT planners in VideoQA. FedCoT-VQA consists of three modules: planner-side partitioning (PSP), which exposes a compact shared-residual adaptation space for efficient federated training; server-side aggregation (SSA), which aggregates planner-side updates while maintaining a deletion-ready contribution log; and a residual unlearning module (RUM), which approximates the retained-only counterfactual planner through retained-client replay and selective residual correction, without full retraining. We evaluate FedCoT-VQA in terms of federated training utility, federated unlearning utility, forgetting quality, and efficiency. Results show that compared to current federated approaches, FedCoT-VQA preserves strong federated training utility, improving grounding quality by up to 4.45%. After unlearning, it retains high accuracy and achieves a counterfactual gap of only 7.38%.
