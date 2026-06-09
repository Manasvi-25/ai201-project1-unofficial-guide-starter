import os
import re

DOCS_DIR = "documents/sources"

def load_documents():
    documents = []
    for filename in os.listdir(DOCS_DIR):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCS_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            documents.append({
                "source": filename,
                "text": text
            })
    print(f"Loaded {len(documents)} documents")
    return documents

def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    text = text.strip()
    return text

def chunk_text(text):
    # split on blank lines — each review is naturally separated
    chunks = text.split('\n\n')
    chunks = [c.strip() for c in chunks if len(c.strip()) > 50]
    return chunks

def process_documents():
    documents = load_documents()
    all_chunks = []

    for doc in documents:
        cleaned = clean_text(doc["text"])
        chunks = chunk_text(cleaned)
        
        # extract professor name from filename e.g. steven_skiena.txt -> Steven Skiena
        name_part = doc["source"].replace(".txt", "")
        professor_name = " ".join(word.capitalize() for word in name_part.split("_"))
        
        for i, chunk in enumerate(chunks):
            # prepend professor name to every chunk
            tagged_chunk = f"Professor: {professor_name}\n{chunk}"
            all_chunks.append({
                "source": doc["source"],
                "chunk_index": i,
                "text": tagged_chunk
            })

    print(f"Total chunks: {len(all_chunks)}")
    return all_chunks

if __name__ == "__main__":
    chunks = process_documents()

    print("\n--- SAMPLE CHUNKS ---")
    for i in [0, 10, 20, 30, 40]:
        if i < len(chunks):
            print(f"\n[Chunk {i} | Source: {chunks[i]['source']}]")
            print(chunks[i]['text'])
            print("-" * 40)