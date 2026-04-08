---
interest: medium
link: https://arxiv.org/abs/2604.03438
next_step: skim
priority: low
slack_ts: '1775618433.696229'
source: cs.SE - Software Engineering
status: unread
title: 'Android Instrumentation Testing in Continuous Integration: Practices, Patterns,
  and Performance'
---
# Android Instrumentation Testing in Continuous Integration: Practices, Patterns, and Performance
> 原文: [https://arxiv.org/abs/2604.03438](https://arxiv.org/abs/2604.03438)

arXiv:2604.03438v1 Announce Type: new
Abstract: Android instrumentation tests (end-to-end tests that run on a device or emulator) can catch problems that simpler tests miss. However, running these tests automatically in continuous integration (CI) is often difficult because emulator setup is fragile and configurations tend to drift over time. We study how open-source Android apps run instrumentation tests in CI by analyzing 4,518 repositories that use CI (snapshot: Aug. 10, 2025). We examine CI workflow files, scripts, and build configurations to identify cases where device setup is defined in Gradle (e.g., Gradle Managed Devices). Our results answer three questions about adoption, evolution, and outcomes. First, only about one in ten repositories (481/4,518; 10.6%) run instrumentation tests in CI, typically using either reusable community components or repository-specific custom scripts to set up emulators. Second, these setups usually stay the same over time; when changes happen, projects tend to move from custom scripts toward reusable community components. Third, we study why projects change their CI setup by analyzing their commits, pull requests, and issue messages. We evaluate how different setup styles perform using GitHub Actions run- and step-level metadata (e.g., outcomes, duration, reruns, and queue delay). We find that teams often change approaches to expand test coverage, and that each approach fits different needs: community-based setups are typically the most reliable and efficient for everyday checks on new code, third-party device labs suit scheduled regression testing but can be costlier and fail more often, and custom scripting provides flexibility but is associated with more reruns.
