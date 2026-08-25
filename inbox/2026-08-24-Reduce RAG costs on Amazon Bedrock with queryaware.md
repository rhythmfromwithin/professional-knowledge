---
interest: medium
link: https://aws.amazon.com/blogs/machine-learning/reduce-rag-costs-on-amazon-bedrock-with-query-aware-compression/
next_step: skim
priority: high
slack_ts: '1787622057.863779'
source: AWS Blog
status: unread
title: Reduce RAG costs on Amazon Bedrock with query-aware compression
---
# Reduce RAG costs on Amazon Bedrock with query-aware compression
> 原文: [https://aws.amazon.com/blogs/machine-learning/reduce-rag-costs-on-amazon-bedrock-with-query-aware-compression/](https://aws.amazon.com/blogs/machine-learning/reduce-rag-costs-on-amazon-bedrock-with-query-aware-compression/)

Input tokens are often a meaningful part of the cost of running Retrieval Augmented Generation (RAG) at scale. This post describes a query-aware context compression pattern on Amazon Bedrock: after retrieval, a smaller model filters retrieved chunks against the query before the primary model answers, reducing input tokens and cost while preserving answer quality.
