"""
docpilot
--------
Generate professional, branded PDF reports with a one-liner API.

Quickstart::

    from docpilot import Report
    import pandas as pd

    rpt = Report("output.pdf", title="Q3 Analysis", company="Acme Ltd")
    rpt.title_block("Q3 Analysis", subtitle="Internal Review")
    rpt.section("Overview", "This quarter we exceeded all KPIs...")
    rpt.table("Deliverables", df)
    rpt.build()
"""

from docpilot.report import Report
from docpilot.styles import BrandStyles
from docpilot.version import __version__

__all__ = ["Report", "BrandStyles", "__version__"]
