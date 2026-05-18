from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def generate_ai_report(company, content):

    try:

        prompt = f"""
        You are an expert AI business consultant.

        Analyze the following company website content.

        Company Name:
        {company}

        Website Content:
        {content}

        Generate a professional business audit report with:

        1. Company Overview
        2. Main Services
        3. Website & Brand Observations
        4. AI Automation Opportunities
        5. Growth Recommendations
        6. Personalized Insights

        Keep the report:
        - professional
        - concise
        - highly personalized
        - business focused
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"AI report generation failed: {str(e)}"