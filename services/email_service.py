import resend
import os
import base64

from dotenv import load_dotenv


load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")


def send_email(to_email, company, pdf_path):

    with open(pdf_path, "rb") as f:
        pdf_data = f.read()

    encoded_pdf = base64.b64encode(pdf_data).decode("utf-8")

    resend.Emails.send({

        "from": "onboarding@resend.dev",

        "to": to_email,

        "subject": f"{company} - AI Business Audit Report",

        "html": f"""
        <h2>AI Business Audit Report</h2>

        <p>
        Please find attached your AI-generated report for <b>{company}</b>.
        </p>

        <p>
        Thank you,<br>
        SimplifIQ AI Automation
        </p>
        """,

        "attachments": [
            {
                "filename": f"{company}_report.pdf",
                "content": encoded_pdf
            }
        ]
    })