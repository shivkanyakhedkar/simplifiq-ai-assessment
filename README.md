# AI-Powered Lead Qualification & Business Audit System

An end-to-end AI automation system that captures prospect information, enriches company data through website scraping, generates personalized AI-powered business audit reports, creates downloadable PDFs, and automatically sends reports via email.

---

# 🚀 Features

- Lead intake form using Streamlit
- Website scraping & company data extraction
- AI-generated personalized business audit reports
- Professional PDF report generation
- Automated email delivery with PDF attachment
- End-to-end workflow automation
- Clean modular architecture

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core backend |
| Streamlit | User interface |
| BeautifulSoup | Website scraping |
| Requests | HTTP requests |
| Groq LLM API | AI report generation |
| ReportLab | PDF generation |
| Resend API | Email automation |
| Python Dotenv | Environment management |

---

# 📌 Workflow

```text
Lead Form Submission
        ↓
Website Scraping
        ↓
Company Data Extraction
        ↓
AI Report Generation
        ↓
PDF Creation
        ↓
Email Delivery



simplifiq-ai-assessment/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── services/
│   ├── scraper.py
│   ├── ai_report.py
│   ├── pdf_generator.py
│   ├── email_service.py
│
├── reports/
│
└── README.md



⚙️ Installation & Setup
1. Clone Repository
git clone <your-repo-url>
cd simplifiq-ai-assessment
2. Create Virtual Environment (Optional)
python -m venv venv
 


Activate environment:

Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables



Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key
RESEND_API_KEY=your_resend_api_key
▶️ Run Application
streamlit run app.py
📄 Example Output



The system generates:

AI-powered business audit report
Professional PDF document
Automated email with PDF attachment
🧠 AI Report Includes
Company Overview
Main Services
Website & Brand Analysis
AI Automation Opportunities
Growth Recommendations
Personalized Insights
⚠️ Assumptions & Limitations
Some websites may block scraping requests
AI report quality depends on extracted website content
Resend free tier only allows sending emails to verified addresses
Report personalization is based on publicly available website data
🔮 Future Improvements
Google Sheets lead logging
Google Drive PDF storage
Competitor analysis
Multi-page website scraping
Better UI/UX enhancements
Dashboard analytics
CRM integrations
📧 Automated Workflow Demonstration


✅ Lead Submission
✅ Website Enrichment
✅ AI Report Generation
✅ PDF Creation
✅ Email Delivery