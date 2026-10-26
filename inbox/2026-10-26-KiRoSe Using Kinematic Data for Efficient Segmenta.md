---
title: "KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2610.31801
priority: medium
status: unread
interest: medium
next_step: skim
---
# KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations
> 原文: [https://arxiv.org/abs/2610.31801](https://arxiv.org/abs/2610.31801)

arXiv:2610.31801v1 Announce Type: new
Abstract: Segmenting robot demonstration data into disjoint temporal and semantic subsegments is valuable for learning, cleaning, retrieval, and analysis. Segmentation is often performed manually in a tedious and error prone process. Multimodal Large Language Models (MLLMs) have the potential for automating this process, but directly ingesting raw multi camera video streams into MLLMs can be costly and can quickly exhaust context windows. In this paper, we introduce KiRoSe (Kinematics for Robot Segmentation), a novel framework that focuses on the companion stream of robot kinematic data. Inspired by the principle of classical entropy coding, such as Huffman coding, where frequently occurring symbols are represented more compactly, we propose Sparse Motion Tokens (SMTs), a discrete kinematic vocabulary designed to compactly represent recurring, temporally localized motion patterns, which we refer to as kinematic events. SMTs are learned by encoding kinematic trajectories with temporal segment supervision and quantizing the resulting features. We use increasingly available robot demonstration subtask annotations to supervise an open language model to interpret the resulting token sequences. Evaluation against human labeled segmentation shows that KiRoSe can substantially outperform baseline segmentation methods in F1 quality and transfers zero shot to unseen robot embodiments and egocentric human motion, while preserving the language models open vocabulary knowledge. Beyond segmentation, KiRoSe tracks task progress on an unseen robot and detects when an action is being reversed.(website: https://berkeleyautomation.github.io/kirose/)
