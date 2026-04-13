"""
tests/test_report.py
--------------------
Smoke tests for docpilot.Report.
Run with: pytest tests/
"""

import sys
import os
from pathlib import Path

# Allow running from project root without install
sys.path.insert(0, str(Path(__file__).parent.parent))

import pandas as pd
import pytest
from docpilot import Report, BrandStyles


TMP = Path(__file__).parent / "_tmp"
TMP.mkdir(exist_ok=True)


def test_basic_report_builds():
    out = TMP / "basic.pdf"
    rpt = Report(str(out), title="Test Report", company="Test Co")
    rpt.title_block("Test Report", subtitle="Sub", date="2025-01-01", version="1")
    rpt.section("Intro", "Hello <b>world</b>.")
    rpt.bullets("Points", ["One", "Two", "Three"])
    rpt.build()
    assert out.exists()
    assert out.stat().st_size > 1000


def test_dataframe_table():
    out = TMP / "df_table.pdf"
    df = pd.DataFrame({"A": [1, 2], "B": ["x", "y"]})
    rpt = Report(str(out), title="Table Test")
    rpt.table("My Table", df, caption="Caption here")
    rpt.build()
    assert out.exists()


def test_raw_table():
    out = TMP / "raw_table.pdf"
    rows = [["Name", "Value"], ["Alpha", "100"], ["Beta", "200"]]
    rpt = Report(str(out), title="Raw Table Test")
    rpt.table("Raw", rows)
    rpt.build()
    assert out.exists()


def test_custom_brand():
    out = TMP / "branded.pdf"
    brand = BrandStyles(primary="#0D1B2A", secondary="#E63946")
    rpt = Report(str(out), title="Branded", brand=brand)
    rpt.section("Section", "Custom brand colours applied.")
    rpt.build()
    assert out.exists()


def test_page_break_and_spacer():
    out = TMP / "paging.pdf"
    rpt = Report(str(out), title="Paging Test")
    rpt.section("Page 1", "Content.")
    rpt.page_break()
    rpt.spacer(10)
    rpt.section("Page 2", "More content.")
    rpt.build()
    assert out.exists()
