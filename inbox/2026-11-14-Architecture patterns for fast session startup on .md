---
interest: medium
link: https://aws.amazon.com/blogs/machine-learning/architecture-patterns-for-fast-session-startup-on-amazon-bedrock-agentcore-runtime/
next_step: skim
priority: high
slack_ts: '1794635835.274989'
source: AWS Blog
status: unread
title: Architecture patterns for fast session startup on Amazon Bedrock AgentCore
  runtime
---
# Architecture patterns for fast session startup on Amazon Bedrock AgentCore runtime
> 原文: [https://aws.amazon.com/blogs/machine-learning/architecture-patterns-for-fast-session-startup-on-amazon-bedrock-agentcore-runtime/](https://aws.amazon.com/blogs/machine-learning/architecture-patterns-for-fast-session-startup-on-amazon-bedrock-agentcore-runtime/)

Amazon Bedrock AgentCore runtime V2 snapshots your initialized environment and restores it for each new session, so session start no longer grows with image size. This post explains how V2 starts a session, how to measure session start time, and four patterns to keep work off the first request.
