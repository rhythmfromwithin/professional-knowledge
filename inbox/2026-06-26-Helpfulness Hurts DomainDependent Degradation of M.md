---
interest: medium
link: https://arxiv.org/abs/2606.26102
next_step: skim
priority: high
slack_ts: '1782447548.154579'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Helpfulness Hurts: Domain-Dependent Degradation of Mid-Trained Compassion
  Values Under Post-Training'
---
# Helpfulness Hurts: Domain-Dependent Degradation of Mid-Trained Compassion Values Under Post-Training
> 原文: [https://arxiv.org/abs/2606.26102](https://arxiv.org/abs/2606.26102)

arXiv:2606.26102v1 Announce Type: new
Abstract: Standard post-training pipelines apply supervised fine-tuning (SFT) and reinforcement learning (RL) to make language models helpful, but these processes may inadvertently degrade values instilled during pre-training. We investigate whether the domain of post-training data differentially affects the retention of animal compassion values in a Llama 3.1 8B model mid-trained on compassion-oriented synthetic data, using both SFT (helpfulness via Dolly-15k vs. coding via Magicoder-110K) and GRPO (helpfulness via RLHFlow vs. coding via Magicoder), evaluated on the Animal Harm Benchmark (AHB 2.2) and MORU benchmark (Moral Reasoning Under Uncertainty). Helpfulness training significantly degrades animal compassion relative to coding training on AHB (SFT: 35.7% vs. 65.2%; GRPO: 18.7% vs. 32.0%), replicating across two independent helpfulness datasets and two training paradigms. On English MORU items, helpfulness training degrades general moral reasoning by 25.5 percentage points (46.4% vs. 71.9%), a striking gap that rivals the compassion effect in magnitude. However, this effect does not transfer cross-lingually: on the multilingual MORU benchmark, the domain effect disappears (SFT: 52.3% vs. 51.2%). In contrast, the animal compassion effect transfers consistently across languages, with Magicoder's AHB percentage-point gain over the base model 4.5 times larger on non-English items than English items. This divergence suggests that values instilled through mid-training are encoded more deeply and cross-lingually than reasoning improvements from domain-specific post-training. These results suggest that, for labs building on value-laden mid-training, coding-domain post-training may better preserve mid-trained values than helpfulness post-training without harming general reasoning capabilities.
