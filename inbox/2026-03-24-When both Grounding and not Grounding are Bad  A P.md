---
title: "When both Grounding and not Grounding are Bad -- A Partially Grounded Encoding of Planning into SAT (Extended Version)"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2603.19429
priority: high
status: unread
interest: medium
next_step: skim
---
# When both Grounding and not Grounding are Bad -- A Partially Grounded Encoding of Planning into SAT (Extended Version)
> 原文: [https://arxiv.org/abs/2603.19429](https://arxiv.org/abs/2603.19429)

arXiv:2603.19429v1 Announce Type: new
Abstract: Classical planning problems are typically defined using lifted first-order representations, which offer compactness and generality. While most planners ground these representations to simplify reasoning, this can cause an exponential blowup in size. Recent approaches instead operate directly on the lifted level to avoid full grounding. We explore a middle ground between fully lifted and fully grounded planning by introducing three SAT encodings that keep actions lifted while partially grounding predicates. Unlike previous SAT encodings, which scale quadratically with plan length, our approach scales linearly, enabling better performance on longer plans. Empirically, our best encoding outperforms the state of the art in length-optimal planning on hard-to-ground domains.
