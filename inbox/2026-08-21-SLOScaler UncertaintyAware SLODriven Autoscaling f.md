---
title: "SLO-Scaler: Uncertainty-Aware SLO-Driven Autoscaling for Microservices"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2608.18390
priority: medium
status: unread
interest: medium
next_step: skim
---
# SLO-Scaler: Uncertainty-Aware SLO-Driven Autoscaling for Microservices
> 原文: [https://arxiv.org/abs/2608.18390](https://arxiv.org/abs/2608.18390)

arXiv:2608.18390v1 Announce Type: new
Abstract: Autoscaling microservice-based applications to satisfy Service Level Objectives (SLOs) remains challenging due to bursty workloads, cascading latency across service dependencies, and cold-start overhead. Existing approaches such as the Kubernetes Horizontal Pod Autoscaler (HPA) rely on threshold-based CPU or memory metrics, which react too slowly to traffic spikes. Recent predictive methods improve responsiveness but generate point forecasts that ignore prediction uncertainty, leading to over-provisioning or oscillatory scaling. We propose SLO-Scaler, an uncertainty-aware autoscaling framework that predicts short-horizon request rates, tail latency, and SLO violation probability using a Bayesian LSTM model. SLO-Scaler integrates confidence-interval-based scaling decisions with a dependency graph analysis module that localizes bottleneck services, avoiding unnecessary whole-chain scaling. We evaluate SLO-Scaler on the DeathStarBench Social Network benchmark deployed on Kubernetes under periodic, bursty, and long-tail traffic patterns. Under bursty traffic, SLO-Scaler reduces the SLO violation rate by 29-56%, lowers the average replica count by 18-33%, and decreases scaling event frequency by 38-59% compared with the baselines, while achieving lower tail latency.
