---
title: "Iterated Invariant EKF for Quadruped Robot Odometry"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2604.15449
priority: medium
status: unread
interest: medium
next_step: skim
---
# Iterated Invariant EKF for Quadruped Robot Odometry
> 原文: [https://arxiv.org/abs/2604.15449](https://arxiv.org/abs/2604.15449)

arXiv:2604.15449v1 Announce Type: new
Abstract: Kalman filter-based algorithms are fundamental for mobile robots, as they provide a computationally efficient solution to the challenging problem of state estimation. However, they rely on two main assumptions that are difficult to satisfy in practice: (a) the system dynamics must be linear with Gaussian process noise, and (b) the measurement model must also be linear with Gaussian measurement noise. Previous works have extended assumption (a) to nonlinear spaces through the Invariant Extended Kalman Filter (IEKF), showing that it retains properties similar to those of the classical Kalman filter when the system dynamics are group-affine on a Lie group. More recently, the counterpart of assumption (b) for the same nonlinear setting was addressed in [1]. By means of the proposed Iterated Invariant Extended Kalman Filter (IterIEKF), the authors of that work demonstrated that the update step exhibits several compatibility properties of the classical linear Kalman filter. In this work, we introduce a novel open-source state estimation algorithm for legged robots based on the IterIEKF. The update step of the proposed filter relies solely on proprioceptive measurements, exploiting kinematic constraints on foot velocity during contact and base-frame velocity, making it inherently robust to environmental conditions. Through extensive numerical simulations and evaluation on real-world datasets, we demonstrate that the IterIEKF outperforms the vanilla IEKF, the SO(3)-based Kalman Filter, and its iterated variant in terms of both accuracy and consistency.
