---
title: "ReCoPII: A Relation-Grounded Framework for Building Contextual PII Masking Datasets"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2610.35925
priority: high
status: unread
interest: medium
next_step: skim
---
# ReCoPII: A Relation-Grounded Framework for Building Contextual PII Masking Datasets
> 原文: [https://arxiv.org/abs/2610.35925](https://arxiv.org/abs/2610.35925)

arXiv:2610.35925v1 Announce Type: new
Abstract: Training contextual masking systems for personally identifiable information (PII) requires examples distinguishing maskable from preservable mentions of one entity type, but privacy restrictions limit access to real data. Author-based augmentation (SPY) labels mentions unrelated to the author as non-PII, presuming a single data subject and overlooking others. We propose ReCoPII (Relation-grounded Contextual PII masking), a framework that builds such data without this premise: it plans ontology-constrained entity relations, writes insertion sentences with placeholders, reconstructs annotations with code, checks the result with a separate LLM, and derives MASK/KEEP labels from entity relations. On Korean documents from six domains, it yields ReCoPII-Ko, a corpus with relation, privacy, and MASK/KEEP annotations, which we validate. Across 300 pairs, four annotators agree with 88.42% of its sampled KEEP labels, against 26.27% for SPY-style augmentation of the same sources. Classifiers trained on it over-mask less than under that reference on a matched test. Contextual masking fine-tuned jointly with a PII detector removes most over-masking of detection alone within a fixed leakage budget; on human-verified entity records, the four detectors meeting it over-mask at most 5.04% with at most 4.18% leakage. The detector is comparable to XLM-R-large on KDPII with about a quarter of its parameters.
