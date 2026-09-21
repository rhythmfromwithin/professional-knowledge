---
title: "Complex Problem Solving in Large Language Models: A Statistical Control Survey and Diagnostic Framework"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.20973
priority: medium
status: unread
interest: medium
next_step: skim
---
# Complex Problem Solving in Large Language Models: A Statistical Control Survey and Diagnostic Framework
> 原文: [https://arxiv.org/abs/2609.20973](https://arxiv.org/abs/2609.20973)

arXiv:2609.20973v1 Announce Type: new
Abstract: Complex problem solving (CPS) with large language models (LLMs) is often framed as a matter of stronger reasoning or longer generation. Yet early-step error amplification, prompt brittleness, and failures to revise incorrect commitments are difficult to explain by missing knowledge or expressive capacity alone. This survey interprets CPS as a sequential estimation-and-decision problem over a latent solution state. A controller maintains a belief about an unobserved solution trajectory, updates it as noisy intermediate evidence arrives, and decides whether to commit, verify, branch, roll back, or abstain to minimize expected loss. Reasoning supplies candidate transitions and interpretations, whereas process control shapes and evaluates those proposals and regulates subsequent transitions and observations. Within this framework, we organize existing methods around five components: explicit state representation, transition structuring, validation and constraint enforcement, search and rollback, and uncertainty management. We also interpret evaluation metrics according to the statistical quantities they estimate. The framework further yields a diagnostic hypothesis: interventions should be most effective when they target the error or uncertainty component implicated by an observed failure. We distinguish systematic, stochastic, and irreducible error together with epistemic and aleatoric uncertainty, and call this alignment problem-control fit and its failure control mismatch. For example, additional sampling may reduce sampling variability while leaving a shared systematic error unchanged. This perspective clarifies what current methods estimate and control, what remains uncontrolled, and why reliable validation, targeted recovery, calibrated uncertainty, and matched-budget evaluation are central open problems.
