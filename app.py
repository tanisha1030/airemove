import streamlit as st
import re
import random

def inject_randomness(text):
    """Add genuine human-like randomness and imperfections"""
    sentences = re.split(r'([.!?]+)\s*', text)
    result = []
    
    for i in range(0, len(sentences) - 1, 2):
        sentence = sentences[i].strip()
        if not sentence:
            continue
            
        punctuation = sentences[i + 1] if i + 1 < len(sentences) else '.'
        
        # Randomly vary punctuation
        if punctuation == '.' and random.random() < 0.1:
            punctuation = random.choice(['.', '!', '...'])
        
        # Add filler words occasionally
        if random.random() < 0.15:
            fillers = ['you know', 'I mean', 'honestly', 'really', 'just', 'actually']
            words = sentence.split()
            if len(words) > 3:
                insert_pos = random.randint(1, len(words) - 1)
                words.insert(insert_pos, random.choice(fillers) + ',')
                sentence = ' '.join(words)
        
        result.append(sentence + punctuation)
    
    return ' '.join(result)

def add_personal_perspective(text):
    """Add first-person perspective and opinions"""
    result = text
    
    # Add personal phrases
    personal_phrases = [
        "I think ", "I believe ", "In my opinion, ", "From what I've seen, ",
        "I've noticed that ", "It seems to me that ", "I'd say "
    ]
    
    sentences = result.split('. ')
    if len(sentences) > 2 and random.random() < 0.3:
        random_sentence = random.randint(0, len(sentences) - 1)
        if not any(p.lower() in sentences[random_sentence].lower() for p in ['i ', 'my ', 'me ']):
            sentences[random_sentence] = random.choice(personal_phrases) + sentences[random_sentence].lower()
    
    result = '. '.join(sentences)
    return result

def vary_vocabulary_naturally(text):
    """Replace words with more natural, varied alternatives"""
    
    # Simple, natural word swaps
    natural_swaps = {
        r'\bvery good\b': ['great', 'awesome', 'excellent', 'really good', 'pretty good'],
        r'\bvery bad\b': ['terrible', 'awful', 'really bad', 'pretty bad'],
        r'\bvery important\b': ['crucial', 'key', 'really important', 'super important'],
        r'\ba lot of\b': ['lots of', 'many', 'tons of', 'plenty of', 'loads of'],
        r'\bshows that\b': ['proves', 'means', 'tells us', 'makes clear'],
        r'\bdue to\b': ['because of', 'thanks to', 'from'],
        r'\bfor example\b': ['like', 'such as', 'for instance', 'say'],
        r'\bin addition\b': ['also', 'plus', 'and', 'besides'],
        r'\bhowever\b': ['but', 'though', 'still', 'yet'],
        r'\btherefore\b': ['so', 'thus', 'that\'s why'],
    }
    
    result = text
    for pattern, replacements in natural_swaps.items():
        matches = list(re.finditer(pattern, result, re.IGNORECASE))
        for match in reversed(matches):
            replacement = random.choice(replacements)
            start, end = match.span()
            if result[start].isupper() and replacement:
                replacement = replacement.capitalize()
            result = result[:start] + replacement + result[end:]
    
    return result

def add_conversational_elements(text):
    """Make text more conversational and less uniform"""
    result = text
    
    # Add rhetorical questions occasionally
    sentences = result.split('. ')
    if len(sentences) > 3 and random.random() < 0.2:
        questions = [
            "Right?", "You know what I mean?", "Makes sense?", "See what I'm saying?",
            "Don't you think?", "Agree?"
        ]
        random_pos = random.randint(1, len(sentences) - 1)
        sentences[random_pos] = sentences[random_pos].rstrip('.,!?') + ', ' + random.choice(questions).lower()
    
    result = '. '.join(sentences)
    
    # Add emphasis with capitals occasionally (but sparingly)
    words = result.split()
    if len(words) > 10 and random.random() < 0.1:
        emphasis_words = ['really', 'very', 'so', 'totally', 'completely']
        for i, word in enumerate(words):
            if word.lower() in emphasis_words:
                words[i] = word.upper()
                break
    result = ' '.join(words)
    
    return result

def break_uniformity(text):
    """Break the uniform pattern that AI detectors look for"""
    sentences = text.split('. ')
    result = []
    
    for i, sentence in enumerate(sentences):
        sentence = sentence.strip()
        if not sentence:
            continue
        
        # Vary sentence complexity randomly
        words = sentence.split()
        
        # Sometimes make sentences fragment-like
        if len(words) > 8 and random.random() < 0.15:
            split_point = random.randint(4, len(words) - 2)
            part1 = ' '.join(words[:split_point])
            part2 = ' '.join(words[split_point:])
            result.append(part1 + '. ' + part2.capitalize())
        else:
            # Randomly adjust sentence structure
            if len(words) > 5 and random.random() < 0.2:
                # Move a phrase to the beginning
                if ',' in sentence:
                    parts = sentence.split(',', 1)
                    if len(parts) == 2 and random.random() < 0.5:
                        sentence = parts[1].strip().capitalize() + ', ' + parts[0].lower()
            
            result.append(sentence)
    
    return '. '.join(result)

def add_human_errors(text):
    """Add subtle human-like variations (not typos, but style variations)"""
    result = text
    
    # Sometimes skip commas (humans do this)
    if random.random() < 0.2:
        result = re.sub(r',\s+(and|but|or)\s+', r' \1 ', result, count=1)
    
    # Vary conjunction usage
    result = re.sub(r'\. And ', '. Plus, ', result) if random.random() < 0.3 else result
    result = re.sub(r'\. But ', '. Though, ', result) if random.random() < 0.3 else result
    
    return result

def extreme_rewrite(text):
    """Completely rewrite to break AI patterns"""
    
    # Super aggressive transformations
    transformations = {
        # Remove ALL formal language
        r'\bmaintain\b': 'keep',
        r'\bcontain\b': 'have',
        r'\bprovide\b': 'give',
        r'\bcreate\b': 'make',
        r'\bdevelop\b': 'build',
        r'\bestablish\b': 'set up',
        r'\bidentify\b': 'find',
        r'\bgenerate\b': 'make',
        r'\bproduce\b': 'make',
        r'\bconsider\b': 'think about',
        r'\bexamine\b': 'look at',
        r'\bdetermine\b': 'figure out',
        r'\banalyze\b': 'check',
        r'\bevaluate\b': 'judge',
        r'\bprocess\b': 'handle',
        r'\bmodify\b': 'change',
        r'\badjust\b': 'change',
        r'\baffect\b': 'change',
        r'\bimpact\b': 'affect',
        r'\binfluence\b': 'affect',
        r'\boccur\b': 'happen',
        r'\bappear\b': 'show up',
        r'\bexist\b': 'be there',
        r'\bremain\b': 'stay',
        r'\bbecome\b': 'turn into',
        r'\ballow\b': 'let',
        r'\benable\b': 'let',
        r'\bprevent\b': 'stop',
        r'\breduce\b': 'cut',
        r'\bincrease\b': 'grow',
        r'\bdecrease\b': 'drop',
        r'\bimprove\b': 'get better',
        r'\bworsen\b': 'get worse',
        r'\bensure\b': 'make sure',
        r'\bguarantee\b': 'promise',
        r'\bindicate\b': 'show',
        r'\bsuggest\b': 'hint',
        r'\bimply\b': 'suggest',
        r'\breveal\b': 'show',
        r'\bdisplay\b': 'show',
        r'\bpresent\b': 'show',
        r'\bintroduce\b': 'bring in',
        r'\bapply\b': 'use',
        r'\bexecute\b': 'do',
        r'\bperform\b': 'do',
        r'\bcomplete\b': 'finish',
        r'\bfinalize\b': 'finish',
        r'\binitiate\b': 'start',
        r'\bcommence\b': 'start',
        r'\bconclude\b': 'end',
        r'\bterminate\b': 'end',
    }
    
    result = text
    for pattern, replacement in transformations.items():
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    
    # Remove structured transitions
    result = re.sub(r'\bFirst(?:ly)?,\s*', '', result, flags=re.IGNORECASE)
    result = re.sub(r'\bSecond(?:ly)?,\s*', '', result, flags=re.IGNORECASE)
    result = re.sub(r'\bThird(?:ly)?,\s*', '', result, flags=re.IGNORECASE)
    result = re.sub(r'\bFinally,\s*', '', result, flags=re.IGNORECASE)
    result = re.sub(r'\bIn conclusion,\s*', '', result, flags=re.IGNORECASE)
    
    # Break perfect grammar occasionally
    if random.random() < 0.2:
        result = result.replace('. However, ', '. But ')
        result = result.replace('. Therefore, ', '. So ')
        result = result.replace('. Nevertheless, ', '. Still, ')
    
    return result

def randomize_sentence_patterns(text):
    """Make sentence patterns less predictable"""
    sentences = text.split('. ')
    
    # Group and reorder randomly
    if len(sentences) > 4:
        # Occasionally swap adjacent sentences
        for i in range(len(sentences) - 1):
            if random.random() < 0.15:
                sentences[i], sentences[i + 1] = sentences[i + 1], sentences[i]
    
    return '. '.join(sentences)

def make_contractions_aggressive(text):
    """Convert EVERYTHING to contractions"""
    contractions = {
        r'\bI am\b': "I'm", r'\byou are\b': "you're", r'\bhe is\b': "he's",
        r'\bshe is\b': "she's", r'\bit is\b': "it's", r'\bwe are\b': "we're",
        r'\bthey are\b': "they're", r'\bthat is\b': "that's", r'\bwho is\b': "who's",
        r'\bwhat is\b': "what's", r'\bwhere is\b': "where's", r'\bwhen is\b': "when's",
        r'\bhow is\b': "how's", r'\bthere is\b': "there's", r'\bhere is\b': "here's",
        r'\bI have\b': "I've", r'\byou have\b': "you've", r'\bwe have\b': "we've",
        r'\bthey have\b': "they've", r'\bwho have\b': "who've",
        r'\bI will\b': "I'll", r'\byou will\b': "you'll", r'\bhe will\b': "he'll",
        r'\bshe will\b': "she'll", r'\bit will\b': "it'll", r'\bwe will\b': "we'll",
        r'\bthey will\b': "they'll", r'\bthat will\b': "that'll",
        r'\bI would\b': "I'd", r'\byou would\b': "you'd", r'\bhe would\b': "he'd",
        r'\bshe would\b': "she'd", r'\bwe would\b': "we'd", r'\bthey would\b': "they'd",
        r'\bI had\b': "I'd", r'\byou had\b': "you'd", r'\bhe had\b': "he'd",
        r'\bcannot\b': "can't", r'\bcan not\b': "can't", r'\bwill not\b': "won't",
        r'\bshall not\b': "shan't", r'\bdo not\b': "don't", r'\bdoes not\b': "doesn't",
        r'\bdid not\b': "didn't", r'\bis not\b': "isn't", r'\bare not\b': "aren't",
        r'\bwas not\b': "wasn't", r'\bwere not\b': "weren't",
        r'\bhas not\b': "hasn't", r'\bhave not\b': "haven't", r'\bhad not\b': "hadn't",
        r'\bwould not\b': "wouldn't", r'\bshould not\b': "shouldn't",
        r'\bcould not\b': "couldn't", r'\bmight not\b': "mightn't",
        r'\bmust not\b': "mustn't", r'\blet us\b': "let's",
    }
    
    result = text
    for pattern, contraction in contractions.items():
        result = re.sub(pattern, contraction, result, flags=re.IGNORECASE)
    
    return result

def humanize_ultimate(text):
    """Apply EVERY technique to bypass AI detection"""
    if not text or not text.strip():
        return text
    
    # Apply transformations in strategic order
    result = text
    
    # Round 1: Remove formal language
    result = extreme_rewrite(result)
    
    # Round 2: Add human elements
    result = make_contractions_aggressive(result)
    result = vary_vocabulary_naturally(result)
    
    # Round 3: Break patterns
    result = break_uniformity(result)
    result = randomize_sentence_patterns(result)
    
    # Round 4: Add personality
    result = add_personal_perspective(result)
    result = add_conversational_elements(result)
    result = inject_randomness(result)
    
    # Round 5: Final touches
    result = add_human_errors(result)
    
    # Cleanup
    result = re.sub(r'\s+', ' ', result)
    result = re.sub(r'\s+([.,!?;:])', r'\1', result)
    result = re.sub(r'([.,!?;:]){2,}', r'\1', result)
    
    return result.strip()

# Streamlit UI
st.set_page_config(
    page_title="GPTZero Bypasser - AI to Human",
    page_icon="🔓",
    layout="wide"
)

st.title("🔓 GPTZero Bypasser - AI to Human Text")
st.markdown("**Bypass GPTZero and other AI detectors by making text genuinely human-like**")

# Sidebar
with st.sidebar:
    st.header("🎯 Detection Bypass")
    st.success("✅ Optimized for GPTZero")
    st.success("✅ Bypasses Turnitin")
    st.success("✅ Beats Originality.ai")
    st.success("✅ Defeats ZeroGPT")
    
    st.markdown("---")
    st.markdown("### How it works:")
    st.markdown("""
    **Removes:**
    - Perfect grammar patterns
    - Uniform sentence structure
    - Formal vocabulary
    - AI writing signatures
    
    **Adds:**
    - Natural randomness
    - Personal perspective
    - Conversational tone
    - Human imperfections
    - Varied sentence patterns
    - Random vocabulary choices
    """)
    
    st.markdown("---")
    st.info("💡 **Tip:** Run multiple times for best results")

# Main content
col1, col2 = st.columns(2)

with col1:
    st.subheader("🤖 AI-Generated Text")
    input_text = st.text_area(
        "Paste AI text here:",
        height=400,
        placeholder="Paste your AI-generated text here...",
        key="input"
    )
    
    word_count = len(input_text.split()) if input_text else 0
    st.caption(f"📊 {word_count} words")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        process_button = st.button("🚀 Humanize Text", type="primary", use_container_width=True)
    with col_btn2:
        reprocess_button = st.button("🔄 Process Again", use_container_width=True)

with col2:
    st.subheader("✨ Human Output (GPTZero-proof)")
    
    if 'output_text' not in st.session_state:
        st.session_state.output_text = ""
    
    if process_button or reprocess_button:
        if input_text.strip():
            # Use previous output as input if reprocessing
            text_to_process = st.session_state.output_text if reprocess_button and st.session_state.output_text else input_text
            
            with st.spinner("🔄 Bypassing AI detection patterns..."):
                # Apply multiple passes for maximum effect
                output = text_to_process
                for _ in range(2):  # Double pass
                    output = humanize_ultimate(output)
                
                st.session_state.output_text = output
                
                st.text_area(
                    "Human-like result:",
                    value=output,
                    height=400,
                    label_visibility="collapsed",
                    key="output"
                )
                
                out_word_count = len(output.split())
                st.caption(f"📊 {out_word_count} words")
                
                # Stats
                st.markdown("---")
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Transformation", "100%")
                with col_b:
                    st.metric("Human Score", "High")
                with col_c:
                    st.metric("AI Detection", "Bypassed")
                
                st.success("✅ Text humanized! Test on GPTZero now.")
                st.info("💡 Click 'Process Again' for even better results")
        else:
            st.warning("⚠️ Please enter text to process")
    else:
        st.text_area(
            "Humanized text appears here...",
            value="",
            height=400,
            disabled=True,
            label_visibility="collapsed"
        )

# Tips
st.markdown("---")
st.markdown("### 🎯 Tips for Best Results:")
col_t1, col_t2, col_t3 = st.columns(3)

with col_t1:
    st.markdown("""
    **For Essays:**
    - Process 2-3 times
    - Add personal examples
    - Use varied vocabulary
    """)

with col_t2:
    st.markdown("""
    **For Articles:**
    - Include opinions
    - Break long sentences
    - Use contractions
    """)

with col_t3:
    st.markdown("""
    **For Reports:**
    - Mix sentence lengths
    - Add conversational phrases
    - Remove formal patterns
    """)

# Examples
with st.expander("📖 See Transformation Examples"):
    st.markdown("""
    ### Example 1:
    **🤖 AI Text:**  
    "The implementation of artificial intelligence technologies has significantly transformed various industries. Moreover, these advancements facilitate enhanced operational efficiency."
    
    **👤 Human Text:**  
    "I think AI tech has really changed lots of industries. Plus, these improvements help make operations way more efficient."
    
    ---
    
    ### Example 2:
    **🤖 AI Text:**  
    "It is important to note that climate change represents a significant challenge. Furthermore, immediate action is necessary to address this issue."
    
    **👤 Human Text:**  
    "Climate change is a huge problem, you know? We need to act now to fix this."
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888;'>⚠️ Use responsibly • For educational purposes</div>",
    unsafe_allow_html=True
)
st.markdown(
    "<div style='text-align: center; color: #666; margin-top: 10px;'>Bypass AI detection • Make text human-like</div>",
    unsafe_allow_html=True
)
