---
title: "Reference your own AWS Secrets Manager secrets in Amazon Bedrock AgentCore Identity"
source: "AWS Blog"
link: https://aws.amazon.com/blogs/machine-learning/reference-your-own-aws-secrets-manager-secrets-in-amazon-bedrock-agentcore-identity/
priority: high
status: unread
interest: medium
next_step: skim
---
# Reference your own AWS Secrets Manager secrets in Amazon Bedrock AgentCore Identity
> 原文: [https://aws.amazon.com/blogs/machine-learning/reference-your-own-aws-secrets-manager-secrets-in-amazon-bedrock-agentcore-identity/](https://aws.amazon.com/blogs/machine-learning/reference-your-own-aws-secrets-manager-secrets-in-amazon-bedrock-agentcore-identity/)

Today, we’re excited to announce the ability to reference a secret in AWS Secrets Manager for AgentCore Identity, so you can reference your own preconfigured secret from Secrets Manager and retain full control over how it is managed. With this ability, you can extend your organization’s existing secrets governance processes to AgentCore. You can provide an existing, preconfigured AWS Secrets Manager secret to use with your credential provider resources. You retain full control over its encryption configuration, rotation, replication, tags, and resource policies, just as you would manage other secrets in Secrets Manager. You can also choose a secret from another AWS account within the same AWS Region, though cross-Region secret sharing isn’t supported. This also supports secrets brought in through AWS Secrets Manager external connectors, enabling integration with third-party secret managers.
