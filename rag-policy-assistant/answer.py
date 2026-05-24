from __future__ import annotations

import json
import sys

from retrieve import retrieve, score


def answer(query: str):
    chunks = retrieve(query)
    if not chunks or score(query, chunks[0]["text"]) == 0:
        return {"answer": "I do not have enough policy context.", "citations": [], "retrieved_chunks": chunks}
    return {"answer": chunks[0]["text"].split("\n")[-1], "citations": [{"source": c["source"], "chunk_id": c["chunk_id"]} for c in chunks if score(query, c["text"]) > 0], "retrieved_chunks": chunks}


if __name__ == "__main__":
    query = " ".join(sys.argv[1:]) or "What happens if an item is out of stock?"
    print(json.dumps(answer(query), indent=2))
