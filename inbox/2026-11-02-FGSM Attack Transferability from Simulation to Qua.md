---
title: "FGSM Attack Transferability from Simulation to Quantum Hardware in Network Intrusion Detection"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2610.40701
priority: low
status: unread
interest: medium
next_step: skim
---
# FGSM Attack Transferability from Simulation to Quantum Hardware in Network Intrusion Detection
> 原文: [https://arxiv.org/abs/2610.40701](https://arxiv.org/abs/2610.40701)

arXiv:2610.40701v1 Announce Type: new
Abstract: Quantum computers are now available through cloud platforms, and recent work has proposed using them to detect network intrusions. It is not yet clear how easily such systems can be attacked. We train a hybrid variational quantum classifier (VQC) on the Friday DDoS subset of CICIDS2017 and test it against two attacks: label flipping during training and FGSM evasion at prediction time. We run the tests in simulation and on IBM hardware, the Fez superconducting processor (Heron r2). We find that two models with similar accuracy can differ greatly in how easily they are attacked. A model that decides with little confidence loses half its detections to a very small change in the input, while a model trained to decide with more confidence needs a much larger change before it fails. Attacks built in simulation against the more confident model also work on real hardware, and the device classifies every unaltered attack sample correctly. Simulated device noise does not reduce accuracy, but it does reduce the model's confidence and makes attacks easier, so accuracy alone does not show how exposed a model is. Label flipping has no measurable effect until 15% of attack labels are changed. These results show that device noise should not be treated as a defense and that reported weaknesses in these classifiers depend partly on how they were trained.
