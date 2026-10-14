#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GEM Linter v6.1.1 — Pytest Test Paketi
"""

import os
import sys
import tempfile
import subprocess
from pathlib import Path
import pytest

# src dizinini sys.path'e ekle
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "src"))

from gem_lint import (
    GemLinterV6,
    normalize,
    citirnak_muaf_mi,
    BLOCK,
    WARN,
    generate_manifest,
    check_cross_similarity,
)

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


class TestGemLintNormalization:
    def test_normalize_turkish(self):
        assert normalize("İbn Fâris") == "ibn faris"
        assert normalize("Şâtıbî") == "satibi"
        assert normalize("Lisânü'l-Arab") == "lisanul-arab"

    def test_quote_exemption(self):
        # Tırnak içi muaf olmalı (18.1-B)
        line = 'Bu metinde "kesinlikle" kelimesi alıntı olarak geçmektedir.'
        assert citirnak_muaf_mi(line, "kesinlikle") is True

        # Tırnak dışı muaf olmamalı
        line2 = "Bu sonuç kesinlikle kanıtlanmıştır."
        assert citirnak_muaf_mi(line2, "kesinlikle") is False


class TestGemLinterRules:
    def test_valid_fixture(self):
        valid_file = FIXTURES_DIR / "valid_v611.md"
        assert valid_file.exists()

        linter = GemLinterV6(valid_file, katman=3, h6=True)
        code = linter.run_all()

        # Kesici hata (BLOCK) olmamalı
        block_findings = [f for f in linter.findings if f["level"] == BLOCK]
        assert len(block_findings) == 0, f"Beklenmeyen BLOCK hataları: {block_findings}"
        # Ön sürüm olduğu için çıkış kodu 1 (WARN) veya 0 (PASS) olmalı
        assert code in [0, 1]

    def test_forbidden_words_detected(self):
        invalid_file = FIXTURES_DIR / "invalid_forbidden.md"
        assert invalid_file.exists()

        linter = GemLinterV6(invalid_file, katman=3, h6=False)
        code = linter.run_all()

        assert code == 2  # Hard fail / BLOCK
        block_findings = [f for f in linter.findings if f["level"] == BLOCK]
        assert len(block_findings) > 0

        # Hem Türkçe hem İngilizce yasaklı kelimeler yakalanmalı
        messages = " ".join(f["message"] for f in block_findings)
        assert "kesinlikle" in messages
        assert "flawless" in messages
        assert "%100" in messages or "ispatlanmıştır" in messages

    def test_contextual_exception_for_absolute(self):
        # 'absolute path' ve 'mutlak nass' uyarı veya blok üretmemeli
        text = """---
gem_version: "6.1.1"
status: "PRE-RELEASE"
---
Bu koddaki absolute path ifadesi teknik bir yoldur.
Ayrıca mutlak nass çerçevesinde değerlendirilmiştir.
"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as f:
            f.write(text)
            temp_path = Path(f.name)

        try:
            linter = GemLinterV6(temp_path, katman=1, h6=False)
            linter.load_file()
            linter.check_language_safety()

            # Koşullu yasaklı uyarısı ISTISNA_IFADELERI nedeniyle verilmemeli
            warn_messages = [f["message"] for f in linter.findings if "absolute" in f["message"] or "mutlak" in f["message"]]
            assert len(warn_messages) == 0
        finally:
            if temp_path.exists():
                temp_path.unlink()

    def test_manifest_generation_and_verification(self):
        content = "Test içeriği SHA-256 bütünlük kontrolü için."
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as f:
            f.write(content)
            temp_path = Path(f.name)

        try:
            gen_code = generate_manifest(temp_path)
            assert gen_code == 0

            manifest_file = temp_path.with_suffix(temp_path.suffix + ".sha256")
            assert manifest_file.exists()

            # Linter manifesti doğrulayabilmeli
            linter = GemLinterV6(temp_path, manifest_path=manifest_file)
            linter.load_file()
            linter.is_v6 = True
            linter.check_v4_hash()

            block_hash_findings = [f for f in linter.findings if f["rule"] == "L-0404"]
            assert len(block_hash_findings) == 0

            # Dosya içeriği değiştirilirse manifest BLOCK üretmeli
            temp_path.write_text("Değiştirilmiş içerik!", encoding="utf-8")
            linter_tampered = GemLinterV6(temp_path, manifest_path=manifest_file)
            linter_tampered.load_file()
            linter_tampered.is_v6 = True
            linter_tampered.check_v4_hash()

            block_tampered = [f for f in linter_tampered.findings if f["rule"] == "L-0404"]
            assert len(block_tampered) == 1
        finally:
            if temp_path.exists():
                temp_path.unlink()
            m = temp_path.with_suffix(temp_path.suffix + ".sha256")
            if m.exists():
                m.unlink()


class TestGemLintCLI:
    def test_cli_version(self):
        cmd = [sys.executable, str(ROOT_DIR / "src" / "gem_lint.py"), "--version"]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        assert res.returncode == 0
        assert "v6.1.1" in res.stdout

    def test_cli_help(self):
        cmd = [sys.executable, str(ROOT_DIR / "src" / "gem_lint.py"), "--help"]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        assert res.returncode == 0
        assert "Kullanım:" in res.stdout
