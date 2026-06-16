---
title: "Schema-Agnostic Process Trace Construction: From Raw Tables to Execution Behavior"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2606.14775
priority: low
status: unread
interest: medium
next_step: skim
---
# Schema-Agnostic Process Trace Construction: From Raw Tables to Execution Behavior
> 原文: [https://arxiv.org/abs/2606.14775](https://arxiv.org/abs/2606.14775)

arXiv:2606.14775v1 Announce Type: new
Abstract: Traditional information systems (IS) engineering assumes stable schemas, explicit keys, and curated event logs. In modern OLTP environments, schemas drift, keys are sparse, and execution traces are dispersed across loosely connected tables, making manual process trace construction costly and error prone. We propose a schema-agnostic pipe-line that automatically reconstructs process execution traces directly from raw relational data. The pipeline (i) identifies columns that function like keys or timestamps, (ii) discovers table-to-table connections using statistical signals rather than predefined schemas, (iii) assembles and orders events for each case while accommodating multiple date fields, and (iv) learns likely ordering and flow relations across systems using a Temporal Convolutional Network which models long-range dependencies and patterns. Evaluations on TPC-H/E benchmarks, synthetic corpora, and a real industry dataset show that our pipeline reconstructs high-fidelity event traces and accurate trace orderings, correctly predicting the next event with 85% accuracy and recovering about 82% of ground-truth precedence relations. By eliminating dependence on predefined schemas, ER diagrams and domain templates, our work offers a generalizable and scalable pathway for automated reconstruction of execution behaviour in dynamic and continuously evolving IS environments.
