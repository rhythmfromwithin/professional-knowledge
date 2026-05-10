---
interest: medium
link: https://arxiv.org/abs/2605.04107
next_step: skim
priority: low
slack_ts: '1778385540.091169'
source: cs.SE - Software Engineering
status: unread
title: 'TSCG: Deterministic Tool-Schema Compilation for Agentic LLM Deployments'
---
# TSCG: Deterministic Tool-Schema Compilation for Agentic LLM Deployments
> 原文: [https://arxiv.org/abs/2605.04107](https://arxiv.org/abs/2605.04107)

arXiv:2605.04107v1 Announce Type: new
Abstract: Production agent frameworks (OpenAI Function Calling, Anthropic Tool Use, MCP) transmit tool schemas as JSON, a format designed for machine parsing, not for interpretation by language models. For small models (4B-14B), this protocol mismatch accounts for the majority of tool-use failure at production catalog sizes. We present TSCG, a deterministic tool-schema compiler that resolves this mismatch at the API boundary, converting JSON schemas into token-efficient structured text without model access, fine-tuning, or runtime search. TSCG combines eight composable operators with a formal compression bound (>=51% on well-formed schemas).
On TSCG-Agentic-Bench (about 19,000 calls, 12 models, 5 scenarios), TSCG restores Phi-4 14B from 0% to 84.4% accuracy at 20 tools (90.3% at 50 tools) and achieves 108-181% accuracy-retained ratio across three models on BFCL. Format-versus-compression decomposition (R^2=0.88 -> 0.03) establishes representation change as the dominant mechanism. Per-operator isolation across three frontier models reveals three distinct operator-response profiles: operator-hungry (Opus 4.7), operator-sensitive (GPT-5.2), and operator-robust (Sonnet 4), providing per-model deployment guidance. Scaling experiments show accuracy advantages persisting on heavy production MCP schemas (+5.0 pp at about 10,500 input tokens) despite saturation on light synthetic catalogs, with 52-57% token savings throughout. The synthetic benchmark generalizes to real MCP schemas within 0.1 accuracy points. TSCG ships as a 1,200-line zero-dependency TypeScript package.
