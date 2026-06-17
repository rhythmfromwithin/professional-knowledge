---
interest: medium
link: https://arxiv.org/abs/2606.17582
next_step: skim
priority: low
slack_ts: '1781672187.822399'
source: cs.DB - Databases
status: unread
title: Collaborative Large and Small Language Models for Accurate and Scalable Data
  Repair
---
# Collaborative Large and Small Language Models for Accurate and Scalable Data Repair
> 原文: [https://arxiv.org/abs/2606.17582](https://arxiv.org/abs/2606.17582)

arXiv:2606.17582v1 Announce Type: new
Abstract: We study the problem of data repair, a key task in data cleaning that corrects erroneous entries in raw datasets to improve overall data quality. Although recent data-driven methods, especially those based on large language models (LLMs), achieve remarkable performance, we observe that: (i) they directly repair data in the raw and low-quality context, which may compromise learning signals, and (ii) they directly use uncertain model outputs as repairs, potentially introducing unreliable corrections and compromising repair quality. Motivated by the efficiency of small language models (SLMs) and the capabilities of LLMs, and aiming to address the above limitations, we propose LasRepair, a framework that collaborates Large and small language models for data repair. LasRepair employs an LLM as an instructor, which selects a global repair context to guide the SLM. The SLM acts as a corrector, using the selected context to repair erroneous data more efficiently. Moreover, to further improve context quality, we extend LasRepair to LasRepair+, which formulates data repair as an Expectation-Maximisation (EM) procedure that alternates between an E-step for updating the corrector parameters and an M-step for refining the repair context. Furthermore, to mitigate model uncertainty, we propose LasRepair++, which uses column-calibrated model confidence to down-weight unreliable repaired rows when updating the corrector, thereby enhancing repair quality. Theoretical analysis and empirical evaluation demonstrate the superiority of our methods. We theoretically prove the effectiveness of the EM-style procedure and the confidence-based weighting. Experiments on real-world datasets show that LasRepair++~ achieves an average F1-score improvement of 18.1% over the strongest baseline.
