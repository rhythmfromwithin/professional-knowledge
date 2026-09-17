---
title: "Predictive Varanus: Combining CSP Conformance Monitoring with Predictive LTL Runtime Verification"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2609.17625
priority: medium
status: unread
interest: medium
next_step: skim
---
# Predictive Varanus: Combining CSP Conformance Monitoring with Predictive LTL Runtime Verification
> 原文: [https://arxiv.org/abs/2609.17625](https://arxiv.org/abs/2609.17625)

arXiv:2609.17625v1 Announce Type: new
Abstract: Runtime Verification is well suited to autonomous and robotic systems because it checks the behaviour that is actually observed during execution. Its main limitation, however, is that it is usually reactive: the monitor detects a violation only after the system has already performed a bad event. This can be too late in domains where failures are costly or unsafe. In this paper we present PREDICTIVE VARANUS, a two-stage verification pipeline that combines VARANUS, a runtime verifier that uses models written in the process algebra Communicating Sequential Processes (CSP), with predictive runtime verification for LTL. A CSP model is first used as a conformance gate over the observed event trace; the same model is then translated into a Buchi automaton that constrains the futures explored by a predictive LTL monitor. In this way, out-of-model behaviour is rejected immediately, while model-consistent prefixes can be classified as already guaranteeing satisfaction, already forcing violation, or still being inconclusive for the monitored temporal property. We formalise the combined monitor, explain its implementation, and illustrate the approach on a robotic rover for nuclear-store inspection. The case study shows how the combination of CSP validation and predictive LTL can provide earlier verdicts than standard runtime monitoring while reusing an existing design-time CSP model.
