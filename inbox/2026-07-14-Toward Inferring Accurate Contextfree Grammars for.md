---
title: "Toward Inferring Accurate Context-free Grammars for Big Languages in a Black-box Setting"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2607.08959
priority: low
status: unread
interest: medium
next_step: skim
---
# Toward Inferring Accurate Context-free Grammars for Big Languages in a Black-box Setting
> 原文: [https://arxiv.org/abs/2607.08959](https://arxiv.org/abs/2607.08959)

arXiv:2607.08959v2 Announce Type: new
Abstract: Black-box context-free grammar inference is crucial for program analysis, reverse engineering, program understanding, fuzzing, and security. But existing approaches such as Arvada, TreeVada, Kedavra, and Cucio struggle with scalability, accuracy, and grammar readability, especially on larger languages. To address this challenge, we introduce XVada with several new techniques for deterministic inference of context-free grammars. In an empirical comparison that avoids several pitfalls of recent studies, XVada improves on the highest-scoring competitor (TreeVada) both in grammar accuracy and grammar compactness. XVada also found a CVE in the widely used Python Liquid engine. Fuzzing based on the XVada-inferred grammar found five more bugs, which the Python Liquid developers fixed based on our bug reports. XVada and all experimental data and scripts are freely available.
