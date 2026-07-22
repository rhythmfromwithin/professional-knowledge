---
interest: medium
link: https://arxiv.org/abs/2607.15321
next_step: skim
priority: medium
slack_ts: '1784690755.032519'
source: cs.CV - Computer Vision
status: unread
title: 'Rethinking the Readout: Unlocking Video Backbones for AI-Generated Video Detection'
---
# Rethinking the Readout: Unlocking Video Backbones for AI-Generated Video Detection
> 原文: [https://arxiv.org/abs/2607.15321](https://arxiv.org/abs/2607.15321)

arXiv:2607.15321v1 Announce Type: new
Abstract: AI-generated videos (AIGVs) typically contain subtle temporal artifacts that arise from inter-frame inconsistencies rather than within individual frames. A detector that captures such artifacts should therefore benefit from video pretrained backbones over image only ones. In practice, however, video backbones with standard global readouts often fail to outperform strong image pretrained probes on AIGV benchmarks. We attribute this gap to excessive spatiotemporal aggregation in the readout. Video pretrained backbones tend to compress each frame into a single global descriptor. This compression suppresses local patch level temporal dynamics and discards inter patch relations, which are precisely the cues that AIGV detection most reliably depends on. Based on this, we propose Velocity Gated Patch Velocity Profiling (V-PVP), a lightweight readout that replaces only the aggregation layer with two parallel streams over the patch velocity field, adding only about $0.5$M trainable parameters. V-PVP serves as a general plug-and-play module that consistently improves performance across diverse video backbones under both end-to-end fine-tuning and linear probing settings. Our method reaches \textbf{95.28} AUC on AIGVDBench while keeping the backbone fully frozen. The results show that simply replacing the aggregation layer reactivates the temporal potential of frozen video backbones, restoring their advantage on AIGV detection. Code is available at https://anonymous.4open.science/r/PVP-81B3/.
