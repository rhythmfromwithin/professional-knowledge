---
title: "Do Generative AI Assistants Respect robots.txt? Tracing Web Access Beyond Visible Answers"
source: "cs.CY - Computers and Society"
link: https://arxiv.org/abs/2607.14447
priority: medium
status: unread
interest: medium
next_step: skim
---
# Do Generative AI Assistants Respect robots.txt? Tracing Web Access Beyond Visible Answers
> 原文: [https://arxiv.org/abs/2607.14447](https://arxiv.org/abs/2607.14447)

arXiv:2607.14447v1 Announce Type: new
Abstract: AI assistants increasingly retrieve web content at inference time to provide fresh and grounded answers, yet it remains unclear whether these search-augmented capabilities respect website-owner restrictions expressed through robots.txt. We present a controlled empirical study of ten widely used AI assistants with advertised web-search capabilities. For each assistant, we first identify a configuration that actually produces observable web-browsing behavior and record the user-agent exposed during retrieval. We then evaluate compliance with controlled robots.txt rules across four complementary conditions: allowed for all user-agents, disallowed for all user-agents, allowed only for the assistant-specific user-agent, and disallowed only for that user-agent. Using server-side logs and secret codes embedded in target pages, we distinguish actual page access from user-visible answer correctness across 200 trials.
Our results show substantial variation across assistants. Some systems followed the expected allowed/disallowed access pattern, whereas others accessed restricted resources without requesting robots.txt or used generic user-agents that complicated attribution. We also find that retrieval behavior and answer correctness can diverge: assistants may access pages without surfacing the retrieved content, or fail to access even allowed resources. These findings raise broader legal and governance concerns about whether AI-assisted web access adequately respects content owners' rights and restrictions. Furthermore, our observations provide valuable insight into the growing erosion of traditional web governance protocols, highlighting the urgent need for updated, enforceable standards that guarantee publisher autonomy in the age of search-augmented AI assistants.
