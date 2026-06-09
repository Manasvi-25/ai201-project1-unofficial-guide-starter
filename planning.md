# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
I chose the domain of rating of cse professors in sbu. this is valuable because students need to amke decisions on which clas to take with which professor and its very I chose the domain of SBU CSE professor ratings and reviews. This is useful because students are constantly trying to figure out which classes to take and which professors to take them with, especially in the CSE department where workload, teaching style, and grading can vary a lot from one professor to another. These choices can genuinely affect how manageable a semester feels, so having good information matters.

Right now, this process is pretty scattered and annoying to do manually. You usually end up jumping between RateMyProfessor, Reddit threads, Discord chats, and random student reviews just to get a basic idea of what a professor is like. Even then, the information is often incomplete, outdated, or super subjective, so it takes a lot of effort to piece together something reliable.

Using this project, instead of spending a long time digging through different sources, you can have a system where you can just look up a professor and immediately get a clear summary of student experiences, common themes, and overall sentiment.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | Abid Malik | RMP reviews for CSE220 (Systems Fundamentals) and CSE337 (Scripting Languages) | https://www.ratemyprofessors.com/professor/2968856 — `docs/abid_malik.txt` |
| 2 | Ahmad Esmaili | RMP reviews for CSE214 (Data Structures) and CSE114 (Intro to OOP) | https://www.ratemyprofessors.com/professor/86020 — `docs/ahmed_esmaili.txt` |
| 3 | Christopher Kane | RMP reviews for CSE215 (Logic), CSE216/316 (Functional/Full Stack), CSE310 (Networks) | https://www.ratemyprofessors.com/professor/2515527 — `docs/christopher_kane.txt` |
| 4 | Eugene Stark | RMP reviews for CSE320 (Systems Fundamentals) and CSE306 (Operating Systems) | https://www.ratemyprofessors.com/professor/926577 — `docs/eugene_stark.txt` |
| 5 | Jalaa Hoblos | RMP reviews for CSE101, CSE114 (Intro to OOP), CSE310 (Networks) | https://www.ratemyprofessors.com/professor/2826272 — `docs/jalaa_hoblos.txt` |
| 6 | Michael Ferdman | RMP reviews for CSE356 (Cloud Computing), CSE506 (OS), CSE502 (Computer Architecture) | https://www.ratemyprofessors.com/professor/1825086 — `docs/michael_ferdman.txt` |
| 7 | Paul Fodor | RMP reviews for CSE114 (Intro to OOP), CSE215 (Logic), CSE316 (Full Stack) | https://www.ratemyprofessors.com/professor/1614881 — `docs/paul_fodor.txt` |
| 8 | Pramod Ganapathi | RMP reviews for CSE215 (Discrete Math) and CSE113 | https://www.ratemyprofessors.com/professor/2519551 — `docs/pramod_ganapathi.txt` |
| 9 | Steven Skiena | RMP reviews for CSE373 (Analysis of Algorithms) and CSE519 (Data Science) | https://www.ratemyprofessors.com/professor/394782 — `docs/steven_skiena.txt` |
| 10 | Yifan Sun | RMP reviews for CSE353 (ML), CSE512 (ML Theory), CSE519 (Data Science) | https://www.ratemyprofessors.com/professor/2605339 — `docs/yifan_sun.txt` |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:** 500

**Overlap:** 50

**Reasoning:** I’m using chunk size = 500 and overlap = 50. Each review is usually 2–5 sentences (~200–400 chars), so 500 chars fits one full review plus its metadata like course, professor, difficulty, etc. 

I didn’t go smaller because then you lose context, something like “exams are hard” without course/professor info becomes useless and just matches everything. I didn’t go bigger either because mixing multiple reviews in one chunk makes embeddings messy and less precise since different opinions get blended together.

Overlap = 50 is just a small safety buffer since reviews are already separated cleanly, so we don’t really need a heavy overlap.

Semantic search works well here because users don’t use the exact words from reviews. Like someone might say “brutal” but reviews say “very difficult” or “tons of workload” — embeddings still connect those.

Top-k = 4 because each chunk is one review, so 4 reviews is enough to get a balanced mix of opinions without dumping too much noise on the model.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:** all-MiniLM-L6-v2 via sentence-transformers

**Top-k:** 4

**Production tradeoff reflection:** 

all-MiniLM-L6-v2 is what I’m using for this since it runs locally, is fast, and doesn’t cost anything per request, which makes it a practical choice for this project. But if this were a real deployment, I’d consider a few tradeoffs. For accuracy, OpenAI’s text-embedding-3-small handles nuanced opinion text better, but it comes with per-request API costs. For context length, MiniLM only supports around 256 tokens, which is fine for short student reviews, but it could truncate longer inputs if we scale up. Latency is actually a plus for local models like MiniLM since there’s no network call, so queries stay quick even with multiple users. Multilingual support isn’t needed here since everything is in English, but it would matter if the system expanded to a more diverse student base later.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | How time consuming is CSE214 with Esmaili? | Very time consuming — 7 homeworks due every other week described as mini-projects, pop quizzes require attendance, exams are hard but curved heavily |
| 2 | Which professor should I take for CSE316? | Kane or Fodor — Kane is described as the GOAT for 316, passionate and accessible; Fodor taught it and students found it easy with fair assignments |
| 3 | Is Ganapathi a hard professor? | Yes — one of the hardest in the department, exams cover surprise material not in lectures, only 1/3 of CSE215 students get above C+, overwhelming majority of reviews warn to avoid |
| 4 | Who is a good data science professor? | Skiena — highly rated for CSE519, described as legendary, funny, and a great lecturer; wrote the Algorithm Design Manual; though CSE373 is difficult |
| 5 | Who is the best professor for CSE114? | Fodor — called "the GOAT" in dozens of reviews, records lectures, gives extra credit, very caring; Esmaili is also decent but stricter; Hoblos is widely warned against |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Bias in reviews: RateMyProfessors is naturally biased because people with strong feelings are way more likely to leave reviews. So you mostly get extremes — really happy or really angry students — while neutral experiences rarely show up. That means the data doesn’t always reflect the “average” classroom experience.

2. Outdated course info: Some reviews might be for professors teaching courses they don’t actually teach anymore. Like a 2019 review saying Stark taught CSE320 might not match what’s happening now, which could mess with course planning.

3. Conflicting opinions: Some professors have super split feedback (like half love them, half hate them). In those cases, the system might end up blending everything into a vague summary instead of clearly showing that people actually disagree a lot, which is important info on its own.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

     [.txt files in /docs]
        ↓
   ingest.py
   (load + clean)
        ↓
   chunk_text()
   (size=500, overlap=50)
        ↓
   embed.py
   (all-MiniLM-L6-v2)
        ↓
   ChromaDB
   (vector store)
        ↓
   query.py
   (top-4 retrieval)
        ↓
   Groq llama-3.3-70b
   (answer + sources)
        ↓
   app.py (Gradio UI)

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

1. **ingest.py + chunking** — using Claude
   - give it: Documents table + Chunking Strategy section
   - want: script that loads all .txt from /docs, splits into 500 char chunks with 50 overlap, attaches filename as metadata
   - verify: print 5 chunks and make sure each one has professor name + course in it

2. **embed.py** — using Claude
   - give it: Retrieval Approach section + architecture diagram
   - want: script that embeds chunks with all-MiniLM-L6-v2 and stores in ChromaDB
   - verify: query ChromaDB manually and check source metadata comes back correctly

3. **query.py** — using Claude
   - give it: Retrieval Approach + my 5 eval questions
   - want: function that retrieves top-4 chunks and sends to Groq with grounding prompt, returns answer + sources
   - verify: run eval questions and make sure answers reference actual doc content not hallucinations

4. **app.py** — using Claude
   - give it: query.py output format + Gradio requirements
   - want: simple Gradio UI with question input, answer box, sources box
   - verify: run locally and test all 5 eval questions work

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
