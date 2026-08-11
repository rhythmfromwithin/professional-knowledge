---
interest: medium
link: https://arxiv.org/abs/2608.06396
next_step: skim
priority: high
slack_ts: '1786414366.810799'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'TEXAS: Task-Expert-Aware Supervision for Downstream Mixture-of-Experts LLM
  Adaptation'
---
# TEXAS: Task-Expert-Aware Supervision for Downstream Mixture-of-Experts LLM Adaptation
> 原文: [https://arxiv.org/abs/2608.06396](https://arxiv.org/abs/2608.06396)

arXiv:2608.06396v1 Announce Type: new
Abstract: Mixture-of-Experts (MoE) language models route each token through a small subset of experts, making routing patterns useful for identifying task-relevant experts during downstream adaptation. Yet current approaches have two limitations: task experts are typically identified from aggregate routing statistics that reflect usage rather than association with successful task completion, and task-expert activations remain underexplored as signals for supervision allocation. We introduce Task-Expert-Aware Supervision (TEXAS), which combines correctness-conditioned task expert discovery with token-level supervision allocation. TEXAS compares expert activations on instances that the base model solves successfully and those it fails to solve, and retains experts more strongly activated on successful instances. During fine-tuning, it upweights answer tokens in failed instances when they activate these experts. TEXAS therefore leverages existing routing behavior without restricting adaptation to a fixed expert subset or imposing an explicit target routing distribution. Across three MoE models and six benchmarks, TEXAS achieves the best or tied-best performance in 17 of 18 settings and improves over the strongest baseline by 1.3--1.5 points on average. Ablations and further analyses validate both the discovered experts and the resulting supervision strategy.
