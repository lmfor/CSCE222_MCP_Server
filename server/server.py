from fastmcp import FastMCP
from pathlib import Path
from pypdf import PdfReader

BASE_DIR = Path(__file__).resolve().parent.parent
PDF_DIR = BASE_DIR / "resources"

server = FastMCP("CSCE 222 Server")

# Load all PDFs once at startup
DOCUMENTS = {}

for pdf_path in PDF_DIR.glob("*.pdf"):
    reader = PdfReader(str(pdf_path))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    DOCUMENTS[pdf_path.stem] = text

server = FastMCP("CSCE 222 Server")


@server.tool
def search_notes(query: str) -> str:
    """
    Very simple keyword search across all PDFs.
    Returns matching excerpts.
    """
    results = []

    for name, text in DOCUMENTS.items():
        if query.lower() in text.lower():
            # Return first 1000 characters around match
            idx = text.lower().find(query.lower())
            snippet = text[max(0, idx - 300): idx + 700]
            results.append(f"\n--- {name} ---\n{snippet}")

    if not results:
        return "No matches found."

    return "\n\n".join(results)


if __name__ == "__main__":
    server.run()
