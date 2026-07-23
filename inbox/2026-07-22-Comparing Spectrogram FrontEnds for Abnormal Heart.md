---
interest: medium
link: https://arxiv.org/abs/2607.16220
next_step: skim
priority: medium
slack_ts: '1784777491.945589'
source: cs.CY - Computers and Society
status: unread
title: Comparing Spectrogram Front-Ends for Abnormal Heart-Sound Detection with a
  Convolutional Neural Network
---
# Comparing Spectrogram Front-Ends for Abnormal Heart-Sound Detection with a Convolutional Neural Network
> 原文: [https://arxiv.org/abs/2607.16220](https://arxiv.org/abs/2607.16220)

arXiv:2607.16220v1 Announce Type: new
Abstract: Heart disease kills a lot of people, and one cheap way to catch it early is by listening to heart sounds with a stethoscope, or better yet, just recording them and running them through a model. This project is a binary classification task: take a short clip of someones heartbeat and decide if it sounds normal or abnormal. Instead of trying out a bunch of different models, we kept the CNN the same the whole time and just changed how we turned the raw audio into a picture for it to look at. We tried three ways of doing that: a regular logmel spectrogram, PCEN (which basically normalizes each frequency bin over time), and a multi resolution version that stacks a few different window sizes together. We ran all three on the PhysioNet 2016 heart-sound dataset with the exact same setup but same model, same optimizer, same random seed. Turns out all three do pretty well at catching abnormal cases (sensitivity around 0.95), but PCEN and multi-resolution both edge out the plain logmel on the official PhysioNet accuracy metric (0.915 and 0.916 vs. 0.910). We also ran Grad-CAM to see where the model was actually looking, and it mostly focused on the low frequencies where S1 and S2 heart sounds live, which is a good sign that it learned something real
