---
interest: medium
link: https://arxiv.org/abs/2609.13802
next_step: skim
priority: low
slack_ts: '1789532917.942819'
source: cs.DB - Databases
status: unread
title: Numerical Stability of Linear Algebra Operations over Relational Databases
---
# Numerical Stability of Linear Algebra Operations over Relational Databases
> 原文: [https://arxiv.org/abs/2609.13802](https://arxiv.org/abs/2609.13802)

arXiv:2609.13802v1 Announce Type: new
Abstract: A large body of work in the database literature develops efficient algorithms for linear algebra and machine learning over matrices defined by relational joins, yet the numerical stability of such computations has so far received no attention. This is a practical concern: a join matrix can be much larger than the input database, and the repeated copies of input values it contains compound the floating-point errors incurred by the numerical operations performed over it.
This paper initiates a formal investigation of numerical stability for linear algebra over database joins. We first show that backward stability, the standard yardstick of numerical stability, loses its effectiveness in this setting: join matrices form a structured subspace of the ambient matrix space, so a perturbation explaining a computed result need not correspond to any perturbed input database. This failure already occurs for operations as simple as matrix-vector multiplication.
To overcome this limitation, we introduce projected backward stability, a generalization of backward stability from the computation of one function to that of a composition of two functions, and establish its connection to classical backward stability. In our database setting, the two functions are the join query and the numerical operation.
We further introduce the database condition number as the square root of the ratio of maximal to minimal number of copies of input data values into the join matrix, and show that it quantifies how a perturbation of the join matrix is amplified into a perturbation of the input database, independently of the computation used. The database condition number coincides with the classical condition number of the expansion matrix that replicates input values into the join matrix.
