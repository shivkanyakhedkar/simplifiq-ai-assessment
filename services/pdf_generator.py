from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

import os
from datetime import datetime


def generate_pdf(company, report_text):

    os.makedirs("reports", exist_ok=True)

    filename = f"{company.replace(' ', '_')}_report.pdf"

    filepath = os.path.join("reports", filename)

    doc = SimpleDocTemplate(
        filepath,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        f"<b>AI Business Audit Report - {company}</b>",
        styles['Title']
    )

    story.append(title)

    story.append(Spacer(1, 20))

    date_text = Paragraph(
        f"Generated: {datetime.now()}",
        styles['Normal']
    )

    story.append(date_text)

    story.append(Spacer(1, 20))

    report = Paragraph(
        report_text.replace("\n", "<br/>"),
        styles['BodyText']
    )

    story.append(report)

    doc.build(story)

    return filepath