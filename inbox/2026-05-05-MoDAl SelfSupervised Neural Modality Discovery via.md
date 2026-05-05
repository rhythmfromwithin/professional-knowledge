---
interest: medium
link: https://arxiv.org/abs/2605.00025
next_step: skim
priority: low
slack_ts: '1777952331.002079'
source: q-bio.NC - Neurons and Cognition
status: unread
title: 'MoDAl: Self-Supervised Neural Modality Discovery via Decorrelation for Speech
  Neuroprosthesis'
---
# MoDAl: Self-Supervised Neural Modality Discovery via Decorrelation for Speech Neuroprosthesis
> 原文: [https://arxiv.org/abs/2605.00025](https://arxiv.org/abs/2605.00025)

arXiv:2605.00025v1 Announce Type: new
Abstract: Speech neuroprosthesis systems decode intended speech from neural activity in the absence of audible output, offering a path to restoring communication for individuals with speech-impairing conditions. Current approaches decode predominantly from motor cortical areas, discarding others -- such as area 44, part of Broca's area -- that may encode complementary linguistic information. We introduce MoDAl (Modality Decorrelation and Alignment), a framework that discovers complementary neural modalities through the interplay of two objectives in a shared projection space. A contrastive loss aligns each of several parallel brain encoders with the text embeddings of a pretrained large language model (LLM), while a decorrelation loss prevents the encoders from coalescing to duplicative representations. We prove that these objectives are in productive tension: Contrastive alignment induces transitive modality coalescence, which decorrelation must counteract for the framework to discover diverse neurolinguistic modalities. On the Brain-to-Text Benchmark '24, MoDAl reduces word error rate (WER) from 26.3% to 21.6% compared to the previous best end-to-end method, with the gain from incorporating previously discarded area 44 signals arising entirely from the decorrelation mechanism. Analysis of the discovered modalities reveals functional specialization: Encoders receiving area 44 input capture structural and syntactic properties (sentence length, grammatical voice, wh-words), consistent with the neurolinguistic understanding of Broca's area.
