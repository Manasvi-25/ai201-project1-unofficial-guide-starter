# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain: SBU CSE Professor Reviews

I chose the domain of SBU CSE professor ratings and reviews. This is useful because students are constantly trying to figure out which classes to take and which professors 
to take them with, especially in the CSE department where workload, teaching style, and grading can vary a lot from one professor to another. These choices can genuinely affect how manageable a semester feels, so having good information matters.

Right now this process is pretty scattered and annoying to do manually. You usually end up jumping between RateMyProfessor, Reddit threads, and Discord just to get a basic idea of what a professor is like. Even then the information is often incomplete or outdated. This system lets you just ask a question and get a grounded answer from real student reviews instead.

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->


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

**Chunk size:** One review per chunk — I split on blank lines between reviews rather than 
a fixed character count.

**Overlap:** None. I didn't use overlap because reviews are already self-contained units 
so there's no risk of a key fact being cut across a boundary.

**Why these choices fit your documents:** My documents are lists of student reviews 
separated by blank lines. Every review already contains all the context needed to answer 
a question — professor name, course number, date, grade, and the actual opinion. Splitting 
by blank line means each chunk is exactly one complete student opinion. I tried fixed 
character splitting first (500 chars) but it cut reviews mid-sentence, making chunks 
meaningless — a chunk like "Abid Malik w" has no retrievable signal. I also prepended 
each chunk with the professor's full name extracted from the filename (e.g. 
steven_skiena.txt → "Professor: Steven Skiena") because many reviews don't mention the 
professor's name in the review text itself, which would break retrieval for 
professor-name queries.

**Final chunk count:** 238 chunks across 10 documents

## SAMPLE CHUNKS

[Chunk 1 | Source: abid_malik.txt]
Professor: Abid Malik
Quality: 1.0 | Difficulty: 4.0 | Course: CSE-220 | Date: Jan 3, 2026 | Grade: A
I love systems programming but bro made it horrendous. Very boring lectures and was 
often very rude to students. I don't understand the groups that say he gets too much hate.
----------------------------------------

[Chunk 10 | Source: ahmed_esmaili.txt]
Professor: Ahmed Esmaili
Quality: 3.0 | Difficulty: 3.0 | Course: CSE114 | Date: Aug 22, 2023 | Grade: A
His grading and exams are mostly fair, his lectures aren't the most captivating but he does a decent job explaining the concepts. Generally has a pretty good email response rate. Be careful to show that you are not cheating because he is very cautious about that.
----------------------------------------

[Chunk 20 | Source: ahmed_esmaili.txt]
Professor: Ahmed Esmaili
Quality: 1.0 | Difficulty: 4.0 | Course: CSE311 | Date: May 22, 2020
Worst professor I've ever had at Stony. Every semester there is a scandal of him accusing innocent students of cheating when it was his own fault for poorly organizing the exam links. Barely replies to emails or Piazza.
----------------------------------------

[Chunk 30 | Source: ahmed_esmaili.txt]
Professor: Ahmed Esmaili
Quality: 5.0 | Difficulty: 3.0 | Course: CSE214 | Date: May 29, 2017 | Grade: B+
Exams are fair and he mostly tests you on the theory behind each data structure. Pop quizzes are pretty easy and are mostly there to check attendance. Do all of the homework assignments — you will learn a lot from them.
----------------------------------------

[Chunk 40 | Source: christopher_kane.txt]
Professor: Christopher Kane
Quality: 4.0 | Difficulty: 3.0 | Course: CSE216 | Date: Oct 23, 2024 | Grade: A-
Kane structures his class very well, but it tends to be heavily based on lectures and live-coding examples. The tests are online but include many niche trivia-like questions from the notes, so be sure to study the slides and know them well. Always start HW early because the assignments can take a while.

---
## Retrieval Test Results

**Query 1: "Is Stark's CSE320 worth taking?"**

Top retrieved chunks (source: eugene_stark.txt):
- "Professor: Eugene Stark | Quality: 5.0 | Difficulty: 5.0 | Course: CSE320 | Date: Jan 8, 2021 — Stark is the best professor in the CS department at Stony. This is one of the few CS courses where you will learn a lot."
- "Professor: Eugene Stark | Quality: 4.0 | Difficulty: 5.0 | Course: CSE320 | Date: Dec 7, 2022 — The class is definitely the most difficult one I've taken so far, but you also learn a lot."

Why these chunks are relevant: The query asks about CSE320 with Stark specifically. The embedding model correctly matched "worth taking" with reviews discussing whether the class is valuable despite difficulty — both chunks directly address that tradeoff.

System response summary: Correctly identified CSE320 as very hard but worth it, cited specific reviews, noted heavy workload.
Sources returned: eugene_stark.txt 

---

**Query 2: "Should I avoid Hoblos?"**

Top retrieved chunks (source: jalaa_hoblos.txt):
- "Professor: Jalaa Hoblos | Quality: 1.0 | Difficulty: 5.0 | Course: CSE114 | Date: Dec 27, 2022 — Taking this class is like signing your soul away. Tests are extremely unreasonable."
- "Professor: Jalaa Hoblos | Quality: 5.0 | Difficulty: 3.0 | Course: CSE310 | Date: Dec 19, 2024 — Professor Hoblos is an excellent teacher who truly cares about her students."

Why these chunks are relevant: The query is about whether to avoid a specific professor. Retrieval correctly pulled only Hoblos reviews and surfaced both negative and positive opinions, giving the LLM enough context to give a balanced answer.

System response summary: Correctly showed mixed reviews, warned about strictness and anger issues, noted some positive reviews too. 
Sources returned: jalaa_hoblos.txt 

---

**Query 3: "Which professor should I take for CSE316?"**

Top retrieved chunks (source: christopher_kane.txt, paul_fodor.txt):
- "Professor: Christopher Kane | Quality: 5.0 | Difficulty: 3.0 | Course: CSE316 | Date: Nov 22, 2024 — Records all lectures, gives many examples, great prof, would recommend for any course."
- "Professor: Paul Fodor | Quality: 5.0 | Difficulty: 1.0 | Course: CSE316 | Date: Aug 4, 2021 — The assignments were not hard at all. You just do what you have to do and you will pass with an A or A-."

System response summary: Correctly identified both Kane and Fodor for CSE316, compared their styles, recommended Kane for engagement and Fodor for easier workload.
Sources returned: christopher_kane.txt, paul_fodor.txt 

---
## Query Interface

The interface is a Gradio web app that runs locally at http://localhost:7860.

**Input fields:**
- Your question (text box) — type any natural language question about SBU CSE professors or courses

**Output fields:**
- Answer (text box) — the system's grounded response based on retrieved student reviews
- Retrieved from (text box) — the source filenames the answer was drawn from

**Sample interaction:**

User: Is Ganapathi a hard professor?

Answer: Yes, according to the reviews, Professor Ganapathi is considered a hard 
professor, especially for CSE215. Many students mentioned that his homeworks and tests 
are hard, and the grading is also difficult. One student stated "Homeworks are hard, 
tests are hard, grading is hard. There is no winning." Another student said "Hardest 
course I've ever taken." The majority of reviews gave a difficulty rating of 5.0. 
However, one review for CSE113 mentioned that with effort, his classes can be manageable.

Retrieved from:
- pramod_ganapathi.txt

---
## Example Responses

**Response 1 — grounded answer with source attribution**

Question: how is professor Esmaili?

Answer: Professor Esmaili is a mixed bag according to the reviews. Some students praise 
him as a "Great professor" (Dec 23, 2016, CSE214) and say he's "good and funny" 
(Dec 22, 2018, CSE214), while others criticize him for not being great at explaining 
things and having poorly organized exams. One student even calls him the "Worst professor 
I've ever had at Stony" (May 22, 2020, CSE311). However, many students agree that he 
genuinely cares about his students. Overall, his quality ratings range from 1.0 to 5.0, 
with most being around 3.0 or 4.0.

Retrieved from: • ahmed_esmaili.txt

---

**Response 2 — grounded answer with source attribution**

Question: how hard is CSE320 with Stark?

Answer: CSE320 with Professor Stark is considered very difficult, with many students 
rating difficulty 5.0. One student warned "Start homeworks early or you will fail this 
class" and another said every assignment must start "AT LEAST 14 days beforehand and 
you should spend AT LEAST 40 hours." Despite the difficulty, many students say it's 
worth it — one said "I truly feel I am a better programmer after taking this class."

Retrieved from: • eugene_stark.txt

---

**Response 3 — out-of-scope refusal**

Question: Where is Paris?

Answer: I don't have enough information on that.

Retrieved from: • jalaa_hoblos.txt • ahmed_esmaili.txt • paul_fodor.txt • eugene_stark.txt

---
## Embedding Model

**Model used:** all-MiniLM-L6-v2 via sentence-transformers. I chose this because it runs 
locally with no API key, no rate limits, and no cost — which made it practical for this 
project where I'm running everything on my own machine.

**Production tradeoff reflection:** If I were deploying this for real SBU students, I’d think about a few tradeoffs. For accuracy, text-embedding-3-small handles slangy, opinion-heavy reviews better than MiniLM. MiniLM is limited to ~256 tokens, so longer text can get cut off. Latency is better with MiniLM since it runs locally with no API calls, which helps under heavy use. Multilingual isn’t needed here since reviews are all in English, but could matter later. Overall, it’s a local vs API tradeoff: MiniLM is free and private, while API models are more accurate and easier to update.

---

## Grounded Generation

**System prompt grounding instruction:** I restricted the LLM by giving it an explicit 
instruction at the start of every prompt:

"Answer the question using ONLY the information in the provided student reviews below. 
Do not use any outside knowledge. If the reviews don't contain enough information to 
answer, say exactly: 'I don't have enough information on that.'"

I also added a keyword pre-filter, if the query contains a course number like CSE316, 
my code skips semantic search and directly filters all chunks for that course number. 
This stops the model from pulling in loosely related chunks about other courses.

**How source attribution is surfaced in the response:** Source attribution is handled 
programmatically — after generation I extract the source filenames from ChromaDB metadata 
and display them in a separate "Retrieved from" box in the Gradio UI. This way attribution 
is always shown regardless of what the LLM says, since it comes from the pipeline not 
the model.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | How time consuming is CSE214 with Esmaili? | Very time consuming — 7 homeworks due every other week, pop quizzes, hard exams but curved | Correctly identified HWs as mini-projects, said to start early, noted summer section is worse | Relevant | Accurate |
| 2 | Which professor should I take for CSE316? | Kane or Fodor — Kane is GOAT for 316, Fodor taught it and students found it easy | Correctly identified both Kane and Fodor, compared difficulty ratings, gave recommendation based on student preference | Relevant | Accurate |
| 3 | Is Ganapathi a hard professor? | Yes — surprise exam material, only 1/3 pass CSE215, majority warn to avoid | Correctly said yes, cited specific reviews, mentioned difficulty 5.0 ratings, noted one positive review for balance | Relevant | Accurate |
| 4 | Who teaches data science CSE519? | Skiena and Yifan Sun — Skiena highly rated, Sun newer with fewer reviews | Named both Skiena and Sun but gave no detail about what students said about either professor | Partially relevant | Partially accurate |
| 5 | Who teaches CS114 and are they good? | Fodor most recommended, Hoblos warned against, Esmaili mixed | Only mentioned Fodor positively, missed Hoblos and Esmaili entirely | Partially relevant | Partially accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

**Question that failed:** Who teaches object oriented programming?

**What the system returned:** "I don't have enough information on that."

**Root cause (tied to a specific pipeline stage):** This is a retrieval failure. My 
documents use course numbers like CSE114 and short names like "Intro to OOP" — nobody 
writes "object oriented programming" in a Rate My Professor review. So when the embedding 
model tries to match that query, it finds nothing close enough. The keyword pre-filter 
also doesn't help since there's no course number in the query. The answer is in the docs, 
the system just can't connect the terminology.

**What you would change to fix it:** Add a simple alias map that converts common topic 
names to course numbers before retrieval — like "object oriented programming" → "CSE114" 
or "data structures" → "CSE214". That way the keyword filter would kick in and pull the 
right chunks even when the user doesn't know the course number.

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:** Writing out the chunking strategy 
in planning.md before coding made me think about the structure of my documents before 
touching any code. When I actually ran the pipeline and saw chunks getting cut mid-sentence, 
I already knew why — I had thought through what a "good chunk" looked like for review-style 
text. Without the spec I probably would have just left the broken chunks and moved on.

**One way your implementation diverged from the spec, and why:** I first planned to use fixed 500-char chunks with 50-char overlap, but later switched to splitting by blank lines. When I checked the output, fixed chunks were breaking reviews in weird places and losing context. Blank-line splitting just made more sense since each review is already a full unit, so there was no reason to slice it up. I also added a simple course-number keyword filter that wasn’t in the plan, because semantic search alone was sometimes pulling irrelevant courses.

---

## AI Usage

**Instance 1**
- *What I gave the AI:* My Chunking Strategy section and Documents table from planning.md, 
  and asked Claude to implement ingest.py that loads all .txt files and splits them into 
  500 char chunks with 50 char overlap.
- *What it produced:* A working script that loaded documents and split by fixed character 
  count with overlap.
- *What I changed or overrode:* Switched from fixed 500-char splitting to blank-line 
  splitting after seeing the output was cutting reviews mid-sentence. Later added 
  professor name prepending to every chunk because retrieval was failing for queries that 
  didn't include the professor's name.

**Instance 2**
- *What I gave the AI:* My Retrieval Approach section and eval questions, and asked Claude 
  to implement query.py that retrieves top-4 chunks and sends them to Groq with a grounding 
  prompt.
- *What it produced:* A working query function with a grounding prompt and source attribution.
- *What I changed or overrode:* Bumped k from 4 to 10 after seeing retrieval was missing 
  relevant chunks. Also tightened the prompt after the system was returning "I don't have enough information" 
  for questions that should have worked.
