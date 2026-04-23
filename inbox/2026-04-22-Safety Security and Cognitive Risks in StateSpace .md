---
interest: medium
link: https://arxiv.org/abs/2604.16424
next_step: skim
priority: low
slack_ts: '1776915191.557169'
source: cs.CR - Cryptography and Security
status: unread
title: 'Safety, Security, and Cognitive Risks in State-Space Models: A Systematic
  Threat Analysis with Spectral, Stateful, and Capacity Attacks'
---
# Safety, Security, and Cognitive Risks in State-Space Models: A Systematic Threat Analysis with Spectral, Stateful, and Capacity Attacks
> 原文: [https://arxiv.org/abs/2604.16424](https://arxiv.org/abs/2604.16424)

arXiv:2604.16424v1 Announce Type: new
Abstract: State-Space Models (SSMs) -- structured SSMs (S4, S4D, DSS, S5), selective SSMs (Mamba, Mamba-2), and hybrid architectures (Jamba) -- are deployed in safety-critical long-context applications: genomic analysis, clinical time-series forecasting, and cybersecurity log processing. Their linear-time scaling is compelling, yet the security properties of their compressed-state recurrent architectures remain unstudied.
We present the first systematic treatment of SSM safety, security, and cognitive risks. Seven contributions: (1) Formal threat framework -- SSM Attack Surface (five layers), State Integrity Violation (StIV), Cross-Context Amplification Ratio $\mathcal{X}\_\mathcal{S}$, and a Spectral Sensitivity Proposition grounded in the $H\_\infty$ norm. (2) Three novel attack classes: spectral adversarial attacks (transfer-function gain exploitation), delayed-trigger stateful backdoors (activate thousands of steps after injection), and state capacity saturation (entropy flooding forces silent forgetting). (3) 14 MITRE ATLAS technique extensions across the full tactic chain. (4) Six-profile attacker taxonomy with kill chains for genomics, clinical, and cybersecurity domains. (5) Four cognitive risk hypotheses grounded in state-compression mechanics. (6) Governance-aligned mitigations mapped to CREST, NIST AI 600-1, and EU AI Act. (7) Empirical evaluation: targeted genomic injection achieves $\mathrm{StIV}=0.519$ vs. $0.086$ random ($6.0\times$, $p<0.001$); PGD state injection achieves $156\times$ output perturbation over random; SSD-structured extraction confirmed at $O(N^2)$ vs. $O(N^3)$ query complexity ($N\times$ speedup). Validation on pretrained checkpoints is detailed in the Appendix.
