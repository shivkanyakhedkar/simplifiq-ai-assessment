import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            return {
                "success": False,
                "error": f"Status code: {response.status_code}"
            }

        soup = BeautifulSoup(response.text, "lxml")

        title = soup.title.string if soup.title else "No title found"

        paragraphs = soup.find_all("p")

        content = " ".join([
            p.get_text(strip=True)
            for p in paragraphs
        ])

        content = content[:5000]

        return {
            "success": True,
            "title": title,
            "content": content
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }