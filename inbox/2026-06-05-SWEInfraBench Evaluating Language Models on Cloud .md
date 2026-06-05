---
title: "SWE-InfraBench: Evaluating Language Models on Cloud Infrastructure Code"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2606.05249
priority: low
status: unread
interest: medium
next_step: skim
---
# SWE-InfraBench: Evaluating Language Models on Cloud Infrastructure Code
> 原文: [https://arxiv.org/abs/2606.05249](https://arxiv.org/abs/2606.05249)

arXiv:2606.05249v1 Announce Type: new
Abstract: Building infrastructure-as-code (IaC) in cloud computing is a critical task, underpinning the reliability, scalability, and security of modern software systems. Despite the remarkable progress of large language models (LLMs) in software engineering -- demonstrated across many dedicated benchmarks -- their capabilities in developing IaC remain underexplored. Unlike existing IaC benchmarks that predominantly center on declarative paradigms such as Terraform and involve generating entire codebases from scratch, our benchmark reflects the incremental code edits common in enterprise development with imperative tools like the AWS CDK. We present SWE-InfraBench, a diverse evaluation dataset sourced from dozens of real-world IaC codebases that challenge LLMs to perform realistic code modifications in AWS CDK repositories. Each example requires models to implement changes to existing codebases based on natural language instructions, with success determined by passing provided test cases. These tasks demand sophisticated reasoning about cloud resource dependencies and implementation patterns beyond conventional code generation challenges. Our evaluation results reveal significant limitations in current LLMs showing that even state-of-the-art systems struggle with many tasks -- the best model, Sonnet 3.7, succeeds in only 34\% of cases, while specialized reasoning models like DeepSeek R1 achieve just 24% success. The SWE-InfraBench dataset is available at: https://www.kaggle.com/datasets/64e59070fd51c0278560b01eb5dc4f3c447d5268cdabe5a350d2969e4413fea5
