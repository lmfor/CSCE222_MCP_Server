from fastmcp import FastMCP
from pathlib import Path

# Directories
BASE_DIR = Path(__file__).resolve().parent.parent
RESOURCES_DIR = Path(BASE_DIR) / "resources"

# PDF Pointers
LOGIC_PATH = Path(RESOURCES_DIR) / "Logic.pdf"
PREDICATE_LOGIC_PATH = Path(RESOURCES_DIR) / "Predicate_Logic.pdf"
PROOFS_1_PATH = Path(RESOURCES_DIR) / "Proofs_1.pdf"
PROOFS_2_PATH = Path(RESOURCES_DIR) / "Proofs_2.pdf"
SETS_PATH = Path(RESOURCES_DIR) / "Sets.pdf"
FUNCTIONS_PATH = Path(RESOURCES_DIR) / "Functions.pdf"
ALGORITHMS_PATH = Path(RESOURCES_DIR) / "Algorithms_And_Complexities.pdf"

server = FastMCP("CSCE 222 Server")


@server.resource("pdf://logic")
def logic_pdf() -> bytes:
    return LOGIC_PATH.read_bytes()


@server.resource("pdf://predicate_logic")
def predicate_logic_pdf() -> bytes:
    return PREDICATE_LOGIC_PATH.read_bytes()


@server.resource("pdf://proofs_1")
def proofs_1_pdf() -> bytes:
    return PROOFS_1_PATH.read_bytes()


@server.resource("pdf://proofs_2")
def proofs_2_pdf() -> bytes:
    return PROOFS_2_PATH.read_bytes()


@server.resource("pdf://sets")
def sets_pdf() -> bytes:
    return SETS_PATH.read_bytes()


@server.resource("pdf://functions")
def functions_pdf() -> bytes:
    return FUNCTIONS_PATH.read_bytes()


@server.resource("pdf://algorithms")
def algorithms_pdf() -> bytes:
    return ALGORITHMS_PATH.read_bytes()


if __name__ == "__main__":
    server.run()

