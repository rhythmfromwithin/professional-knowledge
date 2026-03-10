---
title: "Beyond Linear LLM Invocation: An Efficient and Effective Semantic Filter Paradigm"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.04799
priority: low
status: unread
interest: medium
next_step: skim
---
# Beyond Linear LLM Invocation: An Efficient and Effective Semantic Filter Paradigm
> 原文: [https://arxiv.org/abs/2603.04799](https://arxiv.org/abs/2603.04799)

arXiv:2603.04799v1 Announce Type: new
Abstract: Large language models (LLMs) are increasingly used for semantic query processing over large corpora. A set of semantic operators derived from relational algebra has been proposed to provide a unified interface for expressing such queries, among which the semantic filter operator serves as a cornerstone. Given a table T with a natural language predicate e, for each tuple in the relation, the execution of a semantic filter proceeds by constructing an input prompt that combines the predicate e with its content, querying the LLM, and obtaining the binary decision. However, this tuple-by-tuple evaluation necessitates a complete linear scan of the table, incurring prohibitive latency and token costs. Although recent work has attempted to optimize semantic filtering, it still does not break the linear LLM invocation barriers. To address this, we propose Clustering-Sampling-Voting (CSV), a new framework that reduces LLM invocations to sublinear complexity while providing error guarantees. CSV embeds tuples into semantic clusters, samples a small subset for LLM evaluation, and infers cluster-level labels via two proposed voting strategies: UniVote, which aggregates labels uniformly, and SimVote, which weights votes by semantic similarity. Moreover, CSV triggers re-clustering on ambiguous clusters to ensure robustness across diverse datasets. The results conducted on real-world datasets demonstrate that CSV reduces the number of LLM calls by 1.28-355x compared to the state-of-the-art approaches, while maintaining comparable effectiveness in terms of Accuracy and F1 score.
