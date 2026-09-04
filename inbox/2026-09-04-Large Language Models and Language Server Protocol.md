---
title: "Large Language Models and Language Server Protocol: a match made in context"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2609.03086
priority: low
status: unread
interest: medium
next_step: skim
---
# Large Language Models and Language Server Protocol: a match made in context
> 原文: [https://arxiv.org/abs/2609.03086](https://arxiv.org/abs/2609.03086)

arXiv:2609.03086v1 Announce Type: new
Abstract: This article introduces Eiffel-tools, a language server protocol (LSP) implementation for the Eiffel programming language that uses Large Language Models (LLMs) to aid the development of statically verified software. The tool provides various interactive and non-interactive commands to produce code and specifications. It uses language and project specific knowledge to precisely direct the LLM and verifies the output using a static verifier. It crafts rich programmatic prompts for the input and corrects or rejects the output. Furthermore, it handles the retries until the program passes verification. The tool's bug fixing capability is evaluated on 2 public datasets using 3 models. The tool can fix 76% to 95% of bugs by combining LLMs and a formal verifier depending on the model and prompts used. The results show the trade-off between the number of fixing attempts and the success rate.
