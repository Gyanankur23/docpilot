# docpilot 📄

**Generate professional, branded PDF reports with a minimal fluent API.**

```bash
pip install docpilot
```

---

## Quickstart

```python
from docpilot import Report
import pandas as pd

df = pd.DataFrame({
    "Deliverable": ["API Gateway", "Auth Service", "Dashboard"],
    "Status":      ["Complete",   "In Progress",  "Planned"],
    "ETA":         ["—",          "2025-09-05",   "2025-10-01"],
})

rpt = Report("report.pdf", title="Q3 Project Report", company="Acme Ltd")

rpt.title_block("Q3 Project Report", subtitle="Internal Review", date="14 April 2026", version="1.0")
rpt.section("Executive Summary", "All major milestones were met this quarter. "
            "Sprint velocity improved by <b>18 %</b> following process changes.")
rpt.bullets("Key Highlights", [
    "API Gateway shipped ahead of schedule.",
    "Zero critical bugs open at sprint end.",
    "Test coverage raised from 74 % to 88 %.",
])
rpt.table("Deliverables", df, caption="Table 1 – Current project status.")
rpt.page_break()
rpt.section("Next Steps", "See the risk register for open items.")
rpt.build()
```

That's it — a fully paginated, branded PDF is written to `report.pdf`.

---

## Features

| Feature | Method |
|---|---|
| Branded cover title block | `rpt.title_block(...)` |
| Headed text sections | `rpt.section(heading, body)` |
| Bullet lists | `rpt.bullets(heading, items)` |
| Styled tables (DataFrame or raw rows) | `rpt.table(heading, data)` |
| Embedded images with caption | `rpt.image(path, caption)` |
| Page breaks & spacers | `rpt.page_break()` / `rpt.spacer()` |
| Dynamic headers + page-numbered footers | automatic on every page |
| Custom brand colours | `BrandStyles(primary="#...", secondary="#...")` |
| Optional logo in header | `Report(..., logo="logo.png")` |

---

## Custom Branding

```python
from docpilot import Report, BrandStyles

brand = BrandStyles(
    primary="#0D1B2A",    # deep charcoal
    secondary="#E63946",  # red accent
    accent="#F1A208",     # amber
)

rpt = Report(
    "branded.pdf",
    title="Annual Report",
    company="Corp Inc.",
    confidentiality="Strictly Confidential",
    brand=brand,
    logo="assets/logo.png",
)
rpt.title_block("Annual Report 2025")
rpt.section("Message from the CEO", "Dear shareholders, ...")
rpt.build()
```

---

## Raw Table (no Pandas)

```python
rpt.table("Risk Register", [
    ["Risk",                   "Likelihood", "Impact"],   # header row
    ["Third-party API outage", "Low",        "High"  ],
    ["Scope creep",            "High",       "Medium"],
])
```

---

## Installation

```bash
pip install docpilot
```

### From source

```bash
git clone https://github.com/yourusername/docpilot.git
cd docpilot
pip install -e ".[dev]"
```

---

## Publishing to PyPI

```bash
pip install build twine
python -m build
twine upload dist/*
```

---

## License

MIT © Your Name
