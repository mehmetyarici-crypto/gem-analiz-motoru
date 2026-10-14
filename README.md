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

## Published GEM v6.1.1 Reports (Corpus)

The following reports are fully compliant with the GEM v6.1.1 standard and verified with external cryptographic SHA-256 manifests:

| # | Verse | Topic | Report File | Status |
|:---:|:---:|:---|:---|:---:|
| **01** | **At-Tawbah 9:5** | Treaty Violation, Deterrence, and Law of Legitimate Defense | [`docs/tr/06-pilot-tevbe-95-v6.1.1.md`](docs/tr/06-pilot-tevbe-95-v6.1.1.md) | `PRE-RELEASE` |
| **02** | **An-Nisa 4:34** | Domestic Governance, Qiwamah, and Non-Violent Counsel Doctrine | [`docs/tr/07-pilot-nisa-434-v6.1.1.md`](docs/tr/07-pilot-nisa-434-v6.1.1.md) | `PRE-RELEASE` |
| **03** | **Al-Ma'idah 5:38** | Property Rights, Theft Punishment, Necessity, and Social Security | [`docs/tr/08-pilot-maide-538-v6.1.1.md`](docs/tr/08-pilot-maide-538-v6.1.1.md) | `PRE-RELEASE` |
| **04** | **Al-Baqarah 2:256** | Freedom of Faith and Conscience, Prohibition of Coercion, and Pluralism | [`docs/tr/09-rapor-bakara-2256-v6.1.1.md`](docs/tr/09-rapor-bakara-2256-v6.1.1.md) | `PRE-RELEASE` |
| **05** | **An-Nisa 4:58** | Public Governance, Meritocracy, Judicial Independence, and Justice | [`docs/tr/10-rapor-nisa-458-v6.1.1.md`](docs/tr/10-rapor-nisa-458-v6.1.1.md) | `PRE-RELEASE` |
| **06** | **Ali 'Imran 3:159** | Consultation (Shūrā) in Crisis Governance, Leadership, and Determination | [`docs/tr/11-rapor-ali-imran-3159-v6.1.1.md`](docs/tr/11-rapor-ali-imran-3159-v6.1.1.md) | `PRE-RELEASE` |
| **07** | **Al-Hujurat 49:9–10** | Conflict Resolution, International Arbitration, Law of Baghy, and Peacekeeping | [`docs/tr/12-rapor-hucurat-49910-v6.1.1.md`](docs/tr/12-rapor-hucurat-49910-v6.1.1.md) | `PRE-RELEASE` |
| **08** | **Al-Isra 17:36** | Epistemic Responsibility, Verification, Cognitive Security, and AI Era | [`docs/tr/13-rapor-isra-1736-v6.1.1.md`](docs/tr/13-rapor-isra-1736-v6.1.1.md) | `PRE-RELEASE` |

---

## Versions and Documentation

- **v6.1.1 (Current Standard):** [docs/tr/GEM-v6.1.1-taslak.md](docs/tr/GEM-v6.1.1-taslak.md) — 26 steps, 5 macro-phases, Enfüs-Âfâk & Heart Fiqh analytical lens, source verification, and epistemic disclaimer.
- **Academic Peer-Review Guide:** [docs/tr/akademik-hakem-rehberi.md](docs/tr/akademik-hakem-rehberi.md) — 5-dimension peer review rubric and Z-5 form.
- **Roadmap:** [docs/tr/GEM-v6.1.1-yol-haritasi.md](docs/tr/GEM-v6.1.1-yol-haritasi.md) — Implementation and verification roadmap.
- **Linter Rules:** [docs/tr/linter-kurallari.md](docs/tr/linter-kurallari.md) — Formal linter rule specifications.
- **Changelog:** [CHANGELOG.md](CHANGELOG.md) — Version history.
- **v5.2.0 (Archive):** [GEM-V520-TALIMAT.md](GEM-V520-TALIMAT.md) — Historical specification.

---

## Files

| File | Purpose |
|---|---|
| `YONTEM.md` | Summary of the 26-step method and macro-phases |
| `src/gem_lint.py` | Format, language safety, schema, and manifest linter (Python) |
| `docs/tr/05-ornek-rapor-v6.1.1.md` | Official v6.1.1 report template |
| `docs/tr/GEM-v6.1.1-taslak.md` | Current v6.1.1 methodology standard draft |
| `docs/tr/akademik-hakem-rehberi.md` | Independent external peer-review guidelines |

---

## Quick Start

```bash
# Lint the template or any report
python src/gem_lint.py docs/tr/05-ornek-rapor-v6.1.1.md --katman 3 --h6
python src/gem_lint.py docs/tr/11-rapor-ali-imran-3159-v6.1.1.md --katman 3 --h6

# Run test suite
pytest tests/ -v
```
