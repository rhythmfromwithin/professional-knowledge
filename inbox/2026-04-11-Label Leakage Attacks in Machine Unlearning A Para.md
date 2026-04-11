---
title: "Label Leakage Attacks in Machine Unlearning: A Parameter and Inversion-Based Approach"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2604.07386
priority: low
status: unread
interest: medium
next_step: skim
---
# Label Leakage Attacks in Machine Unlearning: A Parameter and Inversion-Based Approach
> 原文: [https://arxiv.org/abs/2604.07386](https://arxiv.org/abs/2604.07386)

arXiv:2604.07386v1 Announce Type: new
Abstract: With the widespread application of artificial intelligence technologies in face recognition and other fields, data privacy security issues have received extensive attention, especially the \textit{right to be forgotten} emphasized by numerous privacy protection laws. Existing technologies have proposed various unlearning methods, but they may inadvertently leak the categories of unlearned data. This paper focuses on the category unlearning scenario, analyzes the potential problems of category leakage of unlearned data in multiple scenarios, and proposes four attack methods from the perspectives of model parameters and model inversion based on attackers with different knowledge backgrounds. At the level of model parameters, we construct discriminative features by computing either dot products or vector differences between the parameters of the target model and those of auxiliary models trained on subsets of retained data and unrelated data, respectively. These features are then processed via k-means clustering, Youden's Index, and decision tree algorithms to achieve accurate identification of the forgotten class. In the model inversion domain, we design a gradient optimization-based white-box attack and a genetic algorithm-based black-box attack to reconstruct class-prototypical samples. The prediction profiles of these synthesized samples are subsequently analyzed using a threshold criterion and an information entropy criterion to infer the forgotten class. We evaluate the proposed attacks on four standard datasets against five state-of-the-art unlearning algorithms, providing a detailed analysis of the strengths and limitations of each method. Experimental results demonstrate that our approach can effectively infer the classes forgotten by the target model.
