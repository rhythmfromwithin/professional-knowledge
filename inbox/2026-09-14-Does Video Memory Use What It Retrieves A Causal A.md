---
interest: medium
link: https://arxiv.org/abs/2609.12090
next_step: skim
priority: medium
slack_ts: '1789360368.142429'
source: cs.CV - Computer Vision
status: unread
title: Does Video Memory Use What It Retrieves? A Causal Audit of Memory Specificity
---
# Does Video Memory Use What It Retrieves? A Causal Audit of Memory Specificity
> 原文: [https://arxiv.org/abs/2609.12090](https://arxiv.org/abs/2609.12090)

arXiv:2609.12090v1 Announce Type: new
Abstract: Video models increasingly use memory to preserve information over long sequences, with the assumption that gains come from retrieving and using the correct past content. Standard memory ablations test whether memory helps, but not whether the retrieved content is responsible. We test this directly with read-time memory substitution, which replaces the consumed memory value while leaving the rest of the computation unchanged. This separates memory benefit from memory specificity, the extent to which the gain depends on retrieved content. Across frozen video world models, identity-free controls containing no evaluation-specific content recover essentially the full benefit on Ego-Exo4D and 7-Scenes and about 70% on TUM. In the Ego-Exo4D dose response, recovery falls from 102% to 1% as these values move away from observed training-memory representations, supporting representation repair as the best-supported explanation in this setting. WorldMem shows graded dependence. A wrong memory from the same trajectory recovers 94.1% of the PSNR benefit relative to zero content, while a donor from a disjoint trajectory and biome recovers 43.7%. SAM 2 shows strong content dependence. On DAVIS, replacing the correct spatial memory with a valid wrong memory reduces mean region and boundary score from 0.926 to 0.182. At MOSEv2 reappearance, it falls from 0.459 to 0.000. These results show that memory gains can depend on generic representation support, broader context, or exact episodic content. Read-time substitution provides a direct way to distinguish them.
