---
interest: medium
link: https://arxiv.org/abs/2608.05399
next_step: skim
priority: low
slack_ts: '1786154729.420089'
source: cs.SE - Software Engineering
status: unread
title: 'Improving Debugging in Verification-Aware Languages Through Automated Fault
  Localization: A Case Study in Dafny'
---
# Improving Debugging in Verification-Aware Languages Through Automated Fault Localization: A Case Study in Dafny
> 原文: [https://arxiv.org/abs/2608.05399](https://arxiv.org/abs/2608.05399)

arXiv:2608.05399v1 Announce Type: new
Abstract: Verification-aware languages, like Dafny, integrate formal specifications directly into source code to enable static correctness checks. However, when verification fails, the feedback provided is often limited to the specific condition of the error, such as a violated postcondition, rather than the root cause of the fault. While Dafny's counterexample features provide concrete execution traces, these typically expose a single failing path per assertion failure, leaving the developer to manually look through the entire trace to locate the error.
This paper investigates automated fault localization for verification-aware languages by comparing two paradigms: state-based and counterexample-based localization. Our state-based localization strategy replicates the ``snapshot'' methodology of AutoFix by inferring invariants and predicates to identify suspicious program states. The counterexample-based strategy consists of a family of techniques that progressively enrich the use of verifier output: from raw counterexample extraction, to structured single-trace ranking, and to multi-trace aggregation.
To validate these methods, we present an evaluation framework using MutDafny to generate a diverse mutant dataset from DafnyBench and measure localization effectiveness using the EXAM score. Our results show that counterexample-based approaches substantially outperform state-based localization in this setting. Structured ranking over a single trace yields the largest improvement over raw counterexample output, while multi-trace aggregation provides additional gains in robustness and debugging utility by increasing coverage and reducing path bias introduced by the solver. These findings demonstrate that effective fault localization in verification-aware languages depends both on using counterexample information, and how that information is structured and diversified.
