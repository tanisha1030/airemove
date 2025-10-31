import streamlit as st
import openai
import os

# Set your OpenAI API key here (or use environment variables for security)
# NEVER hardcode your key in production; use Streamlit secrets or env vars.
openai.api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    st.error("Please set your OpenAI API key in Streamlit secrets or environment variables. Get one at openai.com.")

def rewrite_text_with_gpt(text, strength="moderate"):
    """
    Rewrites text using OpenAI's GPT model to make it sound more human-like.
    Strength: 'light' (minor changes), 'moderate' (balanced), 'heavy' (significant rewrite).
    """
    prompts = {
        "light": f"Rewrite the following text with minor changes to make it sound more natural, keeping the original meaning: {text}",
        "moderate": f"Paraphrase the following text in a human-like way, preserving the core ideas but varying the wording: {text}",
        "heavy": f"Completely rewrite the following text as if a human wrote it originally, changing structure and words while keeping the meaning intact: {text}"
    }
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use gpt-4 for better results if available
            messages=[{"role": "user", "content": prompts[strength]}],
            max_tokens=1000,  # Adjust based on text length
            temperature=0.7  # Controls creativity; lower for more consistent output
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error rewriting text: {str(e)}. Check your API key and quota."

st.title("Advanced Text Rewriter (Human-Like Paraphrasing)")
st.write("""
This app uses OpenAI's GPT to rewrite text in a more human-like style.
**Disclaimer:** No tool guarantees 100% undetectability. Use for educational purposes only. Ethical use is crucial – don't use for fraud or plagiarism.
""")

# Text input
input_text = st.text_area("Input Text", height=200, placeholder="Paste your text here to rewrite...")

# Rewrite strength
strength = st.selectbox("Rewrite Strength", ["light", "moderate", "heavy"], index=1)

if st.button("Rewrite Text"):
    if input_text.strip():
        with st.spinner("Rewriting..."):
            output_text = rewrite_text_with_gpt(input_text, strength)
        st.subheader("Rewritten Text:")
        st.text_area("Output", value=output_text, height=200, disabled=True)
        st.info("Tip: Review and edit for accuracy. This isn't perfect – human writing involves personal style.")
    else:
        st.warning("Please enter some text to rewrite.")
