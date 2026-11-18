---
title: "PDFa11yMut: Mutation-Based Evaluation of Automated PDF Accessibility Validators"
source: "cs.HC - Human-Computer Interaction"
link: https://arxiv.org/abs/2611.21628
priority: low
status: unread
interest: medium
next_step: skim
---
# PDFa11yMut: Mutation-Based Evaluation of Automated PDF Accessibility Validators
> 原文: [https://arxiv.org/abs/2611.21628](https://arxiv.org/abs/2611.21628)

arXiv:2611.21628v1 Announce Type: new
Abstract: Automated validators are widely used to assess PDF accessibility, but their detection boundaries are difficult to measure without controlled ground truth. A validator-clean PDF may be free of the implemented machine-checkable failures, or it may contain accessibility-relevant structural defects that the validator does not detect. This paper introduces PDFa11yMut, a controlled mutation-based benchmark for evaluating automated PDF accessibility validators against independently verified PDF structure defects.
We generated 23 verified mutants from five validator-clean golden PDFs using five mutation operators targeting reading order, omitted assistive structure, heading hierarchy, marked-content association, and internal marked-content sequence. Each generated mutant was independently verified at the PDF structure level and checked for parseability, page-count preservation, and absence of detected visual differences. We then evaluated the mutants with three validators: PAC, Adobe Acrobat Accessibility Checker, and veraPDF, with veraPDF run using the PDF/UA-1 profile.
The validators detected a small and highly operator-specific subset of the verified mutants. PAC detected 4/23 mutants (17.4%), while Acrobat and veraPDF each detected 5/23 mutants (21.7%). All three validators detected every generated heading-hierarchy mutant. None detected the reading-order swap, omitted-structure, or internal MCID-order mutants. Acrobat and veraPDF also detected one marked-content association mutant that PAC missed. The practical implication is that a validator-clean result can coexist with verified, visually invisible structure defects that affect the assistive representation of a PDF.
