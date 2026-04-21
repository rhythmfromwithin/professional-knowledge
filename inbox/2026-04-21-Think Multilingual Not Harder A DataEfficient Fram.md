---
title: "Think Multilingual, Not Harder: A Data-Efficient Framework for Teaching Reasoning Models to Code-Switch"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2604.15490
priority: high
status: unread
interest: medium
next_step: skim
---
# Think Multilingual, Not Harder: A Data-Efficient Framework for Teaching Reasoning Models to Code-Switch
> 原文: [https://arxiv.org/abs/2604.15490](https://arxiv.org/abs/2604.15490)

arXiv:2604.15490v1 Announce Type: new
Abstract: Recent developments in reasoning capabilities have enabled large language models to solve increasingly complex mathematical, symbolic, and logical tasks. Interestingly, while reasoning models are often trained to generate monolingual text, these models have also been observed to code-switch (i.e., mix languages). Prior works have either viewed code-switching as an undesirable error, attempted to control code-switching through modifications to input prompts or the output decoding process, or focus on narrow subsets of languages, domains, tasks, and models. We address these gaps by introducing the first linguistically and behaviorally motivated fine-tuning framework for identifying beneficial code-switched reasoning behaviors in large language models and teaching these models to code-switch more effectively for reasoning. First, we create and systematically analyze a dataset of reasoning traces from diverse models, languages, tasks, and domains to understand the types of code-switching behaviors found in existing reasoning models. Then, we develop fine-tuning interventions that teach reasoning models to code-switch based on our observations of helpful behaviors in existing models. We find that our framework can significantly increase beneficial code-switched reasoning behaviors in a data-efficient manner. Interestingly, we also find that code-switching behaviors in reasoning models can be modified by fine-tuning for tasks that do not directly demonstrate code-switching in reasoning (e.g., machine translation). Our work suggests that data-efficient interventions can instill helpful forms of code-switching behavior in reasoning models.
