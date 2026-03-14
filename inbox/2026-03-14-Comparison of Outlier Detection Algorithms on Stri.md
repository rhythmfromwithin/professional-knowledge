---
title: "Comparison of Outlier Detection Algorithms on String Data"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.11049
priority: high
status: unread
interest: medium
next_step: skim
---
# Comparison of Outlier Detection Algorithms on String Data
> 原文: [https://arxiv.org/abs/2603.11049](https://arxiv.org/abs/2603.11049)

arXiv:2603.11049v1 Announce Type: new
Abstract: Outlier detection is a well-researched and crucial problem in machine learning. However, there is little research on string data outlier detection, as most literature focuses on outlier detection of numerical data. A robust string data outlier detection algorithm could assist with data cleaning or anomaly detection in system log files. In this thesis, we compare two string outlier detection algorithms. Firstly, we introduce a variant of the well-known local outlier factor algorithm, which we tailor to detect outliers on string data using the Levenshtein measure to calculate the density of the dataset. We present a differently weighted Levenshtein measure, which considers hierarchical character classes and can be used to tune the algorithm to a specific string dataset. Secondly, we introduce a new kind of outlier detection algorithm based on the hierarchical left regular expression learner, which infers a regular expression for the expected data. Using various datasets and parameters, we experimentally show that both algorithms can conceptually find outliers in string data. We show that the regular expression-based algorithm is especially good at finding outliers if the expected values have a distinct structure that is sufficiently different from the structure of the outliers. In contrast, the local outlier factor algorithms are best at finding outliers if their edit distance to the expected data is sufficiently distinct from the edit distance between the expected data.
