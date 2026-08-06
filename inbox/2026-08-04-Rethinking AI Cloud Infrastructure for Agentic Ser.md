---
interest: medium
link: https://arxiv.org/abs/2607.29069
next_step: skim
priority: medium
slack_ts: '1785986406.734979'
source: cs.DC - Distributed Computing
status: unread
title: Rethinking AI Cloud Infrastructure for Agentic Serving Systems with the Aries
  Experimentation Framework
---
# Rethinking AI Cloud Infrastructure for Agentic Serving Systems with the Aries Experimentation Framework
> 原文: [https://arxiv.org/abs/2607.29069](https://arxiv.org/abs/2607.29069)

arXiv:2607.29069v1 Announce Type: new
Abstract: Autonomous agents challenge conventional LLM serving by coupling repeated inference with persistent context and sandboxed tool execution. We present Aries, a full-stack experimentation framework that separates task semantics from execution configurations, reconstructs cross-component agent trajectories with correlated system telemetry, and exposes stateful tool execution through a consistent interface across heterogeneous sandbox substrates. We use Aries to conduct reproducible experiments on open agent harnesses and benchmarks. We complement these experiments with production traces from a commercial platform, grounding low-level systems research in observed production behavior. Our results show that (1) token-centric metrics miss non-inference bottlenecks, (2) retaining additional context yields diminishing accuracy benefits while reducing serving capacity, and (3) tool sandboxes alternate between long idle periods and short resource bursts, while current snapshot-based state management makes aggressive suspension costly. A complementary security analysis further highlights the need to reduce the sandbox attack surface. We then discuss the vision for agent-native serving systems designed around trajectory-level metrics, adaptive context management, elastic sandbox resource management, and sandboxes with minimized attack surface.
