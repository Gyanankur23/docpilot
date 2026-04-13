"""
example.py
----------
Minimal demo — run after `pip install docpilot`.
Generates example_report.pdf in the current directory.
"""

from docpilot import Report
import pandas as pd

df = pd.DataFrame({
    "Deliverable": ["API Gateway", "Auth Service", "Dashboard"],
    "Status":      ["Complete",   "In Progress",  "Planned"],
    "ETA":         ["—",          "2025-09-05",   "2025-10-01"],
})

rpt = Report("example_report.pdf", title="Q3 Project Report", company="Acme Ltd")

rpt.title_block(
    "Q3 Project Report",
    subtitle="Internal Review",
    date="14 April 2026",
    version="1.0",
)
rpt.section(
    "Executive Summary",
    "All major milestones were met this quarter. "
    "Sprint velocity improved by <b>18 %</b> following process changes.",
)
rpt.bullets("Key Highlights", [
    "API Gateway shipped ahead of schedule.",
    "Zero critical bugs open at sprint end.",
    "Test coverage raised from 74 % to 88 %.",
])
rpt.table("Deliverables", df, caption="Table 1 – Current project status.")
rpt.page_break()
rpt.section("Next Steps", "See the risk register for open items.")
rpt.build()

print("Done → example_report.pdf")
