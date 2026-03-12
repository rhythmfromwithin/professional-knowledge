---
interest: medium
link: https://arxiv.org/abs/2603.08812
next_step: skim
priority: medium
slack_ts: '1773283556.262849'
source: cs.CV - Computer Vision
status: unread
title: 'VisionCreator-R1: A Reflection-Enhanced Native Visual-Generation Agentic Model'
---
# VisionCreator-R1: A Reflection-Enhanced Native Visual-Generation Agentic Model
> 原文: [https://arxiv.org/abs/2603.08812](https://arxiv.org/abs/2603.08812)

arXiv:2603.08812v1 Announce Type: new
Abstract: Visual content generation has advanced from single-image to multi-image workflows, yet existing agents remain largely plan-driven and lack systematic reflection mechanisms to correct mid-trajectory visual errors. To address this limitation, we propose VisionCreator-R1, a native visual generation agent with explicit reflection, together with a Reflection-Plan Co-Optimization (RPCO) training methodology. Through extensive experiments and trajectory-level analysis, we uncover reflection-plan optimization asymmetry in reinforcement learning (RL): planning can be reliably optimized via plan rewards, while reflection learning is hindered by noisy credit assignment. Guided by this insight, our RPCO first trains on the self-constructed VCR-SFT dataset with reflection-strong single-image trajectories and planning-strong multi-image trajectories, then co-optimization on VCR-RL dataset via RL. This yields our unified VisionCreator-R1 agent, which consistently outperforms Gemini2.5Pro on existing benchmarks and our VCR-bench covering single-image and multi-image tasks.
