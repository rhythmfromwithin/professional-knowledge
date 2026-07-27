---
interest: medium
link: https://arxiv.org/abs/2607.20792
next_step: skim
priority: low
slack_ts: '1785124088.089529'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Memoir: Should a Model Write to Its Memory While It Thinks?'
---
# Memoir: Should a Model Write to Its Memory While It Thinks?
> 原文: [https://arxiv.org/abs/2607.20792](https://arxiv.org/abs/2607.20792)

arXiv:2607.20792v1 Announce Type: cross
Abstract: Memoir combines per-sample fast memory, shared slow parameters, variable-depth latent recurrence, and a future-latent energy objective. We test its riskiest coupling: each pondering iteration may rewrite the fast tier that the same iteration reads. On procedural associative recall with key interference, we compare a coupled arm against an otherwise identical read-only pondering arm. Both arms contain 81,738 parameters, including 76,362 trainable parameters, and use matched declared forward multiply-accumulate counts, data, optimizer, schedule, and seeds. After 240 training steps across 12 seeds, coupled recall is 0.5203 with a 95 percent interval of [0.4522, 0.5883], while read-only recall is 0.6557 with [0.5953, 0.7160]. The arms are paired per seed, and the read-only lead of 0.1354 gives a paired t of 3.23 on 11 degrees of freedom with a 95 percent interval of [0.0431, 0.2277] on the difference, winning on 10 of 12 seeds. After 960 steps across 8 seeds, both arms reach 1.0000, so the measured effect is a learning-speed penalty at a fixed budget, not a demonstrated capability penalty. That longer control is ceiling limited, leaving convergence on a non-saturating task unmeasured. A predicted failure in which memory rewriting corrupts the energy signal did not occur: the energy margin grew and held. Kernel restructuring also reduced delta-rule forward time from 0.907 ms to 0.351 ms on the stated device. Code and evidence are available at https://github.com/RightNow-AI/Memoir
