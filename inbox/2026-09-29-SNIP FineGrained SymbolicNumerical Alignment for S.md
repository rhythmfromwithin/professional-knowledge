---
title: "SNIP++: Fine-Grained Symbolic-Numerical Alignment for Symbolic Regression"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2609.31965
priority: low
status: unread
interest: medium
next_step: skim
---
# SNIP++: Fine-Grained Symbolic-Numerical Alignment for Symbolic Regression
> 原文: [https://arxiv.org/abs/2609.31965](https://arxiv.org/abs/2609.31965)

arXiv:2609.31965v1 Announce Type: new
Abstract: Mathematical expressions and the numerical behavior they produce are two views of the same underlying function, and connecting them is central to scientific discovery. Symbolic Regression (SR) relies on this connection directly: it searches for an expression that reproduces a given behavior. Recent multi-modal models learn this connection by embedding symbolic expressions and their numerical behavior in a shared representation space. We show that this embedding space is only globally aligned: complete expressions correspond to complete behaviors, but the contribution of individual parts of an expression is not represented. This granularity gap leaves the model unable to tell how a local edit to an expression changes its behavior, the central operation in SR. We introduce a compositional alignment method that closes this gap: a structural positional encoding exposes the substructure of an expression to the encoder, and a multi-granularity contrastive objective grounds each subexpression in the behavior it produces before propagating this grounding to the full expression. The resulting representations close much of the modality gap between symbolic and numerical embeddings, reliably distinguish the effects of local edits that the original alignment cannot, and transfer to external SR corpora.
