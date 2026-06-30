---
interest: medium
link: https://arxiv.org/abs/2606.27483
next_step: skim
priority: high
slack_ts: '1782792823.460489'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Internalizing the Future: A Unified Agentic Training Paradigm for World Model
  Planning'
---
# Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning
> 原文: [https://arxiv.org/abs/2606.27483](https://arxiv.org/abs/2606.27483)

arXiv:2606.27483v1 Announce Type: new
Abstract: Large language model (LLM) agents have demonstrated strong capability in sequential decision-making, yet they remains fundamentally reactive in long-horizon tasks. Unlike humans who employ "what-if" reasoning to evaluate potential plans before commitment, standard agents lack an internal world model to simulate future outcomes. Therefore, we propose to internalize future-aware planning by training a single autoregressive model to verbalize both a prospective state rollout and a plan-conditioned success estimate-a textual analogue of the Q-value. Crucially, we identify a format-capability gap: simply fine-tuning agents on look-ahead traces during post-training leads to superficial mimicry of foresight without genuine predictive grounding. To bridge this gap, we introduce a three-stage training paradigm: (i) World Model Agentic Mid-Training (WM-AMT) to inject latent predictive capabilities into the policy; (ii) Format-Eliciting SFT (FE-SFT) to structure this injected capability; and (iii) Foresight-Conditioned Reinforcement Learning (FC-RL) to refine the calibration and utility of the generated simulations. Evaluated on search and mathematical reasoning tasks, our approach consistently outperforms other training baselines. Our results demonstrate that effective internal world modeling in LLM agents requires a capability-first training pipeline to achieve grounded and calibrated foresight.
