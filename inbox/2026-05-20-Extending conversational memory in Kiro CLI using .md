---
title: "Extending conversational memory in Kiro CLI using Amazon Bedrock AgentCore Memory"
source: "AWS Blog"
link: https://aws.amazon.com/blogs/machine-learning/extending-conversational-memory-in-kiro-cli-using-amazon-bedrock-agentcore-memory/
priority: high
status: unread
interest: medium
next_step: skim
---
# Extending conversational memory in Kiro CLI using Amazon Bedrock AgentCore Memory
> 原文: [https://aws.amazon.com/blogs/machine-learning/extending-conversational-memory-in-kiro-cli-using-amazon-bedrock-agentcore-memory/](https://aws.amazon.com/blogs/machine-learning/extending-conversational-memory-in-kiro-cli-using-amazon-bedrock-agentcore-memory/)

In this post, we demonstrate how you can extend the conversational memory of Kiro CLI by implementing a custom Model Context Protocol (MCP) server that integrates with Amazon Bedrock AgentCore Memory. You can use Kiro CLI to interact with AI agents of Kiro directly from your terminal. Amazon Bedrock AgentCore Memory is a fully managed service that allows AI agents to retain information from past interactions, creating more intelligent and context-aware conversations. By implementing a custom MCP server, you can provide Kiro CLI with tools to store and retrieve conversation context, monitor memory usage, and manage the underlying Bedrock Agent Core Memory infrastructure.
