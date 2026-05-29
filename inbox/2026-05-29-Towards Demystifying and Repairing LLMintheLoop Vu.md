---
interest: medium
link: https://arxiv.org/abs/2605.28893
next_step: skim
priority: low
slack_ts: '1780028410.268409'
source: cs.SE - Software Engineering
status: unread
title: Towards Demystifying and Repairing LLM-in-the-Loop Vulnerabilities
---
# Towards Demystifying and Repairing LLM-in-the-Loop Vulnerabilities
> 原文: [https://arxiv.org/abs/2605.28893](https://arxiv.org/abs/2605.28893)

arXiv:2605.28893v1 Announce Type: new
Abstract: Large Language Models(LLMs) have been actively integrated into modern software systems as critical components. LLM-in-the-loop vulnerabilities, where vulnerabilities are introduced by LLMs and their dependent downstream components, such as frameworks, introduce new risks. Although some benchmark datasets have been constructed to study the impact of such vulnerabilities, most works still remain at the analysis from the conventional software level, ignoring the harm actually caused by LLMs. Understanding real-world LLM-in-the-loop vulnerabilities is still an open problem. To address this gap, we build the first LLM-in-the-loop vulnerability dataset, LLMCVE, to facilitate the risk analysis of LLM-integrated software. To do so, we first collect 2,888 multi-source vulnerabilities across 230 popular LLM components. Then, through manual analysis, we identify 205 vulnerabilities that strictly fall under the concept of LLM-in-the-loop vulnerability. Through analysis, we found that LLMs more often play as targets or propagation vectors rather than the root cause of these vulnerabilities. Furthermore, based on LLMCVE, we evaluate the repairing capabilities of existing agent-based vulnerability repair methods, such as SWE-Agent. Experimental results demonstrate that compared to conventional software vulnerabilities, LLM-in-the-Loop vulnerabilities are more challenging to precisely fix, especially for those involving prompt injections where the Pass@1 rate is only 28.57%.
