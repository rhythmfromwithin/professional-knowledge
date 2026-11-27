---
interest: medium
link: https://arxiv.org/abs/2611.31679
next_step: skim
priority: low
slack_ts: '1795766097.408219'
source: cs.DB - Databases
status: unread
title: Rethinking Document Indexing for LLM-based Analysis
---
# Rethinking Document Indexing for LLM-based Analysis
> 原文: [https://arxiv.org/abs/2611.31679](https://arxiv.org/abs/2611.31679)

arXiv:2611.31679v1 Announce Type: new
Abstract: Documents such as clinical records, legal contracts, and scientific papers are increasingly analyzed with large language models (LLMs). The na\"ive approach of prompting the model with the full text for every question is slow, expensive, prone to hallucination on long inputs, and reuses no work across questions. Retrieval-augmented generation (RAG) systems build reusable state to address this, but they store it as embedded chunks: slicing text into fragments can lose the meaning that spans them, and the resulting index is tied to one embedding model, so it must be rebuilt whenever that model changes. Answering many questions over a large body of data without a full rescan, however, is not a new problem: it is the problem database indexes have been solving for decades, and we argue that this accumulated index design knowledge is waiting to be revisited for LLM access.
As a concrete starting point, we propose Periplus, a hierarchical plain-text index inspired by the classic B+ tree. It arranges a document into pages running from general summaries at the root to specific ones at the leaves, so that each level guides the search into the next. But it departs from the B+ tree in three ways suited to LLM access: content lives at every level, the pages are plain text rather than attribute values, and navigation follows the relevance of a page summary to the question rather than a key comparison. The structure itself is discovered per document by the LLM rather than hand-designed in advance. In a preliminary evaluation on narrative and contract corpora, Periplus comes within 0.1--0.9 percentage points of the strongest baseline's accuracy while consuming 70--72\% fewer total tokens. These early results are encouraging, and they offer only a glimpse of what index design can bring to LLM-based analysis.
