---
interest: medium
link: https://arxiv.org/abs/2606.04916
next_step: skim
priority: low
slack_ts: '1780718905.516839'
source: econ.GN - General Economics (AI Economics)
status: unread
title: 'Worker Utility as Hysteresis: A Preisach Model of Transaction Acceptance in
  Gig Labour Markets'
---
# Worker Utility as Hysteresis: A Preisach Model of Transaction Acceptance in Gig Labour Markets
> 原文: [https://arxiv.org/abs/2606.04916](https://arxiv.org/abs/2606.04916)

arXiv:2606.04916v1 Announce Type: cross
Abstract: Worker utility is not observed -- only its consequence is. Each gig transaction produces a single bit: accepted or rejected. We argue this structure points directly to the Preisach hysteresis model as the natural representation of latent worker preferences. The Preisach operator models aggregate output as an integral over a population of binary threshold elements -- precisely the structure that emerges when heterogeneous workers each carry a private acceptance wage. We estimate two latent utility surfaces: acceptance utility U\_1(X) and rejection utility U\_0(X), via a dual-output neural network (shared layers 256->128, margin loss enforcing U\_1 >= U\_0). Classification reduces to the Preisach gap U\_1(X) - U\_0(X), passed into an XGBoost classifier alongside clip-stabilised price-to-threshold encodings. On 36,891 gig transactions, this pipeline achieves Jaccard = 0.827 and ROC AUC = 0.799. The price-to-threshold encoding accounts for +11.0 pp AUC over raw utility features. The model confirms the directional asymmetry hysteresis predicts: price decreases depress completion rates more than equivalent increases raise them. Applied to the full dataset, the model's recommendations simultaneously reduce the total wage bill by 21.3% and increase expected fill rate by 9.7 pp. For 74.2% of transactions, P(accept) already exceeds 0.80; reducing the wage keeps it above threshold (mean post-cut P = 0.972), releasing cost savings (median 31%). For the remaining 25.4%, a median 7% wage increase recovers +43 pp acceptance. A model without an explicit indifference zone cannot execute both moves simultaneously.
