---
title: "The Identity Trap in EEG Foundation Models: A Diagnostic Audit"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2606.06647
priority: low
status: unread
interest: medium
next_step: skim
---
# The Identity Trap in EEG Foundation Models: A Diagnostic Audit
> 原文: [https://arxiv.org/abs/2606.06647](https://arxiv.org/abs/2606.06647)

arXiv:2606.06647v1 Announce Type: cross
Abstract: Objective. EEG foundation models (FMs) report strong accuracy on clinical resting-state EEG. However, high accuracy under subject-disjoint cross-validation remains ambiguous: it can reflect a genuine clinical biomarker, or subject-identity features that correlate with the label. We name this the Identity Trap and ask whether it can be diagnosed at the representation level before fine-tuning.
Approach. We propose FMScope, a frozen-representation protocol packaging five diagnostics: variance decomposition, subject-axis erasure, aperiodic 1/f ablation, layer-wise label probing, and within-subject direction consistency. We apply it to three pretrained FMs (LaBraM, CBraMod, REVE) across four datasets in a 2x2 layout: subject relation of label x presence of a consensus cross-subject EEG marker.
Main results. (i) The Identity Trap is universal: frozen subject-variance is 13-89x a random null in 12/12 pairs, rising in all 12 under fine-tuning (+10 to +63 pp). This dominance is a removable linear axis: erasing it improves label decoding where the label varies within subject (+6 to +12 pp in primary cells; +4 to +27 pp across external cohorts). (ii) Aperiodic 1/f is one subject carrier: removing it drops the subject probe by 9-19 pp on LaBraM and CBraMod. REVE saturates subject identity without measurable aperiodic dependence. (iii) Fine-tuning amplifies label-variance only in cells with a literature-established cross-subject marker.
Significance. The Identity Trap is a physically-grounded instance of shortcut learning: the preferred cue has a measurable physiological component, and subject-disjoint splitting alone cannot rule it out. FMScope separates gains reflecting a biological marker from those reflecting subject identity.
