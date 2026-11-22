---
interest: medium
link: https://arxiv.org/abs/2611.24979
next_step: skim
priority: low
slack_ts: '1795328176.287829'
source: cs.SE - Software Engineering
status: unread
title: 'Trace2ST: Recovering PLC Structured Text from I/O Traces with LLM Generation
  and Verification'
---
# Trace2ST: Recovering PLC Structured Text from I/O Traces with LLM Generation and Verification
> 原文: [https://arxiv.org/abs/2611.24979](https://arxiv.org/abs/2611.24979)

arXiv:2611.24979v1 Announce Type: new
Abstract: Programmable logic controllers (PLCs), the industrial computers that operate power and process plants, often run programs whose source code is no longer available; however, every input and output of the controller is logged continuously. This paper therefore asks whether a large language model (LLM) can recover an executable program in Structured Text (ST), the standard PLC language of IEC 61131-3, from such input/output records (traces) alone and, equally important, how the recovered program can be verified. To answer this question, we build a generate-replay-feedback pipeline. First, the LLM writes a candidate program from a compressed summary of the trace, without ever seeing the original program. The candidate is then executed one control cycle (scan) at a time and compared with the recording, and whenever a mismatch occurs the corresponding part of the trace is returned to the LLM, for at most three revisions. Because every result depends on the software that executes the candidates, we first validate it against two independent open-source PLC runtimes and find no unexplained difference. On this basis, we evaluate 47 third-party programs from two public benchmarks. The recovered programs reproduce the recorded trace exactly in 43 cases and agree with the original on 94% of scans for unseen inputs. The remaining errors, however, lie mostly in program branches that the trace never exercised; once a trace that targets these branches is added, agreement on unseen adversarial inputs rises from 0.80 to 0.98. By contrast, a classical automata-learning baseline without an LLM fits the recording but falls to 0.40 on unseen inputs, which indicates that recovering program structure is the hard part. Finally, on real data from a public water-treatment testbed, the recovered control laws match unseen measurements closely ($R^2 > 0.99$) and expose the only actuator attack in the dataset.
