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

**Chunk size:**

**Overlap:**

**Reasoning:**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

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

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
