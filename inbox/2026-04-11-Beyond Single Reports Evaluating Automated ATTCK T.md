---
interest: medium
link: https://arxiv.org/abs/2604.07470
next_step: skim
priority: low
slack_ts: '1775964761.303809'
source: cs.SE - Software Engineering
status: unread
title: 'Beyond Single Reports: Evaluating Automated ATT&CK Technique Extraction in
  Multi-Report Campaign Settings'
---
# Beyond Single Reports: Evaluating Automated ATT&CK Technique Extraction in Multi-Report Campaign Settings
> 原文: [https://arxiv.org/abs/2604.07470](https://arxiv.org/abs/2604.07470)

arXiv:2604.07470v1 Announce Type: new
Abstract: Large-scale cyberattacks, referred to as campaigns, are documented across multiple CTI reports from diverse sources, with some providing a high-level overview of attack techniques and others providing technical details. Extracting attack techniques from reports is essential for organizations to identify the controls required to protect against attacks. Manually extracting techniques at scale is impractical. Existing automated methods focus on single reports, leaving many attack techniques and their controls undetected, resulting in a fragmented view of campaign behavior. The goal of this study is to aid security researchers in extracting attack techniques and controls from a campaign by replicating and comparing the performance of the state-of-the-art ATT&CK technique extraction methods in a multi-report campaign setting compared to prior single-report evaluations. We conduct an empirical study of 29 methods to extract attack techniques, spanning named entity recognition (NER), encoder-based classification, and decoder-based LLM approaches. Our study analyzes 90 CTI reports across three major attack campaigns: SolarWinds, XZ Utils, and Log4j, using both quantitative performance metrics and their impact on controls. Our results show that aggregating multiple CTI reports improves the F1 score by about 26% over single-report analysis, with most approaches reaching performance saturation after 5--15 reports. Despite these gains, extraction performance remains limited, with maximum F1 scores of 78.6% for SolarWinds and 54.9% for XZ Utils. Moreover, up to 33.3% of misclassifications involve semantically similar techniques that share tactics and overlap in descriptions. The misclassification has a disproportionate effect on control coverage. Reports that are longer and include technical details consistently perform better, even though their readability scores are low.
