---
interest: medium
link: https://arxiv.org/abs/2607.01409
next_step: skim
priority: low
slack_ts: '1783136963.654369'
source: cs.SE - Software Engineering
status: unread
title: 'GPUAlert: A Zero-Instrumentation Process-Boundary Monitor for Diagnosing GPU
  Training-Job Failures'
---
# GPUAlert: A Zero-Instrumentation Process-Boundary Monitor for Diagnosing GPU Training-Job Failures
> 原文: [https://arxiv.org/abs/2607.01409](https://arxiv.org/abs/2607.01409)

arXiv:2607.01409v1 Announce Type: new
Abstract: GPU training jobs fail often, roughly two in five on large production clusters, yet the operator typically learns of a failure only by reconnecting hours later. Experiment trackers require editing the training script and maintaining a cloud connection; the scheduler's mail hook delivers a single status line with no cause and no logs. GPUAlert is a command-line wrapper that monitors any training command at the process boundary, and with no change to that command, emails a structured notification on completion carrying a classified failure cause, durable logs, and output artifacts. The tool is organized around three reliability primitives: a pre-launch log guarantee that establishes the durable destination before the child process can crash, notifier isolation that makes the wrapper's exit code a pure function of the child's status regardless of whether the email succeeds, and a non-silent artifact budget that bounds attachment size without ever dropping output silently. We release a labelled corpus of 474 GPU training logs across 15 failure classes and a reproducible evaluation harness. On the twelve hardware-reproduced classes, the ordered-rule classifier reaches 0.997 macro-F1, against 0.830 for unordered keyword matching and 0.133 for exit-code inspection. Wrapper overhead is a constant approximately 3ms per job; the pre-launch guarantee preserves a log where a shell redirect yields nothing; and across all 15 failure modes the wrapper returns the child's exit code unchanged even when the SMTP relay is unreachable.
