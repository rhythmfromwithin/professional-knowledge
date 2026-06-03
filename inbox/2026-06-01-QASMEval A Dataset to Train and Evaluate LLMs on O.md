---
interest: medium
link: https://arxiv.org/abs/2605.30358
next_step: skim
priority: high
slack_ts: '1780462692.257209'
source: cs.LG - Machine Learning
status: unread
title: 'QASM-Eval: A Dataset to Train and Evaluate LLMs on OpenQASM-3 Beyond Quantum
  Circuits'
---
# QASM-Eval: A Dataset to Train and Evaluate LLMs on OpenQASM-3 Beyond Quantum Circuits
> 原文: [https://arxiv.org/abs/2605.30358](https://arxiv.org/abs/2605.30358)

arXiv:2605.30358v1 Announce Type: new
Abstract: Quantum computing remains in the Noisy Intermediate-Scale Quantum (NISQ) era, where the performance is highly constrained to noise. Addressing the limitation often requires hardware-facing capabilities beyond gate-sequence circuit specification, including mid-circuit measurement and classical feedback for quantum error correction (QEC), precise timing control for dynamical decoupling (DD), and pulse-level waveform access for calibration. OpenQASM-3 was introduced to expose exactly these capabilities, providing a hardware-level programming interface. However, despite the rapid progress of large language models in code generation, there is still no dataset specifically designed to train and evaluate LLMs on OpenQASM-3 programs that involve its advanced hardware-oriented features. To address this gap, we introduce QASM-Eval, the first comprehensive dataset designed to train and evaluate LLMs on OpenQASM-3. Rather than focusing on quantum algorithm design or reasoning, QASM-Eval explicitly targets the language's hardware-facing features. QASM-Eval comprises an expert-verified test set of 100 tasks and a training set of 4,000 tasks, systematically covering classical logic, timing scheduling, pulse control, and complex real-world workflows. To automatically validate generated programs, we check syntax, quantum states and program timeline using an extended verifier. Our evaluation reveals that while state-of-the-art LLMs struggle heavily in OpenQASM-3 coding tasks, targeted fine-tuning on QASM-Eval yields significant gains. QASM-Eval provides a crucial benchmark and training foundation to accelerate the development of reliable LLM assistants for hardware-facing quantum programming in NISQ era. Data and code: https://github.com/fuzhenxiao/QASM-Eval
