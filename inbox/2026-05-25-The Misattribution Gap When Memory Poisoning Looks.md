---
title: "The Misattribution Gap: When Memory Poisoning Looks Like Model Failure in Agentic AI Systems"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.22842
priority: low
status: unread
interest: medium
next_step: skim
---
# The Misattribution Gap: When Memory Poisoning Looks Like Model Failure in Agentic AI Systems
> 原文: [https://arxiv.org/abs/2605.22842](https://arxiv.org/abs/2605.22842)

arXiv:2605.22842v1 Announce Type: new
Abstract: Multi-agent AI pipelines typically assume that agent misconduct originates from model misalignment. We identify a structural failure in this assumption, the \emph{Misattribution Gap}, where memory-layer attacks produce behaviors indistinguishable from model failure, causing defenders to apply the wrong remediation. We formalize \emph{Semantic Norm Drift} (SND) as a third path to agent misconduct, distinct from emergent misalignment and collusion. In SND, a policy-formatted document enters a shared vector store through normal uploads and later reappears as trusted system context after provenance is lost through a Trust Laundering Chain. Across 64 documented failures, attribution systems consistently blamed the model. Four safety classifiers, including one trained on memory poisoning, produced zero detections across 510 checkpoints. In 59 of 65 valid cases, agents explicitly cited the injected document as normative authority before complying. The attack requires no trigger, model access, or repeated interaction, achieves full effect within five sessions, and persists indefinitely. We introduce Counterfactual Composition Testing, which identifies the causal entry with 87.5% accuracy and zero false positives, while a forensics baseline fails across all 25 scenarios. We further prove the Retrieval-Coverage Dilemma, showing that stronger evasion inherently weakens the attack, limiting adaptive bypass strategies. Finally, we propose Memory-Persistent Information-Flow Control, which blocks 97% of attacks at the cross-session boundary where prior defenses fail. We release the SND Corpus, the first adversarial memory benchmark with temporal persistence and multi-agent composition across financial and Health Care domains.
