---
interest: medium
link: https://arxiv.org/abs/2609.13407
next_step: skim
priority: low
slack_ts: '1789446774.935509'
source: cs.CR - Cryptography and Security
status: unread
title: Principled Detection of Coordinated Manipulation from Aggregate Distortion
  and Account Reuse
---
# Principled Detection of Coordinated Manipulation from Aggregate Distortion and Account Reuse
> 原文: [https://arxiv.org/abs/2609.13407](https://arxiv.org/abs/2609.13407)

arXiv:2609.13407v1 Announce Type: new
Abstract: Coordinated manipulation is collective: plausible accounts can jointly distort ratings, rankings, and engagement. Existing defenses primarily construct evidence from identities, graphs, content, or co-activity. We introduce an aggregate-first evidence layer that treats distortion of a context-level outcome distribution as the primary evidence object. The engine observes only a histogram, count, resolution, and reference distribution; identities are withheld until interval evidence is fixed. Because raw discrepancies have positive finite-sample expectation, we subtract a matched null expectation to obtain signed evidence and account for reference uncertainty. Participation logs then accumulate these fixed increments across accounts. We characterize matched-exposure divergence, bound self-influence, establish finite-horizon separation, and derive an exact linear reuse law for paired contexts.
We evaluate the mechanism with controlled rotation experiments and paired counterfactual interventions on historical Amazon review streams. Historical reviews provide the behavioral background; synthetic identities provide known coalition membership, and exact clean twins provide counterfactual controls. In a fixed-attack sweep against historical non-donor comparison accounts, reassigning the same manipulated events across identities with increasing reuse raises account-score ROC-AUC from 0.500 to 0.797. With activity- and exposure-matched clean twins, frequency is at chance while counterfactual attribution achieves ROC-AUC 0.744. Under a mean-preserving shape intervention, Wasserstein-1 and Jensen-Shannon evidence achieve ROC-AUC 0.909 and 0.967, while frequency and mean-based attribution remain at chance. Aggregate evidence complements repeated co-activity, improving mixed-mechanism ROC-AUC from 0.750 to 0.874 with a simple untrained combination.
