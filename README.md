**English** | [Türkçe](README.tr.md)

# GEM — Quran-Based Strategic Analysis Framework

> **This project does not claim religious authority.** Outputs are interpretation, not ruling. It does not claim prophecy, fatwa, or definitive historical prediction.

---

## Table of Contents

- [What is this project?](#what-is-this-project)
- [What does it do?](#what-does-it-do)
- [What does it not do?](#what-does-it-not-do)
- [Files](#files)
- [Quick Start](#quick-start)

---

## What is this project?

GEM (Future-Oriented Reasoning) is a 26-step framework of thought and audit that examines Quranic verses through **strategic analysis** methods.

### What does it do?

- Analyzes the verse text **linguistically** (siyāq-sibāq, nuzūl, address)
- Derives **maqāṣid** (objectives)
- Matches it with contemporary issues
- Produces **scenarios** (4 possibilities)
- Suggests **decision branches** (10 domains)
- Critiques its own analysis (Red Team, falsifiability, self-audit)

### What does it not do?

- Does not issue fatwa
- Does not claim religious authority
- Does not predict the future
- Does not give definitive rulings

---

## Files

| File | Purpose |
|---|---|
| `YONTEM.md` | Summary of the 26-step method |
| `src/gem_lint.py` | Language safety auditor (Python) |
| `docs/tr/04-ornek-rapor.md` | Report template |

---

## Quick Start

```bash
# Run the language auditor
python src/gem_lint.py docs/tr/04-ornek-rapor.md
