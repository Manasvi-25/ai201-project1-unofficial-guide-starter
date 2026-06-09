import gradio as gr
from query import ask

def handle_query(question):
    if not question.strip():
        return "Please enter a question.", ""
    result = ask(question)
    sources = "\n".join(f"• {s}" for s in result["sources"])
    return result["answer"], sources

with gr.Blocks(title="SBU CSE Professor Guide") as demo:
    gr.Markdown("# 🎓 SBU CSE Unofficial Professor Guide")
    gr.Markdown("Ask anything about CSE professors and courses at Stony Brook University.")
    
    inp = gr.Textbox(label="Your question", placeholder="e.g. Is Stark's CSE320 hard?")
    btn = gr.Button("Ask")
    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Retrieved from", lines=4)
    
    btn.click(handle_query, inputs=inp, outputs=[answer, sources])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])

demo.launch()