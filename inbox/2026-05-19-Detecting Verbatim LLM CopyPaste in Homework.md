---
title: "Detecting Verbatim LLM Copy-Paste in Homework"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.16336
priority: low
status: unread
interest: medium
next_step: skim
---
# Detecting Verbatim LLM Copy-Paste in Homework
> 原文: [https://arxiv.org/abs/2605.16336](https://arxiv.org/abs/2605.16336)

arXiv:2605.16336v1 Announce Type: new
Abstract: Large language models (LLMs) have made fluent essay writing, code drafting, and quiz answering instantly available to students at every level, from secondary school through graduate study. Many educators do not object to LLM use \emph{per~se}; what they need to detect is the case in which a student pastes the assignment prompt into a chatbot and submits the model's reply verbatim, without engaging with the work. Existing post-hoc AI-text detectors remain unreliable and have been shown to penalise non-native English writers, while output-side watermarks require cooperation from the model provider. We propose an alternative that the educator controls directly: an input-side watermark in which an invisible instruction is embedded inside the visible assignment prompt itself. An LLM that ingests the prompt verbatim quietly reads the hidden instruction and writes a tell-tale signature into its reply, exposing the copy-and-paste pathway specifically. We describe SteganoPrompt, a single-page, zero-dependency web tool that encodes an arbitrary printable-ASCII payload into the deprecated Unicode Tags block (\texttt{U+E0000}--\texttt{U+E007F}). The encoded string is visually identical to the original, survives common copy-paste channels (Word, Google Docs, PDF, Markdown, Slack, e-mail, the major learning-management systems), and is reliably tokenized by frontier models. We evaluate compliance across seven LLM families and a representative set of educational content channels. The work is informed by my experience as a graduate teaching assistant for an undergraduate software engineering course at the George Washington University. The tool is released under the MIT licence at \url{https://ezharjan.github.io/SteganoPrompt/}.
