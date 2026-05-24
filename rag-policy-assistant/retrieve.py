from __future__ import annotations

from ingest import load_chunks


def score(query: str, text: str) -> int:
    q = set(query.lower().replace("?", "").split())
    t = set(text.lower().replace(",", "").replace("?", "").split())
    return len(q & t)


def retrieve(query: str, k: int = 3):
    return sorted(load_chunks(), key=lambda chunk: score(query, chunk["text"]), reverse=True)[:k]
