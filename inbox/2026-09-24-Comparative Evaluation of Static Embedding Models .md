---
title: "Comparative Evaluation of Static Embedding Models for HTTP Request Anomaly Detection"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2609.26860
priority: low
status: unread
interest: medium
next_step: skim
---
# Comparative Evaluation of Static Embedding Models for HTTP Request Anomaly Detection
> 原文: [https://arxiv.org/abs/2609.26860](https://arxiv.org/abs/2609.26860)

arXiv:2609.26860v1 Announce Type: new
Abstract: Web applications are increasingly targeted by cyberattacks that exploit HTTP requests to evade security mechanisms. Traditional web application firewalls (WAFs) rely on rule-based approaches that often exhibit high false positive rates and limited adaptability. Recent studies have explored machine learning techniques and word embedding models to improve anomaly detection in HTTP traffic. This paper presents a benchmark for static embedding models, specifically Word2Vec, FastText, and Doc2Vec, within a unified, single-class classification framework. We propose HEDA (HTTP Embedding-Based Detection Architecture), a modular detection pipeline that combines static embedding representations with single-class anomaly detection models to detect anomalies at the request level. The approach operates in an unsupervised environment, where both the embedding models and detectors are trained exclusively on benign HTTP traffic. The proposed methodology is evaluated on three datasets with heterogeneous characteristics, including both synthetic and real traffic. The experimental results show that the choice of embedding representation significantly affects detection performance, and that FastText-based embeds produce the most consistent results across all datasets, achieving high detection rates while keeping false positive rates under control.
