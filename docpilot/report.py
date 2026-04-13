"""
docpilot.report
---------------
``Report`` – the single public class users interact with.

Minimal usage::

    from docpilot import Report
    import pandas as pd

    df = pd.DataFrame({"Item": ["A", "B"], "Value": [100, 200]})

    rpt = Report("report.pdf", title="My Report", company="Acme")
    rpt.title_block("My Report", subtitle="Q3 2025")
    rpt.section("Introduction", "Body text goes here.")
    rpt.bullets("Highlights", ["Point one", "Point two"])
    rpt.table("Results", df)
    rpt.build()
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Sequence

import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    Image,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.flowables import Flowable

from docpilot._canvas import make_page_callback
from docpilot.styles import BrandStyles


class Report:
    """Build a professional PDF report with a fluent, chainable API.

    Args:
        path:            Output PDF file path.
        title:           Document title (shown in header on every page).
        company:         Company / author name (shown in footer).
        confidentiality: Footer confidentiality label.
        brand:           Optional custom :class:`BrandStyles` instance.
        logo:            Optional path to a logo image (PNG / JPEG).
        pagesize:        ReportLab page-size tuple (default A4).
        margins:         ``(left, right, top, bottom)`` in mm. Default 20/20/25/25.

    Example::

        from docpilot import Report, BrandStyles

        brand = BrandStyles(primary="#0D1B2A", secondary="#E63946")
        rpt = Report("out.pdf", title="Annual Report", company="Corp", brand=brand)
        rpt.title_block("Annual Report 2025")
        rpt.section("CEO Letter", "Dear shareholders...")
        rpt.build()
    """

    def __init__(
        self,
        path: str | Path,
        title: str,
        company: str = "",
        confidentiality: str = "Confidential",
        brand: BrandStyles | None = None,
        logo: str | None = None,
        pagesize: tuple[float, float] = A4,
        margins: tuple[float, float, float, float] = (20, 20, 25, 25),
    ) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.brand = brand or BrandStyles()

        lm, rm, tm, bm = (v * mm for v in margins)
        self._doc = SimpleDocTemplate(
            str(self.path),
            pagesize=pagesize,
            leftMargin=lm, rightMargin=rm,
            topMargin=tm, bottomMargin=bm,
            title=title, author=company,
        )
        self._cb = make_page_callback(
            brand=self.brand,
            title=title,
            company=company,
            confidentiality=confidentiality,
            logo_path=logo,
        )
        self._story: list[Flowable] = []

    # ------------------------------------------------------------------
    # Chainable builder methods
    # ------------------------------------------------------------------

    def title_block(
        self,
        title: str,
        subtitle: str = "",
        date: str = "",
        version: str = "",
    ) -> "Report":
        """Add a cover-style title block.

        Args:
            title:    Main heading text.
            subtitle: Optional subtitle.
            date:     Optional date string.
            version:  Optional version tag.

        Returns:
            ``self`` for chaining.
        """
        b = self.brand
        self._story.append(Spacer(1, 20 * mm))
        self._story.append(Paragraph(title, b.get("doc_title")))
        if subtitle:
            self._story.append(Paragraph(subtitle, b.get("doc_subtitle")))
        if date or version:
            parts = [p for p in [date, f"Version {version}" if version else ""] if p]
            self._story.append(Paragraph("  |  ".join(parts), b.get("caption")))
        self._story.append(self._rule())
        return self

    def section(
        self,
        heading: str,
        body: str,
        subheading: str = "",
    ) -> "Report":
        """Add a text section.

        Args:
            heading:    H1-level section heading (can be empty string).
            body:       Body text. Supports ReportLab XML markup
                        (``<b>``, ``<i>``, ``<br/>``, etc.).
            subheading: Optional H2 sub-heading.

        Returns:
            ``self`` for chaining.
        """
        b = self.brand
        elems: list[Flowable] = []
        if heading:
            elems.append(Paragraph(heading, b.get("h1")))
        if subheading:
            elems.append(Paragraph(subheading, b.get("h2")))
        elems.append(Paragraph(body, b.get("body")))
        self._story.append(KeepTogether(elems))
        return self

    def bullets(self, heading: str, items: Sequence[str]) -> "Report":
        """Add a bulleted list section.

        Args:
            heading: Section heading (H1). Pass ``""`` to skip.
            items:   Sequence of bullet strings.

        Returns:
            ``self`` for chaining.
        """
        b = self.brand
        if heading:
            self._story.append(Paragraph(heading, b.get("h1")))
        for item in items:
            self._story.append(Paragraph(f"\u2022  {item}", b.get("bullet")))
        self._story.append(Spacer(1, 4 * mm))
        return self

    def table(
        self,
        heading: str,
        data: pd.DataFrame | list[list[str]],
        col_widths: list[float] | None = None,
        caption: str = "",
    ) -> "Report":
        """Add a styled table from a DataFrame **or** raw row list.

        When a ``list[list[str]]`` is supplied, the first row is used as the
        header row.

        Args:
            heading:    Section heading. Pass ``""`` to skip.
            data:       A :class:`~pandas.DataFrame` or a list of rows.
            col_widths: Optional column widths in points.
            caption:    Optional caption rendered below the table.

        Returns:
            ``self`` for chaining.
        """
        b = self.brand
        if heading:
            self._story.append(Paragraph(heading, b.get("h1")))

        if isinstance(data, pd.DataFrame):
            cells = self._df_cells(data)
        else:
            cells = self._raw_cells(data)

        self._story.append(self._build_table(cells, col_widths))

        if caption:
            self._story.append(Spacer(1, 2 * mm))
            self._story.append(Paragraph(caption, b.get("caption")))
        self._story.append(Spacer(1, 4 * mm))
        return self

    def image(
        self,
        path: str | Path,
        caption: str = "",
        max_width: float = 120 * mm,
        max_height: float = 80 * mm,
    ) -> "Report":
        """Add a centred image.

        Args:
            path:       Path to the image file.
            caption:    Optional caption.
            max_width:  Maximum width in points.
            max_height: Maximum height in points.

        Returns:
            ``self`` for chaining.
        """
        p = Path(path)
        if not p.exists():
            return self
        img = Image(str(p), width=max_width, height=max_height)
        img.hAlign = "CENTER"
        elems: list[Flowable] = [img]
        if caption:
            elems += [Spacer(1, 2 * mm),
                      Paragraph(caption, self.brand.get("caption"))]
        self._story.append(KeepTogether(elems))
        return self

    def spacer(self, height_mm: float = 6) -> "Report":
        """Insert vertical whitespace.

        Args:
            height_mm: Height in millimetres (default 6).

        Returns:
            ``self`` for chaining.
        """
        self._story.append(Spacer(1, height_mm * mm))
        return self

    def page_break(self) -> "Report":
        """Force a page break.

        Returns:
            ``self`` for chaining.
        """
        self._story.append(PageBreak())
        return self

    def build(self) -> Path:
        """Render the story to PDF.

        Returns:
            The :class:`~pathlib.Path` of the written PDF.
        """
        self._doc.build(
            self._story,
            onFirstPage=self._cb,
            onLaterPages=self._cb,
        )
        return self.path

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _rule(self) -> HRFlowable:
        return HRFlowable(width="100%", thickness=0.75,
                          color=self.brand.SECONDARY, spaceAfter=2 * mm)

    def _df_cells(self, df: pd.DataFrame) -> list[list[Paragraph]]:
        b = self.brand
        hdr = [Paragraph(str(c), b.get("table_header")) for c in df.columns]
        rows = [
            [Paragraph(str(v), b.get("table_cell")) for v in row]
            for row in df.itertuples(index=False, name=None)
        ]
        return [hdr] + rows

    def _raw_cells(self, rows: list[list[str]]) -> list[list[Paragraph]]:
        if not rows:
            return []
        b = self.brand
        hdr = [Paragraph(str(c), b.get("table_header")) for c in rows[0]]
        data = [
            [Paragraph(str(c), b.get("table_cell")) for c in row]
            for row in rows[1:]
        ]
        return [hdr] + data

    def _build_table(
        self,
        cells: list[list[Any]],
        col_widths: list[float] | None,
    ) -> Table:
        b = self.brand
        n = len(cells)
        tbl = Table(cells, colWidths=col_widths, repeatRows=1)
        cmds: list[tuple[Any, ...]] = [
            ("BACKGROUND", (0, 0), (-1, 0), b.HEADER_BG),
            ("TEXTCOLOR",  (0, 0), (-1, 0), b.HEADER_FG),
            ("FONTNAME",   (0, 0), (-1, -1), "Helvetica"),
            ("FONTSIZE",   (0, 0), (-1, -1), 9),
            ("TOPPADDING",    (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING",   (0, 0), (-1, -1), 6),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
            ("GRID",      (0, 0), (-1, -1), 0.4, b.TEXT_MUTED),
            ("LINEBELOW", (0, 0), (-1, 0),  1.5, b.SECONDARY),
            ("VALIGN",    (0, 0), (-1, -1), "MIDDLE"),
        ]
        for i in range(1, n):
            bg = b.ROW_ODD if i % 2 == 1 else b.ROW_EVEN
            cmds.append(("BACKGROUND", (0, i), (-1, i), bg))
        tbl.setStyle(TableStyle(cmds))
        return tbl
