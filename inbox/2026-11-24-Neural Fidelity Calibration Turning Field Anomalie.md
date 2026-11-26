---
interest: medium
link: https://arxiv.org/abs/2611.28260
next_step: skim
priority: medium
slack_ts: '1795679634.803949'
source: cs.RO - Robotics
status: unread
title: 'Neural Fidelity Calibration: Turning Field Anomalies into Simulation Fine-Tuning'
---
# Neural Fidelity Calibration: Turning Field Anomalies into Simulation Fine-Tuning
> 原文: [https://arxiv.org/abs/2611.28260](https://arxiv.org/abs/2611.28260)

arXiv:2611.28260v1 Announce Type: new
Abstract: A policy that transfers from simulation to a lab robot often fails in the field. Calibrating a simulator from real-world data typically targets only a few hand-picked parameters, and even calibrated simulators fail to capture unmodeled dynamics, while environments reconstructed via onboard perception inherit sensing noise and artifacts. We propose Neural Fidelity Calibration (NFC), a framework based on conditional flow matching that infers online, directly from a robot's execution data, both simulator physical parameters and residual fidelity - the remaining dynamics discrepancy and the gap between perceived and true environment geometry. A simulation-trained anomaly detector determines when recalibration or fine-tuning is required using onboard sensory signals alone, while an exploration policy actively modulates posterior uncertainty using optimism in the face of uncertainty. Across five robot platforms with up to 39 calibrated parameters and a 128x128 residual terrain map, NFC achieves the most accurate posterior distributions compared to established simulation-based inference baselines. In physical outdoor experiments with a wheeled robot suffering an axle failure across snow, mud, and wet grass, NFC increases rough-terrain navigation success from 26% to 70% while reducing orientation jerk by 88%.
