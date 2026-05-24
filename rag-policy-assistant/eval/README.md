# RAG Evaluation

This folder is reserved for groundedness and citation checks over the local policy corpus.

Run the demo query:

```bash
cd rag-policy-assistant
python answer.py "What happens if an item is out of stock?"
```

Expected behavior: the answer includes cited chunks from `substitutions.md` or refuses unsupported questions with `I do not have enough policy context.`
