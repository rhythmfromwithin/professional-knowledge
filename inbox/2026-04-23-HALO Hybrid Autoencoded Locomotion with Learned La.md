---
title: "HALO: Hybrid Auto-encoded Locomotion with Learned Latent Dynamics, Poincar\'e Maps, and Regions of Attraction"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2604.18887
priority: medium
status: unread
interest: medium
next_step: skim
---
# HALO: Hybrid Auto-encoded Locomotion with Learned Latent Dynamics, Poincar\'e Maps, and Regions of Attraction
> 原文: [https://arxiv.org/abs/2604.18887](https://arxiv.org/abs/2604.18887)

arXiv:2604.18887v1 Announce Type: new
Abstract: Reduced-order models are powerful for analyzing and controlling high-dimensional dynamical systems. Yet constructing these models for complex hybrid systems such as legged robots remains challenging. Classical approaches rely on hand-designed template models (e.g., LIP, SLIP), which, though insightful, only approximate the underlying dynamics. In contrast, data-driven methods can extract more accurate low-dimensional representations, but it remains unclear when stability and safety properties observed in the latent space meaningfully transfer back to the full-order system. To bridge this gap, we introduce HALO (Hybrid Auto-encoded Locomotion), a framework for learning latent reduced-order models of periodic hybrid dynamics directly from trajectory data. HALO employs an autoencoder to identify a low-dimensional latent state together with a learned latent Poincar\'e map that captures step-to-step locomotion dynamics. This enables Lyapunov analysis and the construction of an associated region of attraction in the latent space, both of which can be lifted back to the full-order state space through the decoder. Experiments on a simulated hopping robot and full-body humanoid locomotion demonstrate that HALO yields low-dimensional models that retain meaningful stability structure and predict full-order region-of-attraction boundaries.
