"""
docpilot._canvas
----------------
Internal canvas-level helpers: page headers, footers, decorative bands.
Not part of the public API.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas

if TYPE_CHECKING:
    from docpilot.styles import BrandStyles

PageCallback = Callable[[Canvas, object], None]


def _draw_header(
    canvas: Canvas,
    doc: object,
    brand: "BrandStyles",
    title: str,
    logo_path: str | None,
) -> None:
    canvas.saveState()
    pw: float = doc.pagesize[0]          # type: ignore[attr-defined]
    ph: float = doc.pagesize[1]          # type: ignore[attr-defined]
    mg: float = doc.leftMargin           # type: ignore[attr-defined]
    hy: float = ph - 18 * mm

    canvas.setStrokeColor(brand.SECONDARY)
    canvas.setLineWidth(1.5)
    canvas.line(mg, hy - 2, pw - mg, hy - 2)

    if logo_path:
        try:
            canvas.drawImage(logo_path, x=mg, y=hy, width=30*mm,
                             height=10*mm, preserveAspectRatio=True,
                             mask="auto")
        except Exception:
            pass

    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(brand.TEXT_MUTED)
    canvas.drawRightString(pw - mg, hy + 3, title)
    canvas.restoreState()


def _draw_footer(
    canvas: Canvas,
    doc: object,
    brand: "BrandStyles",
    company: str,
    confidentiality: str,
) -> None:
    canvas.saveState()
    pw: float = doc.pagesize[0]          # type: ignore[attr-defined]
    mg: float = doc.leftMargin           # type: ignore[attr-defined]
    fy: float = 12 * mm

    canvas.setStrokeColor(brand.PRIMARY)
    canvas.setLineWidth(0.75)
    canvas.line(mg, fy + 6, pw - mg, fy + 6)

    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(brand.TEXT_MUTED)
    if company:
        canvas.drawString(mg, fy, company)
    canvas.drawCentredString(pw / 2, fy, confidentiality)
    canvas.drawRightString(pw - mg, fy, f"Page {canvas.getPageNumber()}")
    canvas.restoreState()


def make_page_callback(
    brand: "BrandStyles",
    title: str,
    company: str,
    confidentiality: str,
    logo_path: str | None,
) -> PageCallback:
    """Return a combined header+footer callback for SimpleDocTemplate."""

    def _cb(canvas: Canvas, doc: object) -> None:
        _draw_header(canvas, doc, brand, title, logo_path)
        _draw_footer(canvas, doc, brand, company, confidentiality)

    return _cb
