---
title: "Exact Mining of Dense Patterns via Direct Evaluation of Local Interval Frequency Using a Sliding Window"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2604.24122
priority: low
status: unread
interest: medium
next_step: skim
---
# Exact Mining of Dense Patterns via Direct Evaluation of Local Interval Frequency Using a Sliding Window
> 原文: [https://arxiv.org/abs/2604.24122](https://arxiv.org/abs/2604.24122)

arXiv:2604.24122v1 Announce Type: new
Abstract: Accurately extracting patterns that appear frequently only within specific time intervals, together with their dense intervals, is important in many applications such as understanding seasonal demand and detecting anomalous behavior.Frequent itemset mining evaluates support over the entire dataset and therefore cannot detect locally dense patterns. Existing methods for dense pattern mining with interval output estimate dense intervals through occurrence-gap constraints; however, since the gap constraint parameter governs both pattern identification accuracy and interval detection accuracy simultaneously, finding a parameter setting that achieves high accuracy for both objectives is difficult.In this paper, we propose Apriori-window, an exact algorithm that resolves this structural limitation. The proposed method directly evaluates local frequency within a sliding window and thus requires no gap constraint parameter, and it efficiently enumerates dense intervals through anti-monotonicity-based pruning of the search space and stride-skip reduction of the number of window scans. Experiments on three real-world datasets demonstrate that existing methods struggle to simultaneously achieve high accuracy in both pattern identification and dense interval detection, and scalability experiments on synthetic data confirm the practical applicability of the proposed method.
