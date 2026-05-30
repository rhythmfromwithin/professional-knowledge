---
interest: medium
link: https://arxiv.org/abs/2605.27601
next_step: skim
priority: medium
slack_ts: '1780113870.274259'
source: cs.DC - Distributed Computing
status: unread
title: A Methodology to Assess Power Modeling in Energy-Aware Federated Learning on
  Heterogeneous Mobile Devices
---
# A Methodology to Assess Power Modeling in Energy-Aware Federated Learning on Heterogeneous Mobile Devices
> 原文: [https://arxiv.org/abs/2605.27601](https://arxiv.org/abs/2605.27601)

arXiv:2605.27601v1 Announce Type: new
Abstract: Estimating CPU power on heterogeneous ARM-based commodity devices is challenging due to limited access to CPU's voltage domains. As a result, state-of-the-art energy-aware Federated Learning (FL) frameworks typically rely on simplified approximate power models to estimate computation energy, rather than the more accurate analytical CMOS-based model. To bridge this gap, we propose a reproducible CPU power estimation methodology combined with a rail-to-cluster mapping technique to retrieve cluster-level supply voltage. We evaluate our approach on two commodity Android devices and show that the analytical model predicts CPU power with errors below 10%, whereas the approximate model incurs errors of up to 959%. Using AnycostFL, a state-of-the-art energy-aware FL framework, we show that the analytical model achieves the same 80% model accuracy while consuming 1.4x less energy than the approximate model. These results highlight that approximate models can severely misestimate computation energy and lead to suboptimal decisions. This work facilitates the use of analytical CPU power models on heterogeneous multi-cluster ARM-based mobile SoCs without additional hardware support or external power measurement tools.
