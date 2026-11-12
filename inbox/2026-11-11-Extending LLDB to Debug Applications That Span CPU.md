---
interest: medium
link: https://engineering.fb.com/2026/11/09/developer-tools/extending-lldb-to-debug-applications-that-span-cpus-and-gpus/
next_step: skim
priority: medium
slack_ts: '1794466369.087359'
source: Meta Engineering
status: unread
title: Extending LLDB to Debug Applications That Span CPUs and GPUs
---
# Extending LLDB to Debug Applications That Span CPUs and GPUs
> 原文: [https://engineering.fb.com/2026/11/09/developer-tools/extending-lldb-to-debug-applications-that-span-cpus-and-gpus/](https://engineering.fb.com/2026/11/09/developer-tools/extending-lldb-to-debug-applications-that-span-cpus-and-gpus/)

We built a vendor-neutral accelerator plugin architecture in lldb-server for debugging applications that span CPUs and GPUs. It separates shared debugger infrastructure from hardware-specific device control. The design represents the CPU and GPU as separate debugger processes while presenting them in one debugging session. Modern AI applications rarely execute in one place. A workload can [...]

[Read More...](https://engineering.fb.com/2026/11/09/developer-tools/extending-lldb-to-debug-applications-that-span-cpus-and-gpus/)

The post [Extending LLDB to Debug Applications That Span CPUs and GPUs](https://engineering.fb.com/2026/11/09/developer-tools/extending-lldb-to-debug-applications-that-span-cpus-and-gpus/) appeared first on [Engineering at Meta](https://engineering.fb.com).
