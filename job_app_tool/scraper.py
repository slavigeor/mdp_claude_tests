"""Job ad scraper — fetches and parses job postings from URLs."""

import requests
from bs4 import BeautifulSoup


class JobScraper:
    """Fetches a job ad URL and extracts the posting text."""

    # Common selectors for job description content
    SELECTORS = [
        {"class_": "description"},
        {"class_": "job-description"},
        {"class_": "jobsearch-jobDescriptionText"},
        {"class_": "show-more-less-html__markup"},  # LinkedIn
        {"id": "job-details"},
        {"class_": "posting-requirements"},
    ]

    def __init__(self, url: str):
        self.url = url
        self.html = ""
        self.text = ""

    def fetch(self) -> str:
        """Fetch the page HTML."""
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(self.url, headers=headers, timeout=15)
        resp.raise_for_status()
        self.html = resp.text
        return self.html

    def parse(self) -> str:
        """Extract job description text from HTML."""
        soup = BeautifulSoup(self.html, "html.parser")

        # Try known selectors first
        for selector in self.SELECTORS:
            element = soup.find(**selector)
            if element:
                self.text = element.get_text(separator="\n", strip=True)
                return self.text

        # Fallback: grab the largest text block in <main> or <body>
        container = soup.find("main") or soup.find("body")
        if container:
            # Remove nav, header, footer, script, style
            for tag in container.find_all(
                ["nav", "header", "footer", "script", "style"]
            ):
                tag.decompose()
            self.text = container.get_text(separator="\n", strip=True)

        return self.text

    def scrape(self) -> str:
        """Fetch and parse in one call."""
        self.fetch()
        return self.parse()
