"""
docpilot.styles
---------------
BrandStyles: colour palette + ParagraphStyle registry.
"""

from __future__ import annotations

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm


def _hex(h: str) -> colors.HexColor:
    return colors.HexColor(h)


class BrandStyles:
    """Central registry for colours and paragraph styles.

    Args:
        primary:   Primary HEX colour (default deep navy ``#1B3A5C``).
        secondary: Secondary HEX colour (default teal ``#2E86AB``).
        accent:    Accent HEX colour (default amber ``#F6AE2D``).

    Example::

        brand = BrandStyles(primary="#0D1B2A", secondary="#E63946")
        rpt = Report("out.pdf", title="Report", brand=brand)
    """

    def __init__(
        self,
        primary: str = "#1B3A5C",
        secondary: str = "#2E86AB",
        accent: str = "#F6AE2D",
    ) -> None:
        self.PRIMARY = _hex(primary)
        self.SECONDARY = _hex(secondary)
        self.ACCENT = _hex(accent)
        self.LIGHT_BG = _hex("#F0F4F8")
        self.WHITE = _hex("#FFFFFF")
        self.TEXT_DARK = _hex("#1A1A2E")
        self.TEXT_MUTED = _hex("#6B7280")
        self.ROW_ODD = _hex("#FFFFFF")
        self.ROW_EVEN = _hex("#EBF5FB")
        self.HEADER_BG = self.PRIMARY
        self.HEADER_FG = _hex("#FFFFFF")

        self._styles: dict[str, ParagraphStyle] = self._build()

    def _build(self) -> dict[str, ParagraphStyle]:
        s: dict[str, ParagraphStyle] = {}

        s["doc_title"] = ParagraphStyle("DocTitle", fontName="Helvetica-Bold",
            fontSize=26, textColor=self.PRIMARY, spaceAfter=6*mm, leading=32)
        s["doc_subtitle"] = ParagraphStyle("DocSubtitle", fontName="Helvetica",
            fontSize=13, textColor=self.SECONDARY, spaceAfter=4*mm, leading=18)
        s["h1"] = ParagraphStyle("H1Brand", fontName="Helvetica-Bold",
            fontSize=16, textColor=self.PRIMARY, spaceBefore=8*mm,
            spaceAfter=3*mm, leading=22)
        s["h2"] = ParagraphStyle("H2Brand", fontName="Helvetica-Bold",
            fontSize=12, textColor=self.SECONDARY, spaceBefore=5*mm,
            spaceAfter=2*mm, leading=17)
        s["body"] = ParagraphStyle("BodyBrand", fontName="Helvetica",
            fontSize=10, textColor=self.TEXT_DARK, spaceAfter=4*mm,
            leading=15)
        s["bullet"] = ParagraphStyle("BulletBrand", fontName="Helvetica",
            fontSize=10, textColor=self.TEXT_DARK, spaceAfter=2*mm,
            leftIndent=12, leading=15)
        s["caption"] = ParagraphStyle("CaptionBrand",
            fontName="Helvetica-Oblique", fontSize=8,
            textColor=self.TEXT_MUTED, spaceAfter=3*mm,
            alignment=TA_CENTER, leading=11)
        s["table_header"] = ParagraphStyle("TableHeader",
            fontName="Helvetica-Bold", fontSize=9, textColor=self.WHITE,
            alignment=TA_CENTER, leading=13)
        s["table_cell"] = ParagraphStyle("TableCell", fontName="Helvetica",
            fontSize=9, textColor=self.TEXT_DARK, alignment=TA_LEFT,
            leading=13)
        s["table_cell_right"] = ParagraphStyle("TableCellRight",
            fontName="Helvetica", fontSize=9, textColor=self.TEXT_DARK,
            alignment=TA_RIGHT, leading=13)
        s["footer"] = ParagraphStyle("FooterText", fontName="Helvetica",
            fontSize=8, textColor=self.TEXT_MUTED, alignment=TA_CENTER,
            leading=10)
        return s

    def get(self, name: str) -> ParagraphStyle:
        """Return a registered ParagraphStyle by key."""
        return self._styles[name]
