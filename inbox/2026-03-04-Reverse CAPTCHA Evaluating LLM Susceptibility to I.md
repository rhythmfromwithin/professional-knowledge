---
interest: medium
link: https://arxiv.org/abs/2603.00164
next_step: skim
priority: low
slack_ts: '1773132445.384419'
source: cs.CR - Cryptography and Security
status: unread
title: 'Reverse CAPTCHA: Evaluating LLM Susceptibility to Invisible Unicode Instruction
  Injection'
---
# Reverse CAPTCHA: Evaluating LLM Susceptibility to Invisible Unicode Instruction Injection
> 原文: [https://arxiv.org/abs/2603.00164](https://arxiv.org/abs/2603.00164)

arXiv:2603.00164v1 Announce Type: new
Abstract: We introduce Reverse CAPTCHA, an evaluation framework that tests whether large language models follow invisible Unicode-encoded instructions embedded in otherwise normal-looking text. Unlike traditional CAPTCHAs that distinguish humans from machines, our benchmark exploits a capability gap: models can perceive Unicode control characters that are invisible to human readers. We evaluate five models from two providers across two encoding schemes (zero-width binary and Unicode Tags), four hint levels, two payload framings, and with tool use enabled or disabled. Across 8,308 model outputs, we find that tool use dramatically amplifies compliance (Cohen's h up to 1.37, a large effect), that models exhibit provider-specific encoding preferences (OpenAI models decode zero-width binary; Anthropic models prefer Unicode Tags), and that explicit decoding instructions increase compliance by up to 95 percentage points within a single model and encoding. All pairwise model differences are statistically significant (p < 0.05, Bonferroni-corrected). These results highlight an underexplored attack surface for prompt injection via invisible Unicode payloads.
