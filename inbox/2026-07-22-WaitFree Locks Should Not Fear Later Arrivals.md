---
interest: medium
link: https://arxiv.org/abs/2607.16571
next_step: skim
priority: medium
slack_ts: '1784863624.851709'
source: cs.DC - Distributed Computing
status: unread
title: Wait-Free Locks Should Not Fear Later Arrivals
---
# Wait-Free Locks Should Not Fear Later Arrivals
> 原文: [https://arxiv.org/abs/2607.16571](https://arxiv.org/abs/2607.16571)

arXiv:2607.16571v1 Announce Type: new
Abstract: Helping seems to make a lock wait-free: wrap the critical section in an idempotent thunk that any process can finish once the holder stalls. Yet helping protects the system, not the call. An overwritable candidate lets later requests bump one another in sequence, so a call can be forced to help newcomer after newcomer and never return, while point contention never exceeds two.
We ask whether a call can instead be charged only for the requests active when it takes its ticket, never for what arrives afterward. We show that the answer is yes. SeniorLock is a deterministic helpable thunk lock in which a call with ticket-time seniority $\beta$ finishes in $O((\beta+1)(T+1))$ local shared-memory steps, where $T$ bounds one thunk's cost, independently of later invocations. We call this guarantee \emph{retrospective wait-freedom}.
The same lock doubles as a universal construction we call SeniorObj: it turns any deterministic sequential object whose operations are bounded, concurrently idempotent thunks into a retrospective wait-free one, with no copying of its representation and, when no senior is active, at essentially the native cost of the operation.
