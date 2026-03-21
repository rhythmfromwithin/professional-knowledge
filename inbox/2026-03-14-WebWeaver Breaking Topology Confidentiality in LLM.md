---
interest: medium
link: https://arxiv.org/abs/2603.11132
next_step: skim
priority: low
slack_ts: '1774060639.196289'
source: cs.CR - Cryptography and Security
status: unread
title: 'WebWeaver: Breaking Topology Confidentiality in LLM Multi-Agent Systems with
  Stealthy Context-Based Inference'
---
# WebWeaver: Breaking Topology Confidentiality in LLM Multi-Agent Systems with Stealthy Context-Based Inference
> 原文: [https://arxiv.org/abs/2603.11132](https://arxiv.org/abs/2603.11132)

arXiv:2603.11132v1 Announce Type: new
Abstract: Communication topology is a critical factor in the utility and safety of LLM-based multi-agent systems (LLM-MAS), making it a high-value intellectual property (IP) whose confidentiality remains insufficiently studied.
%
Existing topology inference attempts rely on impractical assumptions, including control over the administrative agent and direct identity queries via jailbreaks, which are easily defeated by basic keyword-based defenses. As a result, prior analyses fail to capture the real-world threat of such attacks.
%
To bridge this realism gap, we propose \textit{WebWeaver}, an attack framework that infers the complete LLM-MAS topology by compromising only a single arbitrary agent instead of the administrative agent.
%
Unlike prior approaches, WebWeaver relies solely on agent contexts rather than agent IDs, enabling significantly stealthier inference.
%
WebWeaver further introduces a new covert jailbreak-based mechanism and a novel fully jailbreak-free diffusion design to handle cases where jailbreaks fail.
%
Additionally, we address a key challenge in diffusion-based inference by proposing a masking strategy that preserves known topology during diffusion, with theoretical guarantees of correctness.
%
Extensive experiments show that WebWeaver substantially outperforms state-of-the-art (SOTA) baselines, achieving about 60\% higher inference accuracy under active defenses with negligible overhead.
