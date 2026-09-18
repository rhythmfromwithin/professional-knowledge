---
interest: medium
link: https://arxiv.org/abs/2609.19148
next_step: skim
priority: high
slack_ts: '1789705173.850699'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Modality Discrepancy Transformer for Ambivalence and Hesitancy Recognition
---
# Modality Discrepancy Transformer for Ambivalence and Hesitancy Recognition
> 原文: [https://arxiv.org/abs/2609.19148](https://arxiv.org/abs/2609.19148)

arXiv:2609.19148v1 Announce Type: new
Abstract: Ambivalence and hesitancy (A/H) are affective states in which individuals express contradictory signals across facial, vocal, and linguistic channels. Automatically recognising A/H in clinical videos requires detecting cross-modal disagreement -- the signal that standard fusion methods suppress. Based on the conflict-aware multimodal fusion framework of Bekhouche et al., we present the Modality Discrepancy Transformer (MDT). MDT enriches the original 6-token design to a 9-token representation comprising three modality embeddings, three absolute-difference features, and three Hadamard-product discrepancy features learned through linear projections. These nine tokens undergo Transformer self-attention, with FiLM-based text-conditioned modulation and LoRA fine-tuning as core architectural components. A text-guided late fusion branch blends a text-only auxiliary head with the full multimodal output at inference. On the BAH dataset from the 3rd ABAW Challenge, MDT achieves 0.7408 Macro F1 on the labelled test split and 0.7368 on the private leaderboard, outperforming the strongest published baseline by over 10 points while training in under 20 minutes on a single GPU.
