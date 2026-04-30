---
title: "Elite-Driven Support Vector Machines for Classification"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2604.25158
priority: medium
status: unread
interest: medium
next_step: skim
---
# Elite-Driven Support Vector Machines for Classification
> 原文: [https://arxiv.org/abs/2604.25158](https://arxiv.org/abs/2604.25158)

arXiv:2604.25158v1 Announce Type: new
Abstract: Support vector machines (SVMs) are a standard tool for binary classification, but their classical formulations are purely data-driven and offer no direct way to encode trusted benchmark models or structured preferences on selected subsets of the data. We propose Elite-Driven Support Vector Machines (EDSVM), a general framework that augments regularized empirical risk minimization by guiding the slack variables for a curated set of elite observations (typically the union of support vectors from one or more reference SVMs). EDSVM combines the usual slack loss with a deviation penalty that shrinks new slacks toward benchmark slack values, defining a localized, margin-aligned notion of proximity to reference models, unlike global function penalties in knowledge distillation or teacher-student methods, and without requiring privileged features as in SVM+/LUPI. Within this framework we develop two concrete models, C-EDSVM and LS-EDSVM, based respectively on hinge-type and squared-slack losses. For both variants we derive dual quadratic programs that can be implemented with modest modifications of standard SVM solvers, and we give simple sufficient conditions under which the induced margin losses are classification calibrated. Simulation studies and experiments on several UCI benchmarks show that EDSVMs closely track the behaviour induced by reference SVMs while achieving predictive performance that is competitive with, and sometimes better than, C-SVM, LINEX-SVM, and LS-SVM.
