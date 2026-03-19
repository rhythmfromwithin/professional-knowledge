---
title: "XLinear: Frequency-Enhanced MLP with CrossFilter for Robust Long-Range Forecasting"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.15645
priority: high
status: unread
interest: medium
next_step: skim
---
# XLinear: Frequency-Enhanced MLP with CrossFilter for Robust Long-Range Forecasting
> 原文: [https://arxiv.org/abs/2603.15645](https://arxiv.org/abs/2603.15645)

arXiv:2603.15645v1 Announce Type: new
Abstract: Time series forecasters are widely used across various domains. Among them, MLP (multi-layer perceptron)-based forecasters have been proven to be more robust to noise compared to Transformer-based forecasters. However, MLP struggles to capture complex features, resulting in limitations on capturing long-range dependencies. To address this challenge, we propose XLinear, an MLP-based forecaster for long-range forecasting. Firstly, we decompose the time series into trend and seasonal components. For the trend component which contains long-range characteristics, we design Enhanced Frequency Attention (EFA) to capture long-term dependencies by leveraging frequency-domain operations. Additionally, a CrossFilter Block is proposed for the seasonal component to maintain the model's robustness to noise, avoiding the problems of low robustness often caused by attention mechanisms. Experimental results demonstrate that XLinear achieves state-of-the-art performance on test datasets. While keeping the lightweight architecture and high robustness of MLP-based models, our forecaster outperforms other MLP-based forecasters in capturing long-range dependencies.
