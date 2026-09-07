---
title: "An Analysis of Self-supervised Pre-training with Dependent Samples"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.05031
priority: medium
status: unread
interest: medium
next_step: skim
---
# An Analysis of Self-supervised Pre-training with Dependent Samples
> 原文: [https://arxiv.org/abs/2609.05031](https://arxiv.org/abs/2609.05031)

arXiv:2609.05031v1 Announce Type: new
Abstract: Self-supervised learning relies on so-called data augmentations $\phi(x)$ of unlabeled datapoints $x$ --- for example, masking random pixels in an image $x$ --- that should leave the label of $x$ invariant and are often used to learn a lower-complexity invariant subspace $\cal V$ for downstream tasks. In practice, such augmentations $\{ \phi\_l(x\_i) \}$ are pooled together to learn $\cal V$, despite obvious inter-dependencies between different augmentations $\phi\_l(x), \phi\_k(x)$ of the same datapoint $x$. However, theoretical works on the subject typically consider procedures that avoid such dependencies, and are therefore limited to operate on smaller subsets of independent data.
We show in this work that pooling augmentations together, despite inter-dependencies, is a better alternative than the baseline of partitioning the data into subsets of independent data. More precisely, in the context of estimating $\cal V$, the statistical estimation error bounds for pooling are never worse than the partitioning baseline, and in some cases --- such as masking or noise injection-based augmentations over a shallow neural network --- naive pooling leads to faster rates in terms of the number of augmentations. The benefits of pooling are particularly prominent when the correlations between different augmentations $\phi\_l(x), \phi\_k(x)$ have mild effects on estimation or help decrease the estimation variance. The analysis, therefore, yields new insights into the success of pooling augmented samples in self-supervised pre-training, and provides an intuition behind the practical preference towards using many augmentations.
