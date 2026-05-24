---
interest: medium
link: https://arxiv.org/abs/2605.20234
next_step: skim
priority: high
slack_ts: '1779596217.902239'
source: cs.LG - Machine Learning
status: unread
title: 'TabPFN-MT: A Natively Multitask In-Context Learner for Tabular Data'
---
# TabPFN-MT: A Natively Multitask In-Context Learner for Tabular Data
> 原文: [https://arxiv.org/abs/2605.20234](https://arxiv.org/abs/2605.20234)

arXiv:2605.20234v1 Announce Type: new
Abstract: Prior-Data Fitted networks (PFNs) have been very successful in tabular contexts, handling prediction tasks in context. However, they are designed for single-task inference, meaning that predicting several target values within a context requires repeated forward calls and precludes inter-task information sharing. We propose TabPFN-MT, which is trained on an expanded multi-target synthetic prior to capture inter-task dependencies in context. This model uses an expanded $y$-encoder and a shared decoder head to enable multitask in-context learning and simultaneous inference. The model is uniquely specialized for small-to-medium datasets by relying on in-context learning rather than traditional gradient-based training. Within this regime (averaging fewer than 1,000 samples), extensive evaluations across 344 datasets demonstrate that TabPFN-MT establishes a new state-of-the-art for deep tabular multitask learning. Furthermore, despite the inherent compute asymmetry of joint optimization, our model remains highly competitive with the latest state-of-the-art single-task ensembles. Notably, on multitask datasets it achieves an overall Accuracy rank of 4.89, the highest average rank among all models tested. Crucially, TabPFN-MT delivers this highly competitive performance while reducing the inference cost for $T$ tasks from $O(T)$ to $O(1)$ forward passes, offering a massive computational efficiency improvement for multi-target tabular applications.
