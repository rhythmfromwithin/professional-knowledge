---
interest: medium
link: https://arxiv.org/abs/2609.38223
next_step: skim
priority: low
slack_ts: '1790832433.771029'
source: cs.CR - Cryptography and Security
status: unread
title: 'CATP: Design and Evaluation of Local Agent Authorization and Audit Evidence'
---
# CATP: Design and Evaluation of Local Agent Authorization and Audit Evidence
> 原文: [https://arxiv.org/abs/2609.38223](https://arxiv.org/abs/2609.38223)

arXiv:2609.38223v1 Announce Type: new
Abstract: A signed authorization record authenticates what a signer asserted, but does not by itself establish that the assertion agrees with the policy and action used for a runtime decision. CATP specifies the bindings needed to carry a local pre-execution decision into offline-verifiable evidence. Its hook commits to the enforcement-time policy and adapter-normalized action and durably records the decision before returning permission. A later receipt binds the record to a self-contained audit export.
An implementation for Claude Code and Codex supports an empirical examination of these bindings. Controlled, validly signed counterexamples expose five missing consistency checks; adding them changes acceptance on the same inputs, with all 13 expected outcomes satisfied. A separate probe finds that distinct argument vectors can become the same normalized action before hashing, limiting what even a consistent receipt can establish. Eight scripted runtime cases verify hook delivery and allow/deny behavior; failure tests cover tampering, substitution, replay, concurrency and persistence errors. Median paired hook overhead is approximately 85 ms, and offline verification takes approximately 174 ms end to end on the testbed. The evidence remains conditional on a trusted runtime, monitor, host and signing key. It authenticates a decision about the normalized action, without proving execution truth, complete disclosure or autonomous task utility. The optional Groth16 study covers a narrower circuit predicate; the evaluation does not establish superiority over other systems.
