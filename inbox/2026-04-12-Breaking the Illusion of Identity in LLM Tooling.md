---
interest: medium
link: https://arxiv.org/abs/2604.07398
next_step: skim
priority: low
slack_ts: '1776051540.616419'
source: cs.SE - Software Engineering
status: unread
title: Breaking the Illusion of Identity in LLM Tooling
---
# Breaking the Illusion of Identity in LLM Tooling
> 原文: [https://arxiv.org/abs/2604.07398](https://arxiv.org/abs/2604.07398)

arXiv:2604.07398v1 Announce Type: new
Abstract: Large language models (LLMs) in research and development toolchains produce output that triggers attribution of agency and understanding -- a cognitive illusion that degrades verification behavior and trust calibration. No existing mitigation provides a systematic, deployable constraint set for output register. This paper proposes seven output-side rules, each targeting a documented linguistic mechanism, and validates them empirically. In 780 two-turn conversations (constrained vs. default register, 30 tasks, 13 replicates, 1560 API calls), anthropomorphic markers dropped from 1233 to 33 (>97% reduction, p < 0.001), outputs were 49% shorter by word count, and adapted AnthroScore confirmed the shift toward machine register (-1.94 vs. -0.96, p < 0.001). The rules are implemented as a configuration-file system prompt requiring no model modification; validation uses a single model (Claude Sonnet 4). Output quality under the constrained register was not evaluated. The mechanism is extensible to other domains.
