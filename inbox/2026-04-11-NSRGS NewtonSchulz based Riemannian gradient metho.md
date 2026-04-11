---
interest: medium
link: https://arxiv.org/abs/2604.07372
next_step: skim
priority: medium
slack_ts: '1775875969.498089'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'NS-RGS: Newton-Schulz based Riemannian gradient method for orthogonal group
  synchronization'
---
# NS-RGS: Newton-Schulz based Riemannian gradient method for orthogonal group synchronization
> 原文: [https://arxiv.org/abs/2604.07372](https://arxiv.org/abs/2604.07372)

arXiv:2604.07372v1 Announce Type: new
Abstract: Group synchronization is a fundamental task involving the recovery of group elements from pairwise measurements. For orthogonal group synchronization, the most common approach reformulates the problem as a constrained nonconvex optimization and solves it using projection-based methods, such as the generalized power method. However, these methods rely on exact SVD or QR decompositions in each iteration, which are computationally expensive and become a bottleneck for large-scale problems. In this paper, we propose a Newton-Schulz-based Riemannian Gradient Scheme (NS-RGS) for orthogonal group synchronization that significantly reduces computational cost by replacing the SVD or QR step with the Newton-Schulz iteration. This approach leverages efficient matrix multiplications and aligns perfectly with modern GPU/TPU architectures. By employing a refined leave-one-out analysis, we overcome the challenge arising from statistical dependencies, and establish that NS-RGS with spectral initialization achieves linear convergence to the target solution up to near-optimal statistical noise levels. Experiments on synthetic data and real-world global alignment tasks demonstrate that NS-RGS attains accuracy comparable to state-of-the-art methods such as the generalized power method, while achieving nearly a 2$\times$ speedup.
