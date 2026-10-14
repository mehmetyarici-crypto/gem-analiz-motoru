**English** | [Türkçe](README.tr.md)

# GEM — Quran-Based Strategic Analysis Framework

> **This project does not claim religious authority.** Outputs are interpretation, not ruling.
> It does not claim prophecy, fatwa, or definitive historical prediction.

---

## Table of Contents

- [What is this project?](#what-is-this-project)
- [What does it do?](#what-does-it-do)
- [What does it not do?](#what-does-it-not-do)
- [Versions and Documentation](#versions-and-documentation)
- [Files](#files)
- [Quick Start](#quick-start)

---

## What is this project?

GEM (Future-Oriented Reasoning) is a 26-step, 5-macro-phase framework of thought and audit that examines Quranic verses through **strategic analysis** and hermeneutic methods.

### What does it do?

- Analyzes the verse text **linguistically** (siyāq-sibāq, nuzūl, address, lexicographical matrix).
- Derives **maqāṣid** (higher objectives).
- Matches it with contemporary issues and governance crises.
- Produces **scenarios** (4 structural possibilities).
- Suggests **decision branches** (actionable policy options and leverage points).
- Critiques its own analysis (Red Team, empirical falsifiability, self-audit, bias filters).

### What does it not do?

- Does not issue fatwa.
- Does not claim religious authority or absolute truth.
- Does not predict the unseen (ghayb) or definitive future dates.
- Does not give definitive judicial rulings.

---

## Versions and Documentation

- **v6.1.1 (Current Draft):** [docs/tr/GEM-v6.1.1-taslak.md](docs/tr/GEM-v6.1.1-taslak.md) — 26 steps, 5 macro-phases, Enfüs-Âfâk & Heart Fiqh analytical lens, source verification, and epistemic disclaimer.
- **Roadmap:** [docs/tr/GEM-v6.1.1-yol-haritasi.md](docs/tr/GEM-v6.1.1-yol-haritasi.md) — GitHub transition and verification plan.
- **Changelog:** [CHANGELOG.md](CHANGELOG.md) — Version history.
- **v5.2.0 (Archive):** [GEM-V520-TALIMAT.md](GEM-V520-TALIMAT.md) — Historical specification.

---

## Files

| File | Purpose |
|---|---|
| `YONTEM.md` | Summary of the 26-step method and macro-phases |
| `src/gem_lint.py` | Format, language safety and schema linter (Python) |
| `docs/tr/04-ornek-rapor.md` | Historical report template (v5.2.0) |
| `docs/tr/GEM-v6.1.1-taslak.md` | Current v6.1.1 methodology standard draft |
| `docs/tr/GEM-v6.1.1-yol-haritasi.md` | Implementation and integration roadmap |

---

## Quick Start

```bash
# Run the format and safety auditor
python src/gem_lint.py docs/tr/04-ornek-rapor.md
```
