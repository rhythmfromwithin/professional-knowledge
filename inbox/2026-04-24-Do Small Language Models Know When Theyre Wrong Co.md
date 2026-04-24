---
title: "Do Small Language Models Know When They're Wrong? Confidence-Based Cascade Scoring for Educational Assessment"
source: "cs.CY - Computers and Society"
link: https://arxiv.org/abs/2604.19781
priority: medium
status: unread
interest: medium
next_step: skim
---
# Do Small Language Models Know When They're Wrong? Confidence-Based Cascade Scoring for Educational Assessment
> 原文: [https://arxiv.org/abs/2604.19781](https://arxiv.org/abs/2604.19781)

arXiv:2604.19781v1 Announce Type: new
Abstract: Automated scoring of student work at scale requires balancing accuracy against cost and latency. In "cascade" systems, small language models (LMs) handle easier scoring tasks while escalating harder ones to larger LMs -- but the challenge is determining which cases to escalate. We explore verbalized confidence -- asking the LM to state a numerical confidence alongside its prediction -- as a routing signal. Using 2,100 expert-scored decisions from student-AI math conversations, we evaluate cascade systems built from GPT-5.4, Claude 4.5+, and Gemini 3.1 model pairs. We find that: (1) confidence discrimination varies widely across small LMs, with the best achieving AUROC 0.857 and the worst producing a near-degenerate confidence distribution; (2) confidence tracks human scoring difficulty, with lower LM confidence where annotators disagreed and took longer to score; (3) the best cascade approached large-LM accuracy (kappa 0.802 vs. 0.819) at 76% lower cost and 61% lower latency. Confidence discrimination is the bottleneck: the two small LMs with meaningful confidence variance yielded cascades with no statistically detectable kappa loss, while the third -- whose confidence was near-degenerate -- could not close the accuracy gap regardless of threshold. Small LMs with strong discrimination let practitioners trade cost for accuracy along the frontier; those without it do not.
