---
interest: medium
link: https://arxiv.org/abs/2609.22401
next_step: skim
priority: low
slack_ts: '1790137535.233269'
source: cs.CR - Cryptography and Security
status: unread
title: Differentially Private and Fairness-Audited Score Diffusion for Irregular Longitudinal
  Health Records
---
# Differentially Private and Fairness-Audited Score Diffusion for Irregular Longitudinal Health Records
> 原文: [https://arxiv.org/abs/2609.22401](https://arxiv.org/abs/2609.22401)

arXiv:2609.22401v1 Announce Type: new
Abstract: Sharing irregular longitudinal health records can accelerate model development, yet synthetic releases may leak participation, distort temporal dependence, suppress rare events, or reduce utility for underrepresented groups. We present TRUST LONGSYNTH, an auditable patient level private generator that combines bounded sufficient statistics, zCDP accounted Gaussian releases, conditional analytic score diffusion, block banded temporal covariance, separate missingness and gap models, and a protected event sampling floor with population weights.
The method was evaluated on five independently generated, three cohort benchmarks containing 720 patients, fourteen irregular observation slots, six mixed variables, informative missingness, and a rare deterioration outcome. At epsilon = 12 and delta = 10 to the power of minus 5, TRUST LONGSYNTH achieved mean train synthetic test real AUPRC 0.342, Brier score 0.088, expected calibration error 0.082, correlation error 0.222, autocorrelation error 0.317, and membership attack AUROC 0.499.
Relative to the private diagonal score baseline, AUPRC increased by 7.5 percent, while Brier, calibration, correlation, and autocorrelation errors decreased by 6.1 percent, 17.0 percent, 28.0 percent, and 30.1 percent, respectively. The method did not dominate every nonprivate or discrete baseline, and corrected paired tests were inconclusive with five seeds. Canary exposure was 1.8 percent, compared with 28.8 percent for DP Score in the same stress test.
These findings support a transparent privacy utility fairness evaluation protocol, not clinical validity or unconditional release safety, and motivate governed external validation on real multi site records.
