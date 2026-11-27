import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from pathlib import Path

st.set_page_config(page_title="Study Tip Generator", page_icon="🎓")
st.title("🎓 Study Tip Generator")
st.caption("AI-generated study tips for instructor review.")

folder = Path("./fine_tuned_gpt2")

@st.cache_resource
def load_model(folder_path):
    tok = AutoTokenizer.from_pretrained(folder_path)
    net = AutoModelForCausalLM.from_pretrained(folder_path, low_cpu_mem_usage=True).eval()
    return tok, net

if not (folder / "config.json").exists():
    st.error("Run the fine-tuning step and place the exported model beside this app.")
    st.stop()

topic = st.text_input("Enter a study topic", max_chars=120)
if st.button("Generate"):
    if not topic.strip():
        st.warning("Enter a study topic first.")
        st.stop()

    with st.spinner("Generating study tip..."):
        tokenizer, model = load_model(str(folder))
        inputs = tokenizer("Topic: " + topic.strip() + "\nTip:", return_tensors="pt")
        with torch.inference_mode():
            output = model.generate(**inputs, do_sample=True, top_k=50, top_p=0.95, temperature=0.7, max_new_tokens=45, pad_token_id=tokenizer.eos_token_id)

        tip = tokenizer.decode(output[0, inputs.input_ids.shape[1]:], skip_special_tokens=True).strip()
        st.write(tip or "No text was generated. Try a more specific topic.")
        st.caption("AI-generated text. Review before sharing with students.")