from fastmcp import FastMCP
from pathlib import Path
from pypdf import PdfReader

BASE_DIR = Path(__file__).resolve().parent.parent
PDF_DIR = BASE_DIR / "resources"

server = FastMCP("CSCE 222 Server")

# doc -> list of page texts
DOC_PAGES: dict[str, list[str]] = {}

def load_pdfs():
    for pdf_path in PDF_DIR.glob("*.pdf"):
        reader = PdfReader(str(pdf_path))
        pages = []
        for page in reader.pages:
            pages.append(page.extract_text() or "")
        DOC_PAGES[pdf_path.stem] = pages

load_pdfs()

@server.tool
def list_docs() -> list[str]:
    return sorted(DOC_PAGES.keys())

@server.tool
def search_notes(query: str, max_hits: int = 5) -> list[dict]:
    """
    Return the pages that contain the query.
    """
    q = query.lower()
    hits = []

    for doc, pages in DOC_PAGES.items():
        for i, text in enumerate(pages):
            if q in text.lower():
                # small snippet preview
                idx = text.lower().find(q)
                snippet = text[max(0, idx - 250): idx + 750]
                hits.append({
                    "doc": doc,
                    "page": i,              # 0-indexed
                    "cite": f"{doc} p.{i+1}",
                    "snippet": snippet
                })
                if len(hits) >= max_hits:
                    return hits

    return hits

@server.tool
def get_page(doc: str, page: int) -> dict:
    """
    Return full extracted text for one page.
    """
    if doc not in DOC_PAGES:
        raise ValueError(f"Unknown doc: {doc}")
    if page < 0 or page >= len(DOC_PAGES[doc]):
        raise IndexError("Page out of range")

    return {
        "doc": doc,
        "page": page,
        "cite": f"{doc} p.{page+1}",
        "text": DOC_PAGES[doc][page]
    }

if __name__ == "__main__":
    server.run()