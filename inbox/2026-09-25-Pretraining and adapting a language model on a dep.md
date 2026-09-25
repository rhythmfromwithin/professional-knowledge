---
title: "Pretraining and adapting a language model on a dependency-free stack: GPT-2 124M from random weights, reproduced against llm.c, and a clinical adapter for Qwen3-0.6B"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2609.28568
priority: low
status: unread
interest: medium
next_step: skim
---
# Pretraining and adapting a language model on a dependency-free stack: GPT-2 124M from random weights, reproduced against llm.c, and a clinical adapter for Qwen3-0.6B
> 原文: [https://arxiv.org/abs/2609.28568](https://arxiv.org/abs/2609.28568)

arXiv:2609.28568v1 Announce Type: new
Abstract: Almost every language model in service was trained by one family of software. That concentration makes a question hard to settle: how much of what is known about training a language model describes language models, and how much describes that software? Settling it needs a second implementation able to carry a model through a whole lifecycle rather than reproduce one operator.
We report such a lifecycle. Using numbat, a machine-learning stack written in Zig with no third-party runtime dependencies, we pretrain a 124.4 M-parameter GPT-2 from random initialisation over 9.91 B tokens of web text, then adapt a separate small model to clinical question answering. A reference implementation runs on identical hardware at both stages, and a sidecar with authority to halt a run supervises each.
Agreement is close. Held-out cross-entropy finishes at 3.2588 against a published 3.29, and HellaSwag at 0.3053 against 0.299; across 8 paired evaluations it sits below a same-machine reference at every point, by 0.0608 on average. Re-running that reference on different hardware moves it 0.0035, which bounds how much of any gap is method rather than framework. Throughput does not pay for agreement: measured in one session at a production configuration, numbat reaches 43,374 tokens per second against PyTorch's 41,202, scaling 2.769x over three cards. Clinical adaptation ends at 2.1899 held-out loss against 2.1941.
Neither model is a medical device, and neither is validated for clinical use.
