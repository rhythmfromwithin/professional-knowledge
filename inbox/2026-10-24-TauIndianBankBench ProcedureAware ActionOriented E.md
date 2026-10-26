---
interest: medium
link: https://arxiv.org/abs/2610.30161
next_step: skim
priority: high
slack_ts: '1792988477.151879'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'TauIndianBankBench: Procedure-Aware, Action-Oriented Evaluation of Tool-Using
  Conversational Agents'
---
# TauIndianBankBench: Procedure-Aware, Action-Oriented Evaluation of Tool-Using Conversational Agents
> 原文: [https://arxiv.org/abs/2610.30161](https://arxiv.org/abs/2610.30161)

arXiv:2610.30161v1 Announce Type: new
Abstract: Many Indian banks serve customers through FAQ pages and scripted chatbots. Assistants based on language models could respond faster and carry out requests such as blocking a card, but only if they give correct information and follow the bank's rules. These rules prescribe a procedure, a set of required steps, such as obtaining a closure quote before closing a deposit. Adapting models to this domain requires measuring how well they follow the procedure, before and after training. Benchmarks usually judge only the records left at the end of a conversation. Many required steps, however, leave the records unchanged, so an assistant that skips them can still be judged successful. We present TauIndianBankBench, an action-oriented benchmark of 1,000 Indian retail-banking tasks where an assistant helps a simulated customer. Besides the final records, it checks that the assistant took every required step and made no unrequested change. For every model, 6.5-12.0% of sessions are judged successful when only the final records are checked, although the assistant skipped a required step or made an unrequested change. Scoring both procedure and outcome shows more accurately how well language models perform in Indian retail banking.
