---
interest: medium
link: https://arxiv.org/abs/2610.33094
next_step: skim
priority: low
slack_ts: '1793164455.000089'
source: cs.SE - Software Engineering
status: unread
title: 'Beyond Correctness: Attribution of Natural-Language Documentation for Formal
  Libraries'
---
# Beyond Correctness: Attribution of Natural-Language Documentation for Formal Libraries
> 原文: [https://arxiv.org/abs/2610.33094](https://arxiv.org/abs/2610.33094)

arXiv:2610.33094v1 Announce Type: new
Abstract: Formal languages are widely used in software engineering to specify and verify program properties. Because their mathematical notation and logic are hard to read, developers often rely on natural-language documentation to understand the functions in formal libraries. Yet a documentation statement can be provably true and still hold after the function's behavior changes. We call a statement's dependence on the function's specific behavior attribution, and we give a method to check it. We design and implement DocAuth, a documentation-generation method that uses attribution to decide what to publish and attaches to each published sentence the formal property recovered from it, together with checkable evidence. On 150 functions from the Community Books library of the ACL2 theorem prover, three large language models produce proved but non-attributable properties for about a third of the functions. DocAuth matches or exceeds the attribution rate of a mutation-based filter while delivering 37% more attributable sentences. Compared with a pipeline that checks truth alone, it raises the share of published sentences that a second model confirms as attributable from 82.9% to 94.7%. These results show that provable truth does not guarantee that documentation reflects what a function actually does. Attribution complements truth as a criterion for generating and evaluating documentation for formal libraries.
