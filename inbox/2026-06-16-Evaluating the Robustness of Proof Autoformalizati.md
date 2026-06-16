---
interest: medium
link: https://arxiv.org/abs/2606.14867
next_step: skim
priority: high
slack_ts: '1781586968.423299'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Evaluating the Robustness of Proof Autoformalization in Lean 4
---
# Evaluating the Robustness of Proof Autoformalization in Lean 4
> 原文: [https://arxiv.org/abs/2606.14867](https://arxiv.org/abs/2606.14867)

arXiv:2606.14867v1 Announce Type: new
Abstract: Proof autoformalization aims to translate a mathematical informal proof written in natural language into a formal proof in a formal language such as Lean~4. Several works have developed LLM-based models for proof autoformalization. However, existing evaluations have typically focused on translating well-formed informal proofs from curated datasets. We argue that a robust proof autoformalizer must remain faithful even for informal proofs that diverge from these idealized ones, and we present the first study on the robustness of proof autoformalization models. We formulate two categories of perturbations and evaluate robustness under each: a global perturbation paraphrases the informal proof in a different style, under which the formalization should remain consistent; a local perturbation alters a value, symbol, or proof step, possibly in a counterfactual way, and a robust formalization should faithfully reflect the perturbation rather than reverting to the original one or inferring a different one on its own. We build a benchmark with both perturbations on miniF2F and MATH-500, and automatically measure how stable a proof autoformalization's correctness is under global perturbations and how faithfully its output reflects local perturbations. We evaluate seven recent models, all of which are sensitive to global perturbations and mostly fail to remain faithful under local perturbations. Code and data are available via https://github.com/ucr-rai/robust-proof-autoformalization.
