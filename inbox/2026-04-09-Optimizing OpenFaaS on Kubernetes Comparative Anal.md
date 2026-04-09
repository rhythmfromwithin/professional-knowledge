---
title: "Optimizing OpenFaaS on Kubernetes: Comparative Analysis of Language Runtimes and Cluster Distributions"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2604.05496
priority: medium
status: unread
interest: medium
next_step: skim
---
# Optimizing OpenFaaS on Kubernetes: Comparative Analysis of Language Runtimes and Cluster Distributions
> 原文: [https://arxiv.org/abs/2604.05496](https://arxiv.org/abs/2604.05496)

arXiv:2604.05496v1 Announce Type: new
Abstract: Serverless computing, particularly Function-as-a-Service (FaaS), has revolutionized cloud computing by abstracting infrastructure management and enabling dynamic resource allocation. This paper examines the performance and compatibility of OpenFaaS, an open-source serverless platform, when deployed on various Kubernetes distributions, including Kubeadm, K3s, MicroK8s, and K0s. Moreover, leveraging the CloudLab infrastructure, this study examines the impact of Python, Go, and Node.js programming languages on the performance of Kubernetes-enabled OpenFaaS, specifically when these languages are used to develop functions deployed on the platform. The performance is evaluated and analyzed under various levels of concurrent invocations using several usage-level metrics, such as throughput and CPU usage, as well as responsiveness metrics, such as delay. According to our findings, Go consistently outperforms Python and Node.js in terms of throughput and CPU usage, making it the ideal runtime for serverless applications. Among the Kubernetes distributions, K3s and Kubeadm exhibit superior performance, with Kubeadm maintaining low latency and efficient CPU usage, and K3s demonstrating high throughput. This study provides valuable insights into optimizing the Kubernetes-enabled OpenFaaS platform, highlighting the strengths and trade-offs of different Kubernetes distributions and language runtimes.
