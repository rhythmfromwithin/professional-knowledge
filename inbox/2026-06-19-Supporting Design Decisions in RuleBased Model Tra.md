---
title: "Supporting Design Decisions in Rule-Based Model Transformations"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2606.19342
priority: low
status: unread
interest: medium
next_step: skim
---
# Supporting Design Decisions in Rule-Based Model Transformations
> 原文: [https://arxiv.org/abs/2606.19342](https://arxiv.org/abs/2606.19342)

arXiv:2606.19342v1 Announce Type: new
Abstract: Model Driven Engineering relies on model transformations to automate the derivation of target models or source code from source models. However, the design decisions that govern how source elements are mapped to target artifacts typically remain embedded in the transformation source code, limiting flexibility, reusability, and traceability. This paper proposes an approach to explicitly model and manage design decisions in rule-based model transformations. Design decisions are separated from transformation implementation through three mechanisms. First, a decision model captures design decisions and their options independently of any source modeling language for a given transformation domain. Second, a binding model connects these decisions to specific metamodel concepts in a given source modeling language, enabling reuse of the same design knowledge across transformations from similar languages. Third, a configuration model records the specific option chosen for each applicable source model element, with defaults pre-selected automatically. During execution, variability points in transformation rules are resolved dynamically according to configured choices. A trace model records which rules and options were applied to produce each target element. We establish a formal mathematical framework that defines the core concepts of variability-based transformations and proves key properties of the resulting transformations. The formal concepts are realized in a practical architecture of four interconnected artifact models. We demonstrate practical feasibility by extending an existing embedded domain-specific language for model-driven engineering with variability support and illustrate the approach with a complete ER-to-Relational transformation example.
