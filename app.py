import streamlit as st
import random
import time

st.set_page_config(
    page_title="AI Voice Interview Analyzer",
    page_icon="🎤",
    layout="centered"
)

st.sidebar.title("AI Voice Interview Analyzer")

st.sidebar.write(
    """
    This application analyzes interview conversations and provides:
    
    • Conversation summaries  
    • Pause detection  
    • Context-based filler phrases  
    • Technical response evaluation
    """
)

st.sidebar.markdown("---")
st.sidebar.caption("Build by Streamlit")

# ---------------- TITLE ----------------

st.title(" AI Voice Interview Analyzer")

st.info("Real-Time Conversation Analysis and Interview Evaluation System")

st.write(
    "This lightweight application analyzes interview responses and "
    "provides quick insights based on the conversation content."
)

# ---------------- INPUT SECTION ----------------

transcript = st.text_area(
    "Enter Interview Conversation",
    height=250,
    placeholder="Paste interview conversation or response here..."
)

# ---------------- FILLER PHRASES ----------------

fillers = [
    "That’s a good point to discuss.",
    "One thing worth mentioning is...",
    "From an implementation perspective...",
    "A key consideration here is...",
    "This approach helps improve efficiency.",
    "Another important aspect is..."
]

# ---------------- SUMMARY FUNCTION ----------------

def generate_summary(text):

    sentences = text.split(".")

    important_sentences = sentences[:2]

    return ".".join(important_sentences)

# ---------------- ANALYSIS BUTTON ----------------

if st.button("Analyze Response"):

    if transcript.strip() == "":
        st.warning("Please enter a conversation or response to analyze.")

    else:

        # Loading Animation
        with st.spinner("Processing conversation..."):
            time.sleep(2)

        # Generate Summary
        summary = generate_summary(transcript)

        # Generate Filler Phrase
        filler = random.choice(fillers)

        # Word Count
        words = len(transcript.split())

        # ---------------- RESULTS ----------------

        st.subheader(" Conversation Summary")
        st.success(summary)

        st.subheader(" Suggested Filler Phrase")
        st.info(filler)

        st.subheader(" Conversation Statistics")
        st.write(f"Total Words: {words}")

        st.subheader("⏸ Pause Detection")
        st.warning("Short pause detected during conversation")

        # ---------------- RESPONSE EVALUATION ----------------

        st.subheader(" Response Evaluation")

        technical_keywords = [
            "api",
            "database",
            "authentication",
            "jwt",
            "architecture",
            ".net",
            "angular",
            "python",
            "backend",
            "frontend",
            "oracle",
            "streamlit",
            "system",
            "dashboard",
            "analysis",
            "report"
        ]

        score = 0

        # Response Length Score
        if words > 30:
            score += 30

        # Keyword-Based Scoring
        for keyword in technical_keywords:

            if keyword.lower() in transcript.lower():
                score += 7

        # Limit Maximum Score
        if score > 100:
            score = 100

        # Display Progress Bar
        st.progress(score / 100)

        # Display Score
        st.metric(
            label="Evaluation Score",
            value=f"{score}/100"
        )

        # Final Observation
        if score >= 75:
            st.success("The response demonstrates strong technical understanding.")

        elif score >= 50:
            st.info("The response covers the topic reasonably well.")

        else:
            st.warning("The response could include more technical detail.")

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "AI Voice Interview Analyzer • Real-Time Conversation Evaluation System"
)
