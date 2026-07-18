---
interest: medium
link: https://aws.amazon.com/blogs/machine-learning/building-a-restaurant-telephony-ai-host-with-amazon-bedrock-agentcore-and-amazon-nova-2-sonic/
next_step: skim
priority: high
slack_ts: '1784344397.985869'
source: AWS Blog
status: unread
title: Building a restaurant telephony AI host with Amazon Bedrock AgentCore and Amazon
  Nova 2 Sonic
---
# Building a restaurant telephony AI host with Amazon Bedrock AgentCore and Amazon Nova 2 Sonic
> 原文: [https://aws.amazon.com/blogs/machine-learning/building-a-restaurant-telephony-ai-host-with-amazon-bedrock-agentcore-and-amazon-nova-2-sonic/](https://aws.amazon.com/blogs/machine-learning/building-a-restaurant-telephony-ai-host-with-amazon-bedrock-agentcore-and-amazon-nova-2-sonic/)

In this post, we show you how to build a voice ordering system that answers a phone number and takes the order from greeting to confirmation. The system uses Amazon Bedrock AgentCore to host and run the agent and Amazon Nova 2 Sonic for real-time speech, connected to a restaurant backend through the Model Context Protocol (MCP). The walkthrough covers deploying the full stack with AWS Cloud Development Kit (AWS CDK) and bridging a phone call into the agent through a Session Initiation Protocol (SIP) gateway on Amazon Elastic Container Service (Amazon ECS) and AWS Fargate. It also warms the agent session while the phone is still ringing, so the caller never hears dead air.
