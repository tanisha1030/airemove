import streamlit as st
import re
import random

def remove_ai_patterns(text):
    """Remove common AI writing patterns and make text more natural"""
    
    # Common AI phrases to replace or remove
    ai_phrases = {
        r'\bdelve into\b': ['explore', 'examine', 'look at', 'investigate'],
        r'\bIt\'s worth noting that\b': ['Note that', 'Importantly,', ''],
        r'\bIt is important to note that\b': ['Remember that', 'Keep in mind that', ''],
        r'\bin the realm of\b': ['in', 'regarding', 'about'],
        r'\bleverage\b': ['use', 'utilize', 'employ'],
        r'\brobust\b': ['strong', 'solid', 'effective'],
        r'\bmeticulous\b': ['careful', 'thorough', 'detailed'],
        r'\bseamlessly\b': ['smoothly', 'easily', 'well'],
        r'\bin today\'s world\b': ['today', 'now', 'currently'],
        r'\bat the end of the day\b': ['ultimately', 'finally', 'in the end'],
        r'\bgame-changer\b': ['innovation', 'advancement', 'improvement'],
        r'\bparadigm shift\b': ['major change', 'transformation', 'shift'],
        r'\bIt\'s important to understand that\b': ['Understand that', '', 'Remember'],
        r'\bnavigating the\b': ['dealing with', 'working with', 'handling'],
        r'\blandscape of\b': ['field of', 'area of', 'world of'],
        r'\bunderscore\b': ['emphasize', 'highlight', 'stress'],
        r'\bfacilitate\b': ['help', 'enable', 'support'],
        r'\bmultifaceted\b': ['complex', 'varied', 'diverse'],
        r'\bholistic\b': ['complete', 'comprehensive', 'overall'],
        r'\bsynergy\b': ['cooperation', 'teamwork', 'collaboration'],
    }
    
    # Apply replacements
    result = text
    for pattern, replacements in ai_phrases.items():
        matches = re.finditer(pattern, result, re.IGNORECASE)
        for match in reversed(list(matches)):
            replacement = random.choice(replacements)
            start, end = match.span()
            # Preserve original capitalization
            if result[start].isupper() and replacement:
                replacement = replacement.capitalize()
            result = result[:start] + replacement + result[end:]
    
    # Remove excessive transitional phrases at sentence starts
    result = re.sub(r'\.\s+(Moreover|Furthermore|Additionally|In addition),\s+', '. ', result)
    
    # Simplify overly formal constructions
    result = re.sub(r'\bin order to\b', 'to', result)
    result = re.sub(r'\bdue to the fact that\b', 'because', result)
    result = re.sub(r'\bfor the purpose of\b', 'to', result)
    result = re.sub(r'\bin the event that\b', 'if', result)
    result = re.sub(r'\bprior to\b', 'before', result)
    result = re.sub(r'\bsubsequent to\b', 'after', result)
    
    # Remove hedging language
    result = re.sub(r'\b(essentially|basically|actually|literally)\s+', '', result, flags=re.IGNORECASE)
    
    # Fix spacing issues
    result = re.sub(r'\s+', ' ', result)
    result = re.sub(r'\s+([.,!?;:])', r'\1', result)
    
    return result.strip()

def vary_sentence_structure(text):
    """Add variety to sentence structure"""
    sentences = re.split(r'([.!?])\s+', text)
    
    # Recombine sentences with their punctuation
    combined = []
    for i in range(0, len(sentences)-1, 2):
        if i+1 < len(sentences):
            combined.append(sentences[i] + sentences[i+1])
        else:
            combined.append(sentences[i])
    
    # Occasionally combine short sentences
    result = []
    i = 0
    while i < len(combined):
        sentence = combined[i].strip()
        if i < len(combined) - 1 and len(sentence.split()) < 8 and random.random() < 0.3:
            # Combine with next sentence
            next_sentence = combined[i+1].strip()
            connector = random.choice([', and', ', so', ', but', ';'])
            # Make next sentence lowercase unless it's a proper noun
            if next_sentence:
                next_sentence = next_sentence[0].lower() + next_sentence[1:]
            result.append(sentence + connector + ' ' + next_sentence)
            i += 2
        else:
            result.append(sentence)
            i += 1
    
    return ' '.join(result)

def add_natural_imperfections(text):
    """Add slight natural variations that humans use"""
    result = text
    
    # Occasionally use contractions
    contractions = {
        r'\bdo not\b': "don't",
        r'\bdoes not\b': "doesn't",
        r'\bcan not\b': "can't",
        r'\bcannot\b': "can't",
        r'\bwill not\b': "won't",
        r'\bis not\b': "isn't",
        r'\bare not\b': "aren't",
        r'\bwas not\b': "wasn't",
        r'\bwere not\b': "weren't",
        r'\bhas not\b': "hasn't",
        r'\bhave not\b': "haven't",
        r'\bhad not\b': "hadn't",
    }
    
    for pattern, contraction in contractions.items():
        # Apply contractions randomly (50% chance)
        matches = list(re.finditer(pattern, result, re.IGNORECASE))
        for match in reversed(matches):
            if random.random() < 0.5:
                start, end = match.span()
                result = result[:start] + contraction + result[end:]
    
    return result

def humanize_text(text, use_variations=True, use_contractions=True):
    """Main function to humanize AI-generated text"""
    if not text or not text.strip():
        return text
    
    # Step 1: Remove AI patterns
    result = remove_ai_patterns(text)
    
    # Step 2: Vary sentence structure
    if use_variations:
        result = vary_sentence_structure(result)
    
    # Step 3: Add natural imperfections
    if use_contractions:
        result = add_natural_imperfections(result)
    
    return result

# Streamlit UI
st.set_page_config(
    page_title="AI Text Humanizer",
    page_icon="✍️",
    layout="wide"
)

st.title("✍️ AI Text Humanizer")
st.markdown("Transform AI-generated text into natural, human-like writing by removing common AI patterns and phrases.")

# Sidebar options
with st.sidebar:
    st.header("Options")
    use_variations = st.checkbox("Vary sentence structure", value=True)
    use_contractions = st.checkbox("Use contractions", value=True)
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    This tool removes common AI writing patterns such as:
    - Overused phrases ("delve into", "leverage")
    - Excessive formality
    - Hedging language
    - Repetitive transitions
    
    The result is more natural, human-like text.
    """)

# Main content
col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Text")
    input_text = st.text_area(
        "Paste your AI-generated text here:",
        height=400,
        placeholder="Enter the text you want to humanize..."
    )
    
    process_button = st.button("🔄 Humanize Text", type="primary", use_container_width=True)

with col2:
    st.subheader("Humanized Output")
    
    if process_button:
        if input_text.strip():
            with st.spinner("Processing..."):
                output_text = humanize_text(input_text, use_variations, use_contractions)
                st.text_area(
                    "Result:",
                    value=output_text,
                    height=400,
                    label_visibility="collapsed"
                )
                
                # Statistics
                st.markdown("---")
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Original Length", f"{len(input_text)} chars")
                with col_b:
                    st.metric("New Length", f"{len(output_text)} chars")
                with col_c:
                    diff = len(output_text) - len(input_text)
                    st.metric("Difference", f"{diff:+d} chars")
        else:
            st.warning("Please enter some text to process.")
    else:
        st.text_area(
            "Result will appear here...",
            value="",
            height=400,
            disabled=True,
            label_visibility="collapsed"
        )

# Examples section
with st.expander("📝 See Examples"):
    st.markdown("""
    **Before:** "It's worth noting that in today's world, we need to delve into the realm of artificial intelligence to leverage robust solutions."
    
    **After:** "Note that today, we need to explore artificial intelligence to use strong solutions."
    
    ---
    
    **Before:** "It is important to note that this paradigm shift will facilitate seamless integration in order to achieve our goals."
    
    **After:** "Remember that this major change will help smooth integration to achieve our goals."
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>Made with Streamlit • Remove AI patterns from text</div>",
    unsafe_allow_html=True
)
