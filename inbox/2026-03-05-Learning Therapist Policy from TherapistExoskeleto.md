---
interest: medium
link: https://arxiv.org/abs/2603.02458
next_step: skim
priority: medium
slack_ts: '1773456089.800419'
source: cs.RO - Robotics
status: unread
title: Learning Therapist Policy from Therapist-Exoskeleton-Patient Interaction
---
# Learning Therapist Policy from Therapist-Exoskeleton-Patient Interaction
> 原文: [https://arxiv.org/abs/2603.02458](https://arxiv.org/abs/2603.02458)

arXiv:2603.02458v1 Announce Type: new
Abstract: Post-stroke rehabilitation is often necessary for patients to regain proper walking gait. However, the typical therapy process can be exhausting and physically demanding for therapists, potentially reducing therapy intensity, duration, and consistency over time. We propose a Patient-Therapist Force Field (PTFF) to visualize therapist responses to patient kinematics and a Synthetic Therapist (ST) machine learning model to support the therapist in dyadic robot-mediated physical interaction therapy. The first encodes patient and therapist stride kinematics into a shared low-dimensional latent manifold using a Variational Autoencoder (VAE) and models their interaction through a Gaussian Mixture Model (GMM), which learns a probabilistic vector field mapping patient latent states to therapist responses. This representation visualizes patient-therapist interaction dynamics to inform therapy strategies and robot controller design. The latter is implemented as a Long Short-Term Memory (LSTM) network trained on patient-therapist interaction data to predict therapist-applied joint torques from patient kinematics. Trained and validated using leave-one-out cross-validation across eight post-stroke patients, the model was integrated into a ROS-based exoskeleton controller to generate real-time torque assistance based on predicted therapist responses. Offline results and preliminary testing indicate the potential of their use as an alternative approach to post-stroke exoskeleton therapy. The PTFF provides understanding of the therapist's actions while the ST frees the human therapist from the exoskeleton, allowing them to continuously monitor the patient's nuanced condition.
