import streamlit as st
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import random

# Download NLTK data (run once)
nltk.download('punkt')
nltk.download('wordnet')

def get_synonyms(word):
    """Get a list of synonyms for a word using WordNet."""
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def paraphrase_text(text):
    """
    Basic paraphrasing by replacing words with random synonyms.
    This is simplistic and may not produce coherent results for complex text.
    """
    tokens = word_tokenize(text)
    paraphrased = []
    for token in tokens:
        if token.isalpha() and random.random() > 0.7:  # 30% chance to replace
            synonyms = get_synonyms(token.lower())
            if synonyms:
                replacement = random.choice(synonyms)
                # Preserve case
                if token.isupper():
                    replacement = replacement.upper()
                elif token.istitle():
                    replacement = replacement.capitalize()
                paraphrased.append(replacement)
            else:
                paraphrased.append(token)
        else:
            paraphrased.append(token)
    return ' '.join(paraphrased)

st.title("Text Paraphraser (Reduce AI/Plagiarism Detection)")
st.write("""
This app paraphrases input text using synonym replacement to help make it more original.
**Disclaimer:** This is a basic tool for educational purposes. It may not produce high-quality results and won't reliably bypass advanced detectors. Use ethically!
""")

# Text input
input_text = st.text_area("Input Text", height=200, placeholder="Paste your text here to paraphrase...")

# Slider for paraphrase intensity (not used in this simple version, but can be extended)
intensity = st.slider("Paraphrase Intensity (higher = more changes)", 0.1, 1.0, 0.3)

if st.button("Paraphrase Text"):
    if input_text.strip():
        output_text = paraphrase_text(input_text)
        st.subheader("Paraphrased Text:")
        st.text_area("Output", value=output_text, height=200, disabled=True)
        st.info("Tip: Review and edit the output for coherence. For better results, use AI APIs like GPT-3 with proper prompts.")
    else:
        st.warning("Please enter some text to paraphrase.")
