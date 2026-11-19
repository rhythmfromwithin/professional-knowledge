---
title: "ETA: Exit on Tool Arrival in Speculative Agent Loops"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2611.23239
priority: low
status: unread
interest: medium
next_step: skim
---
# ETA: Exit on Tool Arrival in Speculative Agent Loops
> 原文: [https://arxiv.org/abs/2611.23239](https://arxiv.org/abs/2611.23239)

arXiv:2611.23239v1 Announce Type: new
Abstract: Tool-using language agents in explicit thinking modes generate long chains of thought before acting, making each turn inherently serial: later tokens depend on the tool observation. Recent speculative tool dispatch methods overlap tool execution with reasoning, but offers limited benefit when reasoning dominates latency. We present ETA, that treats the speculative fork not as an actuator but as a sensor of the model's decision state, using it to terminate the reasoning of the main decode. It truncates reasoning only when the prediction is stable, agrees with the dispatched call, passes a free probe measuring whether a call will be emitted at all, and the tool result has arrived: a deadline that bounds per-turn regret by the remaining decode cost. ETA achieves speedups of 1.33x on tau2 airline/retail, 1.26x on tau2 telecom, and 1.13x on BFCL v4 multi-turn. On tau2, it decodes 24% fewer tokens at a nearly unchanged per-token rate without dropping action quality.
