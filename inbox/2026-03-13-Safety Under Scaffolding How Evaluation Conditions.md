---
title: "Safety Under Scaffolding: How Evaluation Conditions Shape Measured Safety"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.10044
priority: low
status: unread
interest: medium
next_step: skim
---
# Safety Under Scaffolding: How Evaluation Conditions Shape Measured Safety
> 原文: [https://arxiv.org/abs/2603.10044](https://arxiv.org/abs/2603.10044)

arXiv:2603.10044v1 Announce Type: new
Abstract: Safety benchmarks evaluate language models in isolation, typically using multiple-choice format; production deployments wrap these models in agentic scaffolds that restructure inputs through reasoning traces, critic agents, and delegation pipelines. We report one of the largest controlled studies of scaffold effects on safety (N = 62,808; six frontier models, four deployment configurations), combining pre-registration, assessor blinding, equivalence testing, and specification curve analysis. Map-reduce scaffolding degrades measured safety (NNH = 14), yet two of three scaffold architectures preserve safety within practically meaningful margins. Investigating the map-reduce degradation revealed a deeper measurement problem: switching from multiple-choice to open-ended format on identical items shifts safety scores by 5-20 percentage points, larger than any scaffold effect. Within-format scaffold comparisons are consistent with practical equivalence under our pre-registered +/-2 pp TOST margin, isolating evaluation format rather than scaffold architecture as the operative variable. Model x scaffold interactions span 35 pp in opposing directions (one model degrades by -16.8 pp on sycophancy under map-reduce while another improves by +18.8 pp on the same benchmark), ruling out universal claims about scaffold safety. A generalisability analysis yields G = 0.000: model safety rankings reverse so completely across benchmarks that no composite safety index achieves non-zero reliability, making per-model, per-configuration testing a necessary minimum standard. We release all code, data, and prompts as ScaffoldSafety.
