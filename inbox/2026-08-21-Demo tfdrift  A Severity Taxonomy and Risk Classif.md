---
title: "Demo: tfdrift - A Severity Taxonomy and Risk Classification Framework for Infrastructure Drift Detection"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2608.18173
priority: low
status: unread
interest: medium
next_step: skim
---
# Demo: tfdrift - A Severity Taxonomy and Risk Classification Framework for Infrastructure Drift Detection
> 原文: [https://arxiv.org/abs/2608.18173](https://arxiv.org/abs/2608.18173)

arXiv:2608.18173v1 Announce Type: new
Abstract: Infrastructure as Code (IaC) tools like Terraform have become the standard for declarative cloud resource management, yet configuration drift, where deployed infrastructure diverges from its declared state, remains a persistent operational and security challenge. Current detection approaches treat all changes equivalently, contributing to alert fatigue that causes operators to miss security-critical modifications. We propose a generalized severity taxonomy for infrastructure drift that classifies changes into four risk tiers based on resource type and attribute-level impact. We implement this taxonomy in tfdrift, an open-source classification framework with 60+ configurable rules covering AWS, Azure, and GCP resource patterns (evaluation reported here is AWS-focused). Evaluation across 150+ AWS Terraform workspaces demonstrates that severity filtering reduces alert volume by 73% while retaining 94% of security-relevant changes, offering a lightweight alternative to ML-based alert filtering. tfdrift is available at github.com/sudarshan8417/tfdrift.
