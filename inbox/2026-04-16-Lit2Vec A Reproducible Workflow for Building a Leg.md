---
interest: medium
link: https://arxiv.org/abs/2604.12498
next_step: skim
priority: low
slack_ts: '1776396649.163819'
source: cs.DB - Databases
status: unread
title: 'Lit2Vec: A Reproducible Workflow for Building a Legally Screened Chemistry
  Corpus from S2ORC for Downstream Retrieval and Text Mining'
---
# Lit2Vec: A Reproducible Workflow for Building a Legally Screened Chemistry Corpus from S2ORC for Downstream Retrieval and Text Mining
> 原文: [https://arxiv.org/abs/2604.12498](https://arxiv.org/abs/2604.12498)

arXiv:2604.12498v1 Announce Type: new
Abstract: We present Lit2Vec, a reproducible workflow for constructing and validating a chemistry corpus from the Semantic Scholar Open Research Corpus using conservative, metadata-based license screening. Using this workflow, we assembled an internal study corpus of 582,683 chemistry-specific full-text research articles with structured full text, token-aware paragraph chunks, paragraph-level embeddings generated with the intfloat/e5-large-v2 model, and record-level metadata including abstracts and licensing information. To support downstream retrieval and text-mining use cases, an eligible subset of the corpus was additionally enriched with machine-generated brief summaries and multi-label subfield annotations spanning 18 chemistry domains. Licensing was screened using metadata from Unpaywall, OpenAlex, and Crossref, and the resulting corpus was technically validated for schema compliance, embedding reproducibility, text quality, and metadata completeness. The primary contribution of this work is a reproducible workflow for corpus construction and validation, together with its associated schema and reproducibility resources. The released materials include the code, reconstruction workflow, schema, metadata/provenance artifacts, and validation outputs needed to reproduce the corpus from pinned public upstream resources. Public redistribution of source-derived text and broad text-derived representations is outside the scope of the general release. Researchers can reproduce the workflow by using the released pipeline with publicly available upstream datasets and metadata services.
