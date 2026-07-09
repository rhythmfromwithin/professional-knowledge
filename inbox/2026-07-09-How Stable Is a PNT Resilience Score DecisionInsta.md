---
title: "How Stable Is a PNT Resilience Score? Decision-Instability of Single-Number Resilience Ratings under Framework-Aligned Weighting"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2607.05415
priority: low
status: unread
interest: medium
next_step: skim
---
# How Stable Is a PNT Resilience Score? Decision-Instability of Single-Number Resilience Ratings under Framework-Aligned Weighting
> 原文: [https://arxiv.org/abs/2607.05415](https://arxiv.org/abs/2607.05415)

arXiv:2607.05415v1 Announce Type: new
Abstract: Authoritative positioning, navigation, and timing (PNT) resilience frameworks (the DHS Resilient PNT Conformance Framework, RPCF, and peers) define what resilience means but supply only self-attestation: a checklist or a maturity Level, with no engine and no measurement. We build the missing measurement layer as an open, deterministic scoring engine over a PNT simulator, emitting per-dimension sub-scores traceable to a scenario and an oracle, and ask whether a single composite score or maturity Level is a stable basis for a decision. Across seven architectures spanning cross-dimension tradeoffs, a Dirichlet simplex over the seven RPCF categories, and a five-threat ensemble, the answer splits in two. The composite winner is stable under active denial and under near-equal weightings (about 1 percent flip rate), so a single number is safe precisely where one design dominates; but re-weighting alone flips it in up to 22 percent of draws under nominal conditions, where designs contend, a known composite-indicator sensitivity. The sharper, weighting-invariant failure is categorical: a weakest-link maturity Level (our minimum-over-categories operationalization of the RPCF ladder, not the framework's rule) depends on the threat assumed, not the architecture, changing for one architecture in seven. Because the composite rewards declared techniques, a constructed single-band receiver declaring all seven outscores a more resilient system: self-attestation can be gamed by declaration. And apparent fourfold GNSS redundancy reduces, by the definition of a shared common-mode failure domain, to an effective diversity of one. Conclusions hold under +/-20 percent perturbation of every driver within the reduction. We report per-dimension sub-scores with provenance and a rank range, not a phantom single number. A self-assessment aligned to RPCF v2.0, not a certification.
