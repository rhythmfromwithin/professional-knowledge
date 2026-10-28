---
interest: medium
link: https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/
next_step: skim
priority: high
slack_ts: '1793164456.845609'
source: AWS Blog
status: unread
title: Fleet-wide computer vision lifecycle at the edge with SageMaker SDK v3
---
# Fleet-wide computer vision lifecycle at the edge with SageMaker SDK v3
> 原文: [https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/](https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/)

Fleet-wide computer vision needs a model per camera, not one model for the whole fleet. This post presents a working Amazon SageMaker SDK v3 reference architecture that trains, quality-gates, compiles per-camera models with SageMaker Neo, and versions thousands of them, with an AWS Step Functions layer pacing fleet-scale retraining within account quotas.
