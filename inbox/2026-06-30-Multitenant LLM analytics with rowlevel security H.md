---
interest: medium
link: https://aws.amazon.com/blogs/machine-learning/multi-tenant-llm-analytics-with-row-level-security-how-we-built-a-secure-agent-on-aws/
next_step: skim
priority: high
slack_ts: '1782792824.362959'
source: AWS Blog
status: unread
title: 'Multi-tenant LLM analytics with row-level security: How we built a secure
  agent on AWS'
---
# Multi-tenant LLM analytics with row-level security: How we built a secure agent on AWS
> 原文: [https://aws.amazon.com/blogs/machine-learning/multi-tenant-llm-analytics-with-row-level-security-how-we-built-a-secure-agent-on-aws/](https://aws.amazon.com/blogs/machine-learning/multi-tenant-llm-analytics-with-row-level-security-how-we-built-a-secure-agent-on-aws/)

In this post, we show you how PAR built a production-ready multi-tenant LLM analytics system that enforces row-level security through a three-layer architecture: cryptographic request signing with AWS SigV4, semantic validation on Amazon Bedrock, and programmatic data isolation via Split-Plane SQL. We demonstrate how each layer operates independently to reduce the risk of cross-tenant data exposure, even when the LLM itself is compromised or manipulated.
