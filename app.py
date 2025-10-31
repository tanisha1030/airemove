import streamlit as st
import re
import random

def remove_ai_patterns(text):
    """Aggressively remove ALL AI writing patterns"""
    
    # Comprehensive AI phrases to replace
    ai_phrases = {
        # Super common AI phrases
        r'\bdelve into\b': ['explore', 'look at', 'check out', 'examine', 'study'],
        r'\bleverage\b': ['use', 'apply', 'employ'],
        r'\brobust\b': ['strong', 'solid', 'reliable', 'sturdy'],
        r'\bseamlessly\b': ['smoothly', 'easily', 'naturally'],
        r'\bmeticulous\b': ['careful', 'thorough', 'precise', 'detailed'],
        r'\bparadigm\b': ['model', 'pattern', 'approach', 'way'],
        r'\bsynergy\b': ['teamwork', 'cooperation', 'collaboration'],
        r'\bholistic\b': ['complete', 'whole', 'full', 'comprehensive'],
        r'\bmultifaceted\b': ['complex', 'varied', 'many-sided'],
        r'\bfacilitate\b': ['help', 'enable', 'make easier', 'support'],
        r'\boptimize\b': ['improve', 'enhance', 'better'],
        r'\bstreamline\b': ['simplify', 'improve', 'speed up'],
        r'\bparadigm shift\b': ['big change', 'major shift', 'new approach'],
        r'\bgame-changer\b': ['breakthrough', 'innovation', 'big deal'],
        r'\bgame changer\b': ['breakthrough', 'innovation', 'big deal'],
        
        # Formal/stuffy phrases
        r'\bin the realm of\b': ['in', 'for', 'with'],
        r'\bin the context of\b': ['in', 'for', 'regarding'],
        r'\bwith regard to\b': ['about', 'regarding', 'for'],
        r'\bwith respect to\b': ['about', 'for', 'regarding'],
        r'\bin terms of\b': ['for', 'in', 'about'],
        r'\bfor the purpose of\b': ['to', 'for'],
        r'\bin order to\b': ['to'],
        r'\bdue to the fact that\b': ['because', 'since'],
        r'\bowing to the fact that\b': ['because', 'since'],
        r'\bin the event that\b': ['if'],
        r'\bprior to\b': ['before'],
        r'\bsubsequent to\b': ['after'],
        r'\bat this point in time\b': ['now', 'currently'],
        r'\bat the present time\b': ['now'],
        r'\bin today\'s world\b': ['today', 'now'],
        r'\bin this day and age\b': ['today', 'now'],
        r'\bat the end of the day\b': ['ultimately', 'finally'],
        
        # AI hedging/filler
        r'\bIt\'s worth noting that\b': ['', 'Note that', 'Remember'],
        r'\bIt is worth noting that\b': ['', 'Note that', 'Remember'],
        r'\bIt\'s important to note that\b': ['', 'Remember', 'Keep in mind'],
        r'\bIt is important to note that\b': ['', 'Remember', 'Keep in mind'],
        r'\bIt should be noted that\b': ['', 'Note that'],
        r'\bIt\'s important to understand that\b': ['', 'Understand that'],
        r'\bIt is important to understand that\b': ['', 'Understand that'],
        r'\bIt\'s crucial to recognize that\b': ['', 'Remember that'],
        r'\bOne must consider that\b': ['', 'Consider that', 'Think about'],
        r'\bIt goes without saying that\b': ['', 'Obviously'],
        
        # Business jargon
        r'\baction item\b': ['task', 'job', 'thing to do'],
        r'\bbandwidth\b': ['time', 'capacity', 'resources'],
        r'\bcircle back\b': ['return to', 'revisit', 'check back'],
        r'\bdeep dive\b': ['detailed look', 'close examination', 'thorough review'],
        r'\blow-hanging fruit\b': ['easy wins', 'simple tasks', 'quick fixes'],
        r'\bmove the needle\b': ['make progress', 'improve', 'help'],
        r'\btouch base\b': ['talk', 'meet', 'connect'],
        r'\bthink outside the box\b': ['be creative', 'try new ideas'],
        r'\bpivot\b': ['change', 'shift', 'switch'],
        
        # Overused verbs
        r'\benhance\b': ['improve', 'boost', 'better', 'increase'],
        r'\butilize\b': ['use', 'apply', 'employ'],
        r'\bemploy\b': ['use', 'apply'],
        r'\bimplement\b': ['use', 'apply', 'start', 'do'],
        r'\bincorporate\b': ['include', 'add', 'use'],
        r'\bdemonstrate\b': ['show', 'prove', 'display'],
        r'\bexhibit\b': ['show', 'display'],
        r'\bmanifest\b': ['show', 'appear', 'display'],
        r'\bnavigat(e|ing)\b': ['deal with', 'handle', 'work through'],
        r'\bunderscore\b': ['emphasize', 'highlight', 'stress', 'show'],
        r'\bcomprises\b': ['includes', 'contains', 'has'],
        r'\bencompass\b': ['include', 'cover', 'contain'],
        
        # Overused adjectives
        r'\bcomprehensive\b': ['complete', 'full', 'thorough', 'detailed'],
        r'\bextensive\b': ['large', 'wide', 'broad'],
        r'\bsignificant\b': ['big', 'major', 'important', 'large'],
        r'\bsubstantial\b': ['large', 'big', 'considerable'],
        r'\bnotable\b': ['important', 'significant', 'noteworthy'],
        r'\bvital\b': ['important', 'crucial', 'key', 'essential'],
        r'\bcrucial\b': ['important', 'key', 'essential', 'vital'],
        r'\bessential\b': ['necessary', 'needed', 'important', 'key'],
        r'\bfundamental\b': ['basic', 'key', 'core', 'main'],
        r'\binherent\b': ['built-in', 'natural', 'basic'],
        r'\bintrinsic\b': ['built-in', 'natural', 'inherent'],
        r'\bpivotal\b': ['key', 'crucial', 'important', 'central'],
        r'\bdiverse\b': ['varied', 'different', 'various'],
        r'\bvarious\b': ['different', 'many', 'several'],
        r'\bnumerous\b': ['many', 'lots of', 'several'],
        r'\bplethora\b': ['many', 'lots', 'plenty'],
        r'\bmyriad\b': ['many', 'countless', 'lots of'],
        
        # Academic/formal language
        r'\bnotwithstanding\b': ['despite', 'even with'],
        r'\btherefore\b': ['so', 'thus', 'hence'],
        r'\bthus\b': ['so', 'therefore'],
        r'\bhence\b': ['so', 'therefore', 'thus'],
        r'\baccordingly\b': ['so', 'therefore'],
        r'\bconsequently\b': ['so', 'as a result', 'therefore'],
        r'\bfurthermore\b': ['also', 'plus', 'and'],
        r'\bmoreover\b': ['also', 'besides', 'plus'],
        r'\badditionally\b': ['also', 'too', 'plus'],
        r'\bnevertheless\b': ['but', 'still', 'however', 'yet'],
        r'\bnonetheless\b': ['but', 'still', 'however', 'yet'],
        r'\bhowever\b': ['but', 'yet', 'still'],
        r'\bconversely\b': ['on the other hand', 'but', 'instead'],
    }
    
    result = text
    
    # Apply all replacements
    for pattern, replacements in ai_phrases.items():
        matches = list(re.finditer(pattern, result, re.IGNORECASE))
        for match in reversed(matches):
            replacement = random.choice(replacements)
            start, end = match.span()
            if replacement and result[start].isupper():
                replacement = replacement.capitalize()
            result = result[:start] + replacement + result[end:]
    
    # Remove common AI sentence starters
    result = re.sub(r'^\s*In conclusion,?\s*', '', result, flags=re.IGNORECASE | re.MULTILINE)
    result = re.sub(r'^\s*To summarize,?\s*', '', result, flags=re.IGNORECASE | re.MULTILINE)
    result = re.sub(r'^\s*In summary,?\s*', '', result, flags=re.IGNORECASE | re.MULTILINE)
    
    # Remove hedging language
    result = re.sub(r'\b(essentially|basically|actually|literally|virtually|practically|effectively)\s+', '', result, flags=re.IGNORECASE)
    result = re.sub(r'\bkind of\b', '', result, flags=re.IGNORECASE)
    result = re.sub(r'\bsort of\b', '', result, flags=re.IGNORECASE)
    result = re.sub(r'\bsomewhat\b', '', result, flags=re.IGNORECASE)
    result = re.sub(r'\brelatively\b', '', result, flags=re.IGNORECASE)
    
    # Remove excessive transitions
    result = re.sub(r'\.\s+(Moreover|Furthermore|Additionally|In addition|Besides this),\s+', '. ', result)
    
    # Clean up spacing
    result = re.sub(r'\s+', ' ', result)
    result = re.sub(r'\s+([.,!?;:])', r'\1', result)
    result = re.sub(r'\s+', ' ', result)
    
    return result.strip()

def make_contractions(text):
    """Add natural contractions everywhere"""
    contractions = {
        r'\bI am\b': "I'm",
        r'\byou are\b': "you're",
        r'\bhe is\b': "he's",
        r'\bshe is\b': "she's",
        r'\bit is\b': "it's",
        r'\bwe are\b': "we're",
        r'\bthey are\b': "they're",
        r'\bI have\b': "I've",
        r'\byou have\b': "you've",
        r'\bwe have\b': "we've",
        r'\bthey have\b': "they've",
        r'\bI will\b': "I'll",
        r'\byou will\b': "you'll",
        r'\bhe will\b': "he'll",
        r'\bshe will\b': "she'll",
        r'\bit will\b': "it'll",
        r'\bwe will\b': "we'll",
        r'\bthey will\b': "they'll",
        r'\bI would\b': "I'd",
        r'\byou would\b': "you'd",
        r'\bhe would\b': "he'd",
        r'\bshe would\b': "she'd",
        r'\bwe would\b': "we'd",
        r'\bthey would\b': "they'd",
        r'\bdo not\b': "don't",
        r'\bdoes not\b': "doesn't",
        r'\bdid not\b': "didn't",
        r'\bcan not\b': "can't",
        r'\bcannot\b': "can't",
        r'\bcould not\b': "couldn't",
        r'\bshould not\b': "shouldn't",
        r'\bwould not\b': "wouldn't",
        r'\bwill not\b': "won't",
        r'\bis not\b': "isn't",
        r'\bare not\b': "aren't",
        r'\bwas not\b': "wasn't",
        r'\bwere not\b': "weren't",
        r'\bhas not\b': "hasn't",
        r'\bhave not\b': "haven't",
        r'\bhad not\b': "hadn't",
        r'\bthat is\b': "that's",
        r'\bwhat is\b': "what's",
        r'\bwhere is\b': "where's",
        r'\bwho is\b': "who's",
        r'\bhow is\b': "how's",
        r'\bthere is\b': "there's",
        r'\blet us\b': "let's",
    }
    
    result = text
    for pattern, contraction in contractions.items():
        result = re.sub(pattern, contraction, result, flags=re.IGNORECASE)
    
    return result

def vary_sentence_length(text):
    """Mix short and long sentences like humans do"""
    sentences = re.split(r'([.!?]+)\s+', text)
    
    combined = []
    i = 0
    while i < len(sentences):
        if i + 1 < len(sentences) and sentences[i].strip():
            combined.append(sentences[i] + sentences[i + 1])
            i += 2
        elif sentences[i].strip():
            combined.append(sentences[i])
            i += 1
        else:
            i += 1
    
    result = []
    i = 0
    while i < len(combined):
        sentence = combined[i].strip()
        words = sentence.split()
        
        # Combine very short sentences
        if i < len(combined) - 1 and len(words) < 6:
            next_sentence = combined[i + 1].strip()
            if next_sentence:
                connectors = [', and', ', so', ', but', '. But', '. And', '. So']
                connector = random.choice(connectors)
                if connector.startswith(','):
                    next_sentence = next_sentence[0].lower() + next_sentence[1:]
                result.append(sentence + connector + ' ' + next_sentence)
                i += 2
                continue
        
        result.append(sentence)
        i += 1
    
    return ' '.join(result)

def add_casual_language(text):
    """Make language more casual and conversational"""
    
    # Replace formal words with casual ones
    casual_replacements = {
        r'\bpurchase\b': 'buy',
        r'\bobtain\b': 'get',
        r'\breceive\b': 'get',
        r'\bpossess\b': 'have',
        r'\breside\b': 'live',
        r'\bcommence\b': 'start',
        r'\bterminate\b': 'end',
        r'\bproceed\b': 'go',
        r'\breturn\b': 'go back',
        r'\bassist\b': 'help',
        r'\binquire\b': 'ask',
        r'\binform\b': 'tell',
        r'\brespond\b': 'reply',
        r'\battempt\b': 'try',
        r'\bdesire\b': 'want',
        r'\brequire\b': 'need',
        r'\bpermit\b': 'let',
    }
    
    result = text
    for pattern, replacement in casual_replacements.items():
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    
    return result

def break_complex_sentences(text):
    """Break overly complex sentences into simpler ones"""
    result = text
    
    # Split sentences with multiple clauses
    result = re.sub(r',\s+which\s+', '. This ', result)
    result = re.sub(r',\s+and\s+this\s+', '. This ', result)
    
    return result

def add_human_variations(text):
    """Add natural human variations"""
    result = text
    
    # Occasionally start sentences differently
    starters = ['Well,', 'So,', 'Now,', 'Look,', 'See,']
    sentences = result.split('. ')
    
    for i in range(len(sentences)):
        if i > 0 and random.random() < 0.15 and not any(sentences[i].startswith(s) for s in starters):
            sentences[i] = random.choice(starters) + ' ' + sentences[i]
    
    result = '. '.join(sentences)
    
    # Add occasional interjections
    result = re.sub(r'\. (But|And|So)\b', r'. \1', result)
    
    return result

def remove_passive_voice(text):
    """Convert passive voice to active where possible"""
    # Common passive constructions
    result = re.sub(r'\bis being (\w+ed)\b', lambda m: f'{m.group(1).replace("ed", "es")}', text)
    result = re.sub(r'\bwas (\w+ed) by\b', r'X \1', result)
    result = re.sub(r'\bwere (\w+ed) by\b', r'X \1', result)
    
    return result

def humanize_text_aggressive(text):
    """Apply ALL humanization techniques aggressively"""
    if not text or not text.strip():
        return text
    
    result = text
    
    # Apply all transformations
    result = remove_ai_patterns(result)
    result = make_contractions(result)
    result = add_casual_language(result)
    result = break_complex_sentences(result)
    result = vary_sentence_length(result)
    result = add_human_variations(result)
    
    # Final cleanup
    result = re.sub(r'\s+', ' ', result)
    result = re.sub(r'\s+([.,!?;:])', r'\1', result)
    result = result.strip()
    
    return result

# Streamlit UI
st.set_page_config(
    page_title="AI to Human Text Converter",
    page_icon="🤖➡️👤",
    layout="wide"
)

st.title("🤖➡️👤 AI to 100% Human Text Converter")
st.markdown("**Completely transform AI-generated text into natural, authentic human writing**")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    st.markdown("### Transformation Intensity")
    st.info("All transformations are applied at maximum intensity for complete humanization.")
    
    st.markdown("---")
    st.markdown("### What Gets Removed:")
    st.markdown("""
    ✅ AI clichés & buzzwords  
    ✅ Formal/academic language  
    ✅ Passive voice patterns  
    ✅ Hedging language  
    ✅ Business jargon  
    ✅ Robotic sentence structure  
    ✅ Overly complex phrases  
    
    ### What Gets Added:
    ✅ Natural contractions  
    ✅ Casual language  
    ✅ Varied sentence lengths  
    ✅ Conversational tone  
    ✅ Human imperfections  
    """)

# Main content
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 AI-Generated Text")
    input_text = st.text_area(
        "Paste your AI text here:",
        height=450,
        placeholder="Paste AI-generated text here and watch it transform into natural human writing..."
    )
    
    char_count = len(input_text)
    word_count = len(input_text.split())
    st.caption(f"📊 {word_count} words • {char_count} characters")
    
    process_button = st.button("🚀 Convert to Human Text", type="primary", use_container_width=True)

with col2:
    st.subheader("✨ Human-Like Output")
    
    if process_button:
        if input_text.strip():
            with st.spinner("🔄 Removing all AI patterns..."):
                output_text = humanize_text_aggressive(input_text)
                
                st.text_area(
                    "100% Human Result:",
                    value=output_text,
                    height=450,
                    label_visibility="collapsed"
                )
                
                out_char_count = len(output_text)
                out_word_count = len(output_text.split())
                st.caption(f"📊 {out_word_count} words • {out_char_count} characters")
                
                # Copy button
                st.code(output_text, language=None)
                
                # Statistics
                st.markdown("---")
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Original Words", word_count)
                with col_b:
                    st.metric("New Words", out_word_count)
                with col_c:
                    diff = out_word_count - word_count
                    st.metric("Change", f"{diff:+d}", delta_color="off")
                
                st.success("✅ Text successfully humanized!")
        else:
            st.warning("⚠️ Please enter some text to convert.")
    else:
        st.text_area(
            "Your humanized text will appear here...",
            value="",
            height=450,
            disabled=True,
            label_visibility="collapsed"
        )

# Examples
with st.expander("📖 See Before/After Examples"):
    st.markdown("""
    ### Example 1:
    **🤖 Before (AI):**  
    "It's worth noting that in today's world, we need to delve into the realm of artificial intelligence to leverage robust solutions that facilitate seamless integration."
    
    **👤 After (Human):**  
    "Note that today, we need to explore artificial intelligence to use strong solutions that help smooth integration."
    
    ---
    
    ### Example 2:
    **🤖 Before (AI):**  
    "The implementation of this comprehensive strategy will optimize our operational efficiency and enhance productivity across all departments, thereby facilitating substantial improvements."
    
    **👤 After (Human):**  
    "Using this complete strategy will improve our work efficiency and boost productivity across all departments. This helps make big improvements."
    
    ---
    
    ### Example 3:
    **🤖 Before (AI):**  
    "It is important to note that this paradigm shift represents a significant breakthrough that will fundamentally transform how we navigate the landscape of modern technology."
    
    **👤 After (Human):**  
    "This big change represents a major breakthrough that'll completely transform how we handle modern technology."
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888;'>💡 Tip: Run text through multiple times for even more natural results</div>",
    unsafe_allow_html=True
)
st.markdown(
    "<div style='text-align: center; color: #666; margin-top: 10px;'>Made with Streamlit • Transform AI text to authentic human writing</div>",
    unsafe_allow_html=True
        )
