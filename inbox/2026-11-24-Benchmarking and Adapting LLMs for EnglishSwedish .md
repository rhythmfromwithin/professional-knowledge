---
interest: medium
link: https://arxiv.org/abs/2611.28050
next_step: skim
priority: high
slack_ts: '1795512716.084529'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Benchmarking and Adapting LLMs for English-Swedish Medical Question Answering
---
# Benchmarking and Adapting LLMs for English-Swedish Medical Question Answering
> 原文: [https://arxiv.org/abs/2611.28050](https://arxiv.org/abs/2611.28050)

arXiv:2611.28050v1 Announce Type: new
Abstract: Large language models do well on English medical exams, but less is known about Swedish. This matters most for small open models that hospitals can run locally. To reduce this gap, we first build an item-aligned English-Swedish benchmark from ten medical multiple-choice datasets; each Swedish item keeps the options and answer of its English source. A conservative refinement loop repairs the translations: open models from three families find errors, ground them in a Swedish medical term base, and keep a model-written edit only if blind judges vote for it. On this benchmark, small models lose much more accuracy in Swedish than large ones, especially when they answer without reasoning. Second, we ask whether English data and open teacher models can close this gap. We translate the training data, let teachers write reasoning traces, and fine-tune two small students on gold answers or traces in English, Swedish, or both. Training on reasoning traces that include Swedish closes the gap and lifts the 1.2B student from 23.5\% to 52.0\% in Swedish, slightly above a 20B open model in its fast mode, with a sixth of its memory. We release the benchmark, its edit history, and the code.
