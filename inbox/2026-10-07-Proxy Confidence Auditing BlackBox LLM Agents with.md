---
interest: medium
link: https://arxiv.org/abs/2610.03894
next_step: skim
priority: high
slack_ts: '1791524735.764339'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate''s Log-Probabilities'
---
# Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities
> 原文: [https://arxiv.org/abs/2610.03894](https://arxiv.org/abs/2610.03894)

arXiv:2610.03894v1 Announce Type: new
Abstract: A deployed LLM agent emits tool calls, queries, and code that can be silently wrong -- by the time the error surfaces, the action has run. Frontier chat APIs hide the model's token probabilities; the agent's stated confidence barely beats chance on the mistakes that matter; and resampling does not help, since frontier models are highly repetitive, reproducing the same call across samples.
We recover the missing signal from a low-cost open-weight surrogate run in parallel. It reads the same context, schema, and proposed action as the agent, then scores the call from its own log-probabilities through a family of complementary readouts: teacher forcing and request-PMI weigh the likelihood of each argument value, a discriminative verdict judges the call as a whole, and tool-choice competition tests the function against its siblings. One principle says which to trust: a generative likelihood localizes wrong argument values, while the verdict catches holistically wrong calls. When the error type is unknown, an ensemble is the low-regret default. The readout is training-free, needs no access to the agent's internals, and costs one prefill pass alongside the tool call.
On difficult coding tasks it reaches AUROC 0.825 where the actor's stated confidence is near chance (0.598), and the generative readouts beat it by +0.07 to +0.28 across three further actors. Against self-consistency it gains +0.14 to +0.19 on near-deterministic actors, at 1/K the cost. The signal drives two deployment modes: a real-time gate escalating the least-trustworthy calls for review (+0.05 to +0.30 accepted-action accuracy at 50% coverage), and confidence feedback, returning the tool result with the score so the agent adapts its next step -- lifting task success on live-execution benchmarks (+0.119 and +0.137, p <= 1e-4) and beating a random-value control where step errors are silent (+0.078, p = 0.003).
