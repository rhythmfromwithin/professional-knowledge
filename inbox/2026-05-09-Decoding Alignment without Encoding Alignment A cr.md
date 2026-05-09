---
title: "Decoding Alignment without Encoding Alignment: A critique of similarity analysis in neuroscience"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2605.05907
priority: low
status: unread
interest: medium
next_step: skim
---
# Decoding Alignment without Encoding Alignment: A critique of similarity analysis in neuroscience
> 原文: [https://arxiv.org/abs/2605.05907](https://arxiv.org/abs/2605.05907)

arXiv:2605.05907v1 Announce Type: new
Abstract: Decoding approaches are widely used in neuroscience and machine learning to compare stimulus representations across neural systems, such as different brain regions, organisms, and deep learning models. Popular methods include decoding (perceptual) manifolds and alignment metrics such as Representational Similarity Analysis (RSA) and Dynamic Similarity Analysis (DSA), where similarity in decoding representations is interpreted as evidence for similar computation. This paper demonstrates a fundamental weakness behind this approach: it is misleading to assume that representational geometry is representative of a neuronal population as a whole, when such representations may actually be shaped by a very small subset of neurons. We show that the complementary encoding paradigm addresses this issue directly: it characterizes how neurons are organized globally in terms of their responses to a set of data, providing insight into how the decoding representation is implemented by neurons within a population. We demonstrate across experiments in biological systems and deep learning models that (i) surprisingly, similar decoding behavior and high representational alignment can arise from small, non-representative subpopulations of neurons; and critically, (ii) alignment metrics are insensitive to encoding manifold topology (how function is distributed across neurons), despite this being a key signature of differentiation across biological systems. A controlled MNIST experiment provides causal evidence: decoding metrics remain unchanged even when encoding topology is causally manipulated via the training loss. Overall, similarity in decoding behavior, as measured by classic alignment metrics, does not imply similarity in function or computation, motivating the use of encoding manifolds as a complementary tool for comparing neural systems.
