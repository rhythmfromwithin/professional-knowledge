---
interest: medium
link: https://aws.amazon.com/blogs/machine-learning/orchestrating-sagemaker-ai-endpoint-auto-scaling-with-aws-cdk/
next_step: skim
priority: high
slack_ts: '1793164450.941429'
source: AWS Blog
status: unread
title: Orchestrating SageMaker AI endpoint auto scaling with AWS CDK
---
# Orchestrating SageMaker AI endpoint auto scaling with AWS CDK
> 原文: [https://aws.amazon.com/blogs/machine-learning/orchestrating-sagemaker-ai-endpoint-auto-scaling-with-aws-cdk/](https://aws.amazon.com/blogs/machine-learning/orchestrating-sagemaker-ai-endpoint-auto-scaling-with-aws-cdk/)

Updating a SageMaker AI endpoint that has Application Auto Scaling registered makes AWS CloudFormation and AWS CDK deployments fail. This post shows how to build a reusable AWS CDK construct with CloudFormation custom resources that deregisters and re-registers auto scaling automatically, so you can update the endpoint and its scaling in a single deployment.
