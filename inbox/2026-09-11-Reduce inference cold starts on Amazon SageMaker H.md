---
title: "Reduce inference cold starts on Amazon SageMaker HyperPod with model caching"
source: "AWS Blog"
link: https://aws.amazon.com/blogs/machine-learning/reduce-inference-cold-starts-on-amazon-sagemaker-hyperpod-with-model-caching/
priority: high
status: unread
interest: medium
next_step: skim
---
# Reduce inference cold starts on Amazon SageMaker HyperPod with model caching
> 原文: [https://aws.amazon.com/blogs/machine-learning/reduce-inference-cold-starts-on-amazon-sagemaker-hyperpod-with-model-caching/](https://aws.amazon.com/blogs/machine-learning/reduce-inference-cold-starts-on-amazon-sagemaker-hyperpod-with-model-caching/)

Amazon SageMaker HyperPod now supports model caching for inference, which pre-loads model weights and container images onto cluster nodes so pods read from local NVMe storage instead of downloading over the network. Learn how model caching cuts cold starts from tens of minutes to seconds, how it works, and how to enable it.
