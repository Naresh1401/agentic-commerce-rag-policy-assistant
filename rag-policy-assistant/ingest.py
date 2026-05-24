from __future__ import annotations

from pathlib import Path

POLICY_DIR = Path(__file__).with_name("sample_policies")


def load_chunks():
    chunks = []
    for path in sorted(POLICY_DIR.glob("*.md")):
        paragraphs = [p.strip() for p in path.read_text(encoding="utf-8").split("\n\n") if p.strip()]
        for index, text in enumerate(paragraphs):
            chunks.append({"source": path.name, "chunk_id": f"{path.stem}-{index}", "text": text})
    return chunks


if __name__ == "__main__":
    print({"chunks": len(load_chunks())})
