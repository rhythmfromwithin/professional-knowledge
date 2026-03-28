---
interest: medium
link: https://arxiv.org/abs/2603.22447
next_step: skim
priority: low
slack_ts: '1774666201.813879'
source: cs.SE - Software Engineering
status: unread
title: 'SkillClone: Multi-Modal Clone Detection and Clone Propagation Analysis in
  the Agent Skill Ecosystem'
---
# SkillClone: Multi-Modal Clone Detection and Clone Propagation Analysis in the Agent Skill Ecosystem
> 原文: [https://arxiv.org/abs/2603.22447](https://arxiv.org/abs/2603.22447)

arXiv:2603.22447v1 Announce Type: new
Abstract: Agent skills are modular instruction packages that combine YAML metadata, natural language instructions, and embedded code, and they have reached 196K publicly available instances, yet no mechanism exists to detect clone relationships among them. This gap creates systemic risks: a vulnerability in a widely copied skill silently persists across derivatives with no alert to maintainers. Existing clone detectors, designed for single-modality source code, cannot handle the multi-modal structure of skills, where clone evidence is distributed across three interleaved content channels. We present SkillClone, the first multi-modal clone detection approach for agent skills. SkillClone fuses flat TF-IDF similarity with per-channel decomposition (YAML, NL, code) through logistic regression, combining strong detection with interpretable type classification. We construct SkillClone-Bench, a balanced benchmark of 300 ground-truth pairs with stratified difficulty. On SkillClone-Bench, SkillClone achieves F1 of 0.939 with precision 0.952, outperforming flat TF-IDF (F1 = 0.881) and achieving 4.2x higher Type-4 (semantic) recall than MinHash. Applying SkillClone to 20K skills reveals 258K clone pairs involving 75% of all skills, with 40% crossing author boundaries. A deduplication analysis shows the ecosystem is inflated 3.5x: only 5,642 unique skill concepts underlie the 20K listed skills, and 41% of skills in clone families are superseded by a strictly better variant.
