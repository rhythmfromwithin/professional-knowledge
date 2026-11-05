---
interest: medium
link: https://arxiv.org/abs/2611.03815
next_step: skim
priority: medium
slack_ts: '1793859280.131379'
source: cs.RO - Robotics
status: unread
title: 'AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld
  Data'
---
# AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data
> 原文: [https://arxiv.org/abs/2611.03815](https://arxiv.org/abs/2611.03815)

arXiv:2611.03815v1 Announce Type: new
Abstract: AIRoA-0 (A-0) is a bimanual manipulation system learned from 16,151 hours of handheld demonstrations, with no robot data collected at any stage. The demonstrations are recorded with YUBI, our open-source handheld gripper, which lets people record manipulation data anywhere with no robot present. From a single instruction, A-0 sorts more than a dozen small parts into their numbered cells and changes the mop pads and brush of a robot vacuum; among other tasks, it unzips a pencil case and folds a towel. It performs these tasks using only a camera on each wrist, with no head or scene camera, at a site where none of its training data was recorded. Across the ten tasks of our evaluation, it averages a success rate of 78%, against 27% for the strongest of four other vision-language-action models post-trained on the same task demonstrations. We collect no teleoperation data and use no reinforcement learning or on-robot corrections, and the robot appears only at test time. The system learns which regions of each wrist view matter for the task, predicts the stage the task has reached, and decodes actions as a continuous stream. A-0 is embodiment-agnostic: it runs on robots that mount the YUBI gripper, such as a bimanual Franka, TX-G2, OpenArm and UR. We are releasing the dataset, to our knowledge the largest open dataset of handheld-gripper demonstrations with task and subtask instructions, together with the pre-trained weights and the post-training recipe. Videos of A-0 on every task are on the project page, https://a-0.airoa.io. Anyone can build the gripper, record a task of their own and post-train the model on it in under four hours on a single node of eight H200 GPUs.
