---
interest: medium
link: https://arxiv.org/abs/2606.17082
next_step: skim
priority: medium
slack_ts: '1781672196.638119'
source: cs.RO - Robotics
status: unread
title: 'ParkingTransformer: LLM-Enhanced End-to-End Trajectory Planning for Autonomous
  Parking'
---
# ParkingTransformer: LLM-Enhanced End-to-End Trajectory Planning for Autonomous Parking
> 原文: [https://arxiv.org/abs/2606.17082](https://arxiv.org/abs/2606.17082)

arXiv:2606.17082v1 Announce Type: new
Abstract: End-to-end autonomous parking has emerged as a critical task within the realm of autonomous driving. However, existing methods suffer from black-box characteristics, lacking high-level semantic understanding and interpretability, which impedes the realization of seamless long-distance autonomous parking from the road to the target spot. To address these limitations, we propose ParkingTransformer, a novel framework that leverages multi-view perception and the scene understanding capability of Large Language Models (LLMs). By combining trajectory queries with LLMs implicit state features, our method interacts directly with historical information and raw sensor data to output planning trajectories, eliminating the need for dense Bird's-View (BEV) representations. To compensate for the inadequate spatial reasoning ability of LLMs, we introduce 3D positional encoding to explicitly inject spatial geometric awareness. Furthermore, a fixed-window streaming mechanism is designed for historical information processing, significantly improving long-term temporal processing efficiency and inference speed. Additionally, a coarse-to-fine decoding strategy is employed to progressively enhance trajectory precision. Extensive closed-loop experiments are conducted on the CARLA simulator and real-world vehicle platforms. The results demonstrate that our method achieves a driving score of 61.32 in CARLA simulator and an average success rate of 88.70% in real-world experiments, validating the feasibility and effectiveness of the proposed algorithms.
