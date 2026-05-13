---
interest: medium
link: https://arxiv.org/abs/2605.06832
next_step: skim
priority: high
slack_ts: '1778644943.006709'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'IntentGrasp: A Comprehensive Benchmark for Intent Understanding'
---
# IntentGrasp: A Comprehensive Benchmark for Intent Understanding
> 原文: [https://arxiv.org/abs/2605.06832](https://arxiv.org/abs/2605.06832)

arXiv:2605.06832v1 Announce Type: new
Abstract: Accurately understanding the intent behind speech, conversation, and writing is crucial to the development of helpful Large Language Model (LLM) assistants. This paper introduces IntentGrasp, a comprehensive benchmark for evaluating the intent understanding capability of LLMs. Derived from 49 high-quality, open-licensed corpora spanning 12 diverse domains, IntentGrasp is constructed through source datasets curation, intent label contextualization, and task format unification. IntentGrasp contains a large-scale training set of 262,759 instances and two evaluation sets: an All Set of 12,909 test cases and a more balanced and challenging Gem Set of 470 cases. Extensive evaluations on 20 LLMs across 7 families (including frontier models such as GPT-5.4, Gemini-3.1-Pro, and Claude-Opus-4.7) demonstrate unsatisfactory performance, with scores below 60% on All Set and below 25% on Gem set. Notably, 17 out of 20 tested models perform worse than a random-guess baseline (15.2%) on Gem Set, while the estimated human performance is ~81.1%, showing substantial room for improvement. To enhance such ability, this paper proposes Intentional Fine-Tuning (IFT), which fine-tunes the models on the training set in IntentGrasp, yielding significant gains of 30+ F1 points on All Set and 20+ points on Gem Set. Tellingly, the leave-one-domain-out (Lodo) experiments further demonstrate the strong cross-domain generalizability of IFT, verifying that it is a promising approach to substantially enhancing the intent understanding of LLMs. Overall, by benchmarking and boosting intent understanding ability, this study sheds light on a promising path towards more intentional, capable, and safe AI assistants for human benefits and social good.
