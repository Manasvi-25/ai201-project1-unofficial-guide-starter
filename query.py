import os
import chromadb
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("sbu_reviews")
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask(question):
    try:
        # check if query mentions a specific course number
        import re
        course_match = re.search(r'CSE\s*(\d+)', question, re.IGNORECASE)
        
        if course_match:
            course_num = "CSE" + course_match.group(1)
            # get ALL chunks and filter by course number
            all_chunks = collection.get()
            filtered = [
                (doc, meta) for doc, meta in 
                zip(all_chunks["documents"], all_chunks["metadatas"])
                if course_num in doc
            ]
            if filtered:
                docs = [f[0] for f in filtered[:15]]
                sources = list(set(f[1]["source"] for f in filtered[:15]))
                context = "\n\n".join(docs)
            else:
                # fall back to semantic search
                results = collection.query(
                    query_embeddings=model.encode([question]).tolist(),
                    n_results=10
                )
                docs = results["documents"][0]
                sources = list(set([m["source"] for m in results["metadatas"][0]]))
                context = "\n\n".join(docs)
        else:
            results = collection.query(
                query_embeddings=model.encode([question]).tolist(),
                n_results=10
            )
            docs = results["documents"][0]
            sources = list(set([m["source"] for m in results["metadatas"][0]]))
            context = "\n\n".join(docs)

        prompt = f"""You are a helpful assistant for Stony Brook University CSE students.
Answer the question using ONLY the information in the provided student reviews below.
Do not use any outside knowledge.
If the reviews don't contain enough information to answer, say exactly: "I don't have enough information on that."
Be specific — mention professor names, course numbers, and reference what students actually said.
The source filename tells you the professor name (e.g. steven_skiena.txt = Steven Skiena).

Reviews:
{context}

Question: {question}
Answer:"""

        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        answer = response.choices[0].message.content.strip()
        return {"answer": answer, "sources": sources}

    except Exception as e:
        return {"answer": f"Error: {str(e)}", "sources": []}

if __name__ == "__main__":
    test_questions = [
        "Who teaches CS114 and are they good?",
        "Which professor should I take for CSE316?",
        "Who teaches data science CSE519?",
    ]
    
    for q in test_questions:
        print(f"\nQ: {q}")
        result = ask(q)
        print(f"A: {result['answer']}")
        print(f"Sources: {result['sources']}")
        print("-" * 40)