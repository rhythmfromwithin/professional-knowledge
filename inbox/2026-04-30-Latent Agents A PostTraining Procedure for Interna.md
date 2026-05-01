---
interest: medium
link: https://arxiv.org/abs/2604.24881
next_step: skim
priority: high
slack_ts: '1777608126.009449'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Latent Agents: A Post-Training Procedure for Internalized Multi-Agent Debate'
---
# Latent Agents: A Post-Training Procedure for Internalized Multi-Agent Debate
> 原文: [https://arxiv.org/abs/2604.24881](https://arxiv.org/abs/2604.24881)

arXiv:2604.24881v1 Announce Type: new
Abstract: Multi-agent debate has been shown to improve reasoning in large language models (LLMs). However, it is compute-intensive, requiring generation of long transcripts before answering questions. To address this inefficiency, we develop a framework that distills multi-agent debate into a single LLM through a two-stage fine-tuning pipeline combining debate structure learning with internalization via dynamic reward scheduling and length clipping. Across multiple models and benchmarks, our internalized models match or exceed explicit multi-agent debate performance using up to 93% fewer tokens. We then investigate the mechanistic basis of this capability through activation steering, finding that internalization creates agent-specific subspaces: interpretable directions in activation space corresponding to different agent perspectives. We further demonstrate a practical application: by instilling malicious agents into the LLM through internalized debate, then applying negative steering to suppress them, we show that distillation makes harmful behaviors easier to localize and control with smaller reductions in general performance compared to steering base models. Our findings offer a new perspective for understanding multi-agent capabilities in distilled models and provide practical guidelines for controlling internalized reasoning behaviors. Code available at https://github.com/johnsk95/latent\_agents
