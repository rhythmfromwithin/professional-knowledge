---
title: "GenoTrace: Inheritable Watermarks for Genome Foundation Model Distillation"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2609.35881
priority: low
status: unread
interest: medium
next_step: skim
---
# GenoTrace: Inheritable Watermarks for Genome Foundation Model Distillation
> 原文: [https://arxiv.org/abs/2609.35881](https://arxiv.org/abs/2609.35881)

arXiv:2609.35881v1 Announce Type: new
Abstract: Can a genome model retain a detectable record of the synthetic sequences used to train it? We study watermark inheritance through distillation with GenoTrace, a codon-aware extension of green-list watermarking. Two token-level factors modulate the teacher's generation bias using codon position and organism-specific codon usage. The resulting sequences train a smaller student, whose outputs are audited without an active watermark processor. In a three-seed GenomeOcean-500M-to-100M experiment, the joint configuration achieves a mean audit score of 17.88 and 94.5% detection at a fixed threshold. It retains 49.0% detection after key-aware token substitution, compared with 0% for the available single-seed plain-watermark comparator, and 47.0% after combined mechanism-targeted nucleotide edits. Additional experiments establish inherited signal across five organism-conditioned datasets and teacher-student size ratios up to 40. Component ablations and computational sequence-quality assays reveal distinct operating points for detection strength and coding coverage. GenoTrace provides a practical token-level construction and an empirical account of how genomic structure shapes inherited watermark signals. The findings concern shared-tokenizer distillation and the tested editing procedures, with calibration and biological utility treated as separate evaluation requirements.
