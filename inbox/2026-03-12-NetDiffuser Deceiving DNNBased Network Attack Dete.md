---
interest: medium
link: https://arxiv.org/abs/2603.08901
next_step: skim
priority: low
slack_ts: '1773283554.307829'
source: cs.CR - Cryptography and Security
status: unread
title: 'NetDiffuser: Deceiving DNN-Based Network Attack Detection Systems with Diffusion-Generated
  Adversarial Traffic'
---
# NetDiffuser: Deceiving DNN-Based Network Attack Detection Systems with Diffusion-Generated Adversarial Traffic
> 原文: [https://arxiv.org/abs/2603.08901](https://arxiv.org/abs/2603.08901)

arXiv:2603.08901v1 Announce Type: new
Abstract: Deep learning (DL)-based Network Intrusion Detection System (NIDS) has demonstrated great promise in detecting malicious network traffic. However, they face significant security risks due to their vulnerability to adversarial examples (AEs). Most existing adversarial attacks maliciously perturb data to maximize misclassification errors. Among AEs, natural adversarial examples (NAEs) are particularly difficult to detect because they closely resemble real data, making them challenging for both humans and machine learning models to distinguish from legitimate inputs. Creating NAEs is crucial for testing and strengthening NIDS defenses. This paper proposes NetDiffuser1, a novel framework for generating NAEs capable of deceiving NIDS. NetDiffuser consists of two novel components. First, a new feature categorization algorithm is designed to identify relatively independent features in network traffic. Perturbing these features minimizes changes while preserving network flow validity. The second component is a novel application of diffusion models to inject semantically consistent perturbations for generating NAEs. NetDiffuser performance was extensively evaluated using three benchmark NIDS datasets across various model architectures and state-of-the-art adversarial detectors. Our experimental results show that NetDiffuser achieves up to a 29.93% higher attack success rate and reduces AE detection performance by at least 0.267 (in some cases up to 0.534) in the Area under the Receiver Operating Characteristic Curve (AUC-ROC) score compared to the baseline attacks.
