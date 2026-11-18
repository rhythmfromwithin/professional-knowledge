---
title: "Modeling Document and Section Hierarchies in Embedding Space"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2611.21980
priority: medium
status: unread
interest: medium
next_step: skim
---
# Modeling Document and Section Hierarchies in Embedding Space
> 原文: [https://arxiv.org/abs/2611.21980](https://arxiv.org/abs/2611.21980)

arXiv:2611.21980v1 Announce Type: new
Abstract: Embedded topic models integrate word embeddings into the topic generation process, producing coherent topics and robust performance on large vocabularies. However, each document is represented by a single topic distribution, ignoring its internal structure. Many real world collections, including legal documents, company and government reports, and online discussion forums, exhibit hierarchical organization in which documents consist of multiple sections that often address distinct subtopics. We introduce the Hierarchical Embedded Topic Model (hETM), a structured topic model that couples the topic distribution of a document and those of its sections through a hierarchical prior in the embedding space. We derive an amortized variational inference procedure for hETM and evaluate it on structured collections from each of these domains. Experimental results show that hETM achieves the lowest or near-lowest held-out perplexity among flat and hierarchical topic model baselines, along with comparable or higher topic quality. It also performs strongly on a downstream clustering task, achieving the best clustering performance on most of the collections.
