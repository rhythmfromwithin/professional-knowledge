---
title: "Learning from Human Corrections through Temporal Preferences"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2611.31446
priority: medium
status: unread
interest: medium
next_step: skim
---
# Learning from Human Corrections through Temporal Preferences
> 原文: [https://arxiv.org/abs/2611.31446](https://arxiv.org/abs/2611.31446)

arXiv:2611.31446v1 Announce Type: new
Abstract: When people intervene to correct a robot, they provide information not only through how they correct its behavior, but also through when they choose to intervene. Existing approaches to Learning from Corrections focus on comparing the new trajectory to the robot's originally intended behavior, thus underutilizing the context of the robot's behavior before the intervention. In this work, we investigate how both pre- and post-intervention behavior can be translated into preference pairs for learning value functions that approximate a human's latent reward. We construct post-intervention preferences by comparing corrected behavior with the behavior it replaces, and pre-intervention preferences from temporal relationships among states leading up to an intervention. We evaluate the learned value representations through two downstream tasks: goal inference and correction forecasting. Our results show that post-intervention preferences are particularly effective for goal inference, while pre-intervention preferences provide strong correction-forecasting performance. Combining both sources of information performs strongly across both tasks, even when generalizing to participants unseen during training. These findings demonstrate that both when and how humans correct provide complementary information for learning value representations from corrective interactions.
