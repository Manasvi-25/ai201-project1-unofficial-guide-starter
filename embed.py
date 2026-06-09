import chromadb
from sentence_transformers import SentenceTransformer
from ingest import process_documents

# setup
model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="chroma_db")

# fresh start
try:
    client.delete_collection("sbu_reviews")
except:
    pass

collection = client.create_collection("sbu_reviews")

# load chunks
chunks = process_documents()

# embed and store
texts = [c["text"] for c in chunks]
sources = [c["source"] for c in chunks]
ids = [f"{c['source']}_{c['chunk_index']}" for c in chunks]

print("Embedding chunks...")
embeddings = model.encode(texts, show_progress_bar=True)

collection.add(
    documents=texts,
    embeddings=embeddings.tolist(),
    metadatas=[{"source": s} for s in sources],
    ids=ids
)

print(f"\nStored {collection.count()} chunks in ChromaDB")

# test retrieval with 3 eval questions
test_queries = [
    "How time consuming is CSE214 with Esmaili?",
    "Is Ganapathi a hard professor?",
    "Who is the best professor for CSE114?"
]

print("\n--- RETRIEVAL TESTS ---")
for query in test_queries:
    print(f"\nQuery: {query}")
    results = collection.query(
        query_embeddings=model.encode([query]).tolist(),
        n_results=4
    )
    for i, (doc, meta, dist) in enumerate(zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    )):
        print(f"\n  Result {i+1} | Source: {meta['source']} | Distance: {dist:.3f}")
        print(f"  {doc[:200]}")
    print("-" * 40)