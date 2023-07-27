from pathlib import Path

def read_hello():
    hello_path = Path(__file__).parent / "hello.txt"
    with hello_path.open(mode="r") as f:
        contents = f.read()
        return contents
