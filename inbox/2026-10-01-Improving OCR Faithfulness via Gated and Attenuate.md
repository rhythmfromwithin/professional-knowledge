---
interest: medium
link: https://arxiv.org/abs/2609.38282
next_step: skim
priority: high
slack_ts: '1791003463.198709'
source: cs.AI - Artificial Intelligence
status: unread
title: Improving OCR Faithfulness via Gated and Attenuated On-Policy Distillation
---
# Improving OCR Faithfulness via Gated and Attenuated On-Policy Distillation
> 原文: [https://arxiv.org/abs/2609.38282](https://arxiv.org/abs/2609.38282)

arXiv:2609.38282v1 Announce Type: new
Abstract: Vision-language models may rewrite anomalous text in images into linguistically plausible expressions, compromising OCR transcription faithfulness. Sequence-level task rewards and local teacher guidance are complementary, but guidance from the same teacher may not remain equally effective as the student improves. Offline analysis shows that supervision from a fixed teacher becomes progressively less favorable as the student improves, both across training checkpoints and across response groups with different task rewards. Motivated by this observation, we introduce GAD-RL, which adaptively regulates teacher supervision during joint post-training according to the student's current task performance and local distributions. A frozen teacher conditions on reference transcriptions and student-generated prefixes. GAD-RL disables distillation for response groups containing an output with task reward at least 0.95 and continuously attenuates distillation strength as group-mean reward increases. It also weights forward KL by the student's probability of the teacher's Top-1 token, moderating local auxiliary updates when student support for that candidate is low. On Qwen3.5-2B, GAD-RL achieves 59.92% Micro Recall on CHAOS-Bench, surpassing GRPO and GRPO+OPD (fixed-weight) by 8.45 and 4.43 percentage points, respectively, while achieving an Overall score of 91.18 on OmniDocBench v1.6.
