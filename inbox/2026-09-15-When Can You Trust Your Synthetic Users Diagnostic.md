---
interest: medium
link: https://arxiv.org/abs/2609.13148
next_step: skim
priority: low
slack_ts: '1789532924.235799'
source: cs.HC - Human-Computer Interaction
status: unread
title: When Can You Trust Your Synthetic Users? Diagnostics and Corrections for LLM
  Consumer Panels
---
# When Can You Trust Your Synthetic Users? Diagnostics and Corrections for LLM Consumer Panels
> 原文: [https://arxiv.org/abs/2609.13148](https://arxiv.org/abs/2609.13148)

arXiv:2609.13148v1 Announce Type: new
Abstract: Large language models are increasingly deployed as synthetic consumer panels, promising $97\%$ cost reductions over traditional surveys. Yet aggregate validation metrics conceal systematic failures: variance compression, coefficient sign-flips, subgroup error balloons of 10--30 percentage points, and global corrections that worsen demographic bias. We provide a formal framework for deciding when to trust, correct, or abandon LLM-generated consumer data. The framework decomposes synthetic-panel bias into covariate and concept shift, develops testable diagnostics with interpretable decision thresholds, and supplies a doubly robust AIPW estimator requiring only a small calibration sample ($n = 50$-$300$). We validate on three testbeds. In controlled simulations the decision rule achieves $100\%$ accuracy (180/180 replications). On the American National Election Study with pre-existing LLM failures, it correctly flags heterogeneous concept shift and reduces naive bias by $92.9-99.6\%$. On the Twin-2K-500 consumer pricing dataset (172,884 paired human and GPT-4.1-mini responses), it correctly routes full-sample estimation to Trust and subgroup targeting to Correct, with $83-94\%$ bias reduction.
