"""CV reader — extracts text from PDF CVs."""

from pypdf import PdfReader


class CVReader:
    """Reads a PDF CV and extracts its text content."""

    def __init__(self, path: str):
        self.path = path
        self.text = ""

    def read(self) -> str:
        """Extract text from all pages of the PDF."""
        reader = PdfReader(self.path)
        pages = [page.extract_text() or "" for page in reader.pages]
        self.text = "\n".join(pages).strip()
        return self.text
