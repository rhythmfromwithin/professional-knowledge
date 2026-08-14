---
interest: medium
link: https://arxiv.org/abs/2608.08261
next_step: skim
priority: low
slack_ts: '1786674567.625739'
source: cs.DB - Databases
status: unread
title: 'Scout: Scalable Document Extraction via Data Similarity'
---
# Scout: Scalable Document Extraction via Data Similarity
> 原文: [https://arxiv.org/abs/2608.08261](https://arxiv.org/abs/2608.08261)

arXiv:2608.08261v1 Announce Type: new
Abstract: Extracting values from large document collections powers data analysis across many domains. Frontier LLMs extract such values accurately, but processing an
entire collection with one is prohibitively costly. Yet this cost is largely avoidable: real-world collections exhibit rich similarity, so for the same query
over similar documents, the answer tends to recur in similar locations; an LLM need only read that small span, not the whole document. Prior methods that
exploit this similarity fall short: they either assume a rigid document structure, or assume the answer is a set of substrings of the input and use an
LLM-generated program to return it directly. Even a frontier agent fails to generate effective programs to directly locate the answer's span, as the search
space is large and programs learned from a small sample tend to overfit. We present Scout, a tool that generates accurate and cost-effective programs (that
we call rules) to extract data at scale. From a few sampled documents, Scout generates a broad rule set and refines it by selecting a pareto-optimal subset
with low cost without sacrificing accuracy. We prove rule refinement is NP-hard and give a greedy solution with a provable approximation guarantee. Scout
handles collections that are only partly similar, where similarity holds within clusters of documents. In this setting, a sampling strategy, using no LLM,
draws samples from each cluster; and a cascade strategy selects a subset of refined rules, falling back to the unrefined rule set when the selected rules
don't contain the answer. Experiments on six real-world datasets show that Scout matches the accuracy of the strongest baseline, a frontier LLM agent that
reads each full document, while being 61x to over 1000x cheaper on a collection of 1,000 documents, and is 61% more accurate than the strongest prior
program-based approach.
