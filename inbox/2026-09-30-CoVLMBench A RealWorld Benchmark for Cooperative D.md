---
interest: medium
link: https://arxiv.org/abs/2609.35823
next_step: skim
priority: medium
slack_ts: '1790745142.130409'
source: cs.CV - Computer Vision
status: unread
title: 'CoVLM-Bench: A Real-World Benchmark for Cooperative Driving Question Answering
  and Planning'
---
# CoVLM-Bench: A Real-World Benchmark for Cooperative Driving Question Answering and Planning
> 原文: [https://arxiv.org/abs/2609.35823](https://arxiv.org/abs/2609.35823)

arXiv:2609.35823v1 Announce Type: new
Abstract: Vision-language models (VLMs) have made substantial progress in autonomous driving, but their success has primarily been studied in ego-centric scenes. Infrastructure-side observations provide views beyond the ego vehicle's field of view, yet conventional cooperative-driving systems typically transform them into geometric representations for downstream perception and planning. Directly incorporating these views into VLMs offers an opportunity to improve cooperative scene understanding and trajectory planning. However, question answering and trajectory planning have not been jointly evaluated on the same real-world vehicle-infrastructure scenes. We present CoVLM-Bench, a benchmark for cooperative driving question answering (CDQA) and cooperative planning (CP) on vehicle-infrastructure paired scenes. CoVLM-Bench provides scene-grounded CDQA annotations, three-part rationales as auxiliary supervision, and future trajectory targets derived from recorded ego motion. It contains 2,196 paired frames with 35,136 CDQA annotations, while CP predicts six waypoints over a three-second horizon. The annotations combine model-assisted drafting, record-based computation, and human verification. Built upon CoVLM-Bench, we introduce CoVLM-Drive, a unified VLM baseline that directly uses paired views for both CDQA and CP. Experiments show that CDQA adaptation improves answer accuracy and that CoVLM-Drive reaches a lower FDE than the compared V2X planners; QA initialization and rationale supervision each reduce planning error. Together, CoVLM-Bench and CoVLM-Drive support the training and comparison of VLMs for cooperative scene understanding and planning.
