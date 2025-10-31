import streamlit as st
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import random

# Download NLTK data (run once)
@st.cache_resource
def download_nltk_data():
    """Download required NLTK data with error handling."""
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('punkt_tab', quiet=True)  # Required for newer NLTK versions
        nltk.download('wordnet', quiet=True)
        nltk.download('omw-1.4', quiet=True)  # Optional but recommended
        return True
    except Exception as e:
        st.error(f"Error downloading NLTK data: {e}")
        return False

# Download data at startup
download_nltk_data()

def get_synonyms(word):
    """Get a list of synonyms for a word using WordNet."""
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            # Filter out the original word and words with underscores
            synonym = lemma.name().replace('_', ' ')
            if synonym.lower() != word.lower():
                synonyms.add(synonym)
    return list(synonyms)

def paraphrase_text(text, intensity=0.3):
    """
    Basic paraphrasing by replacing words with random synonyms.
    This is simplistic and may not produce coherent results for complex text.
    """
    tokens = word_tokenize(text)
    paraphrased = []
    
    for token in tokens:
        if token.isalpha() and len(token) > 3 and random.random() > (1 - intensity):
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
    
    # Rejoin with proper spacing for punctuation
    result = ' '.join(paraphrased)
    # Fix spacing around punctuation
    for punct in [',', '.', '!', '?', ';', ':']:
        result = result.replace(f' {punct}', punct)
    
    return result

st.title("Text Paraphraser (Reduce AI/Plagiarism Detection)")
st.write("""
This app paraphrases input text using synonym replacement to help make it more original.

**Disclaimer:** This is a basic tool for educational purposes. It may not produce high-quality results 
and won't reliably bypass advanced detectors. Use ethically!
""")

# Text input
input_text = st.text_area("Input Text", height=200, placeholder="Paste your text here to paraphrase...")

# Slider for paraphrase intensity
intensity = st.slider("Paraphrase Intensity (higher = more changes)", 0.1, 1.0, 0.3, 0.1)

if st.button("Paraphrase Text"):
    if input_text.strip():
        with st.spinner("Paraphrasing..."):
            output_text = paraphrase_text(input_text, intensity)
        
        st.subheader("Paraphrased Text:")
        st.text_area("Output", value=output_text, height=200, disabled=True)
        
        # Show word change statistics
        original_words = len(input_text.split())
        changed_words = sum(1 for o, p in zip(input_text.split(), output_text.split()) if o != p)
        st.info(f"Changed approximately {changed_words}/{original_words} words ({changed_words/original_words*100:.1f}%)")
        
        st.warning("⚠️ **Important:** Review and edit the output for coherence and accuracy. For better results, consider using advanced AI APIs with proper prompts.")
    else:
        st.warning("Please enter some text to paraphrase.")
