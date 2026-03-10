---
interest: medium
link: https://arxiv.org/abs/2602.23523
next_step: skim
priority: medium
slack_ts: '1773132408.344129'
source: cs.CV - Computer Vision
status: unread
title: 'All in One: Unifying Deepfake Detection, Tampering Localization, and Source
  Tracing with a Robust Landmark-Identity Watermark'
---
# All in One: Unifying Deepfake Detection, Tampering Localization, and Source Tracing with a Robust Landmark-Identity Watermark
> 原文: [https://arxiv.org/abs/2602.23523](https://arxiv.org/abs/2602.23523)

arXiv:2602.23523v1 Announce Type: new
Abstract: With the rapid advancement of deepfake technology, malicious face manipulations pose a significant threat to personal privacy and social security. However, existing proactive forensics methods typically treat deepfake detection, tampering localization, and source tracing as independent tasks, lacking a unified framework to address them jointly. To bridge this gap, we propose a unified proactive forensics framework that jointly addresses these three core tasks. Our core framework adopts an innovative 152-dimensional landmark-identity watermark termed LIDMark, which structurally interweaves facial landmarks with a unique source identifier. To robustly extract the LIDMark, we design a novel Factorized-Head Decoder (FHD). Its architecture factorizes the shared backbone features into two specialized heads (i.e., regression and classification), robustly reconstructing the embedded landmarks and identifier, respectively, even when subjected to severe distortion or tampering. This design realizes an "all-in-one" trifunctional forensic solution: the regression head underlies an "intrinsic-extrinsic" consistency check for detection and localization, while the classification head robustly decodes the source identifier for tracing. Extensive experiments show that the proposed LIDMark framework provides a unified, robust, and imperceptible solution for the detection, localization, and tracing of deepfake content. The code is available at https://github.com/vpsg-research/LIDMark.
