import streamlit as st

from services.scraper import scrape_website
from services.ai_report import generate_ai_report
from services.pdf_generator import generate_pdf
from services.email_service import send_email


st.set_page_config(
    page_title="SimplifIQ AI Automation",
    layout="centered"
)

st.title("SimplifIQ AI Lead Automation")

st.write(
    "Submit company details to generate an AI audit report."
)

with st.form("lead_form"):

    name = st.text_input("Your Name")

    email = st.text_input("Your Email")

    company = st.text_input("Company Name")

    website = st.text_input("Company Website")

    submitted = st.form_submit_button(
        "Generate Audit"
    )


if submitted:

    # Basic validation
    if not name or not email or not company or not website:

        st.warning("Please fill all fields.")

    else:

        # Add https if missing
        if not website.startswith("http"):
            website = "https://" + website

        st.info("Scraping website...")

        result = scrape_website(website)

        if result["success"]:

            st.success("Website scraped successfully!")

            st.subheader("Website Title")

            st.write(result["title"])

            st.subheader("Extracted Website Content")

            st.write(
                result["content"][:1000]
            )

            st.info("Generating AI audit report...")

            report = generate_ai_report(
                company,
                result["content"]
            )

            st.subheader("AI Audit Report")

            st.write(report)

            st.info("Generating PDF report...")

            pdf_path = generate_pdf(
                company,
                report
            )

            st.success("PDF generated successfully!")

            with open(pdf_path, "rb") as f:

                st.download_button(
                    label="Download PDF Report",
                    data=f,
                    file_name=f"{company}_report.pdf",
                    mime="application/pdf"
                )

            st.info("Sending email...")

            send_email(
                email,
                company,
                pdf_path
            )

            st.success("Email sent successfully!")

        else:

            st.error(result["error"])