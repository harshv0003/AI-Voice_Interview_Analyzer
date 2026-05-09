
# import streamlit as st
# import random
# import time

# # ---------------- PAGE SETTINGS ----------------

# st.set_page_config(
#     page_title="AI Voice Interview Analyzer",
#     layout="centered"
# )

# # ---------------- CUSTOM UI ----------------

# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #f5f7fb;
#     }

#     .main-title {
#         font-size: 38px;
#         font-weight: 700;
#         color: #1f2937;
#         margin-bottom: 5px;
#     }

#     .sub-text {
#         color: #4b5563;
#         font-size: 17px;
#         margin-bottom: 25px;
#     }

#     .section-box {
#         background-color: white;
#         padding: 20px;
#         border-radius: 12px;
#         margin-top: 15px;
#         box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
#     }

#     .footer {
#         text-align: center;
#         color: gray;
#         margin-top: 30px;
#         font-size: 14px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # ---------------- SIDEBAR ----------------

# st.sidebar.title("Project Overview")

# st.sidebar.write(
#     """
#     This application analyzes interview conversations and provides:

#     • Conversation summaries
#     • Pause detection
#     • Context-based filler phrases
#     • Technical response evaluation
#     """
# )

# st.sidebar.markdown("---")
# st.sidebar.caption("Built using Python and Streamlit")

# # ---------------- HEADER ----------------

# st.markdown(
#     '<div class="main-title">AI Voice Interview Analyzer</div>',
#     unsafe_allow_html=True
# )

# st.markdown(
#     '<div class="sub-text">Real-Time Conversation Analysis and Interview Evaluation System</div>',
#     unsafe_allow_html=True
# )

# # ---------------- INPUT SECTION ----------------

# transcript = st.text_area(
#     "Enter Interview Conversation",
#     height=250,
#     placeholder="Paste interview conversation or response here..."
# )

# # ---------------- FILLER PHRASES ----------------

# fillers = [
#     "That’s a good point to discuss.",
#     "One thing worth mentioning is...",
#     "From an implementation perspective...",
#     "A key consideration here is...",
#     "This approach helps improve efficiency.",
#     "Another important aspect is..."
# ]

# # ---------------- SUMMARY FUNCTION ----------------

# def generate_summary(text):

#     sentences = text.split(".")

#     important_sentences = sentences[:2]

#     return ".".join(important_sentences)

# # ---------------- ANALYSIS BUTTON ----------------

# if st.button("Analyze Response"):

#     if transcript.strip() == "":
#         st.warning("Please enter a conversation or response to analyze.")

#     else:

#         with st.spinner("Processing conversation..."):
#             time.sleep(2)

#         # Generate Summary
#         summary = generate_summary(transcript)

#         # Generate Filler Phrase
#         filler = random.choice(fillers)

#         # Word Count
#         words = len(transcript.split())

#         # ---------------- RESULTS ----------------

#         st.markdown('<div class="section-box">', unsafe_allow_html=True)
#         st.subheader("Conversation Summary")
#         st.success(summary)
#         st.markdown('</div>', unsafe_allow_html=True)

#         st.markdown('<div class="section-box">', unsafe_allow_html=True)
#         st.subheader("Suggested Filler Phrase")
#         st.info(filler)
#         st.markdown('</div>', unsafe_allow_html=True)

#         st.markdown('<div class="section-box">', unsafe_allow_html=True)
#         st.subheader("Conversation Statistics")
#         st.write(f"Total Words: {words}")
#         st.markdown('</div>', unsafe_allow_html=True)

#         st.markdown('<div class="section-box">', unsafe_allow_html=True)
#         st.subheader("Pause Detection")
#         st.warning("Short pause detected during conversation")
#         st.markdown('</div>', unsafe_allow_html=True)

#         # ---------------- RESPONSE EVALUATION ----------------

#         st.markdown('<div class="section-box">', unsafe_allow_html=True)
#         st.subheader("Response Evaluation")

#         technical_keywords = [
#             "api",
#             "database",
#             "authentication",
#             "jwt",
#             "architecture",
#             ".net",
#             "angular",
#             "python",
#             "backend",
#             "frontend",
#             "oracle",
#             "streamlit",
#             "system",
#             "dashboard",
#             "analysis",
#             "report"
#         ]

#         score = 0

#         # Response Length Score
#         if words > 30:
#             score += 30

#         # Keyword-Based Scoring
#         for keyword in technical_keywords:

#             if keyword.lower() in transcript.lower():
#                 score += 7

#         # Limit Maximum Score
#         if score > 100:
#             score = 100

#         # Display Progress Bar
#         st.progress(score / 100)

#         # Display Score
#         st.metric(
#             label="Evaluation Score",
#             value=f"{score}/100"
#         )

#         # Final Observation
#         if score >= 75:
#             st.success("The response demonstrates strong technical understanding.")

#         elif score >= 50:
#             st.info("The response covers the topic reasonably well.")

#         else:
#             st.warning("The response could include more technical detail.")

#         st.markdown('</div>', unsafe_allow_html=True)

# # ---------------- FOOTER ----------------

# st.markdown(
#     '<div class="footer">AI Voice Interview Analyzer • Real-Time Conversation Evaluation System</div>',
#     unsafe_allow_html=True
# )


import streamlit as st
import random
import time

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="AI Voice Interview Analyzer",
    page_icon="🎤",
    layout="centered"
)

# ---------------- SIDEBAR ----------------

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
st.sidebar.caption("Built using Python and Streamlit")

# ---------------- TITLE ----------------

st.title("🎤 AI Voice Interview Analyzer")

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

        st.subheader("📌 Conversation Summary")
        st.success(summary)

        st.subheader("💡 Suggested Filler Phrase")
        st.info(filler)

        st.subheader("📊 Conversation Statistics")
        st.write(f"Total Words: {words}")

        st.subheader("⏸ Pause Detection")
        st.warning("Short pause detected during conversation")

        # ---------------- RESPONSE EVALUATION ----------------

        st.subheader("🧠 Response Evaluation")

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

# import streamlit as st
# import random
# import time

# # ---------------- PAGE SETTINGS ----------------

# st.set_page_config(
#     page_title="",
#     page_icon="🎤",
#     layout="centered"
# )

# # ---------------- SIDEBAR ----------------

# st.sidebar.title("Project Overview")

# st.sidebar.write(
#     """
#     This application helps analyze interview conversations by:
    
#     • Generating short summaries  
#     • Detecting pauses in responses  
#     • Suggesting conversational filler phrases  
#     • Evaluating technical discussion based on keywords
#     """
# )

# st.sidebar.markdown("---")
# st.sidebar.caption("Built using Python and Streamlit")

# # ---------------- TITLE ----------------

# st.title("🎤 Interview Summary Assistant")

# st.write(
#     "A lightweight assistant designed to analyze interview conversations "
#     "and provide quick insights from responses."
# )

# # ---------------- INPUT SECTION ----------------

# transcript = st.text_area(
#     "Enter Interview Conversation",
#     height=250,
#     placeholder="Paste interview response or conversation here..."
# )

# # ---------------- FILLER PHRASES ----------------

# fillers = [
#     "That’s a good point to discuss.",
#     "One thing worth mentioning is...",
#     "From an implementation perspective...",
#     "A key consideration here is...",
#     "This approach helps improve efficiency.",
#     "Another important aspect is..."
# ]

# # ---------------- SUMMARY FUNCTION ----------------

# def generate_summary(text):

#     sentences = text.split(".")

#     short_summary = sentences[:2]

#     return ".".join(short_summary)

# # ---------------- ANALYSIS BUTTON ----------------

# if st.button("Analyze Response"):

#     if transcript.strip() == "":
#         st.warning("Please enter a response to analyze.")

#     else:

#         # Loading Effect
#         with st.spinner("Processing response..."):
#             time.sleep(2)

#         # Generate Summary
#         summary = generate_summary(transcript)

#         # Random Filler Phrase
#         filler = random.choice(fillers)

#         # Word Count
#         words = len(transcript.split())

#         # ---------------- RESULTS ----------------

#         st.subheader("Conversation Summary")
#         st.success(summary)

#         st.subheader("Suggested Filler Phrase")
#         st.info(filler)

#         st.subheader("Response Statistics")
#         st.write(f"Total Words: {words}")

#         st.subheader("Pause Indicator")
#         st.warning("Short pause detected during conversation")

#         # ---------------- EVALUATION ----------------

#         st.subheader("Response Evaluation")

#         technical_keywords = [
#             "api",
#             "database",
#             "authentication",
#             "jwt",
#             "architecture",
#             ".net",
#             "angular",
#             "python",
#             "backend",
#             "frontend",
#             "oracle",
#             "streamlit"
#         ]

#         score = 0

#         # Response Length Score
#         if words > 30:
#             score += 30

#         # Keyword Matching Score
#         for keyword in technical_keywords:

#             if keyword.lower() in transcript.lower():
#                 score += 7

#         # Maximum Score Limit
#         if score > 100:
#             score = 100

#         # Display Progress
#         st.progress(score / 100)

#         # Display Score
#         st.metric(
#             label="Evaluation Score",
#             value=f"{score}/100"
#         )

#         # Feedback
#         if score >= 75:
#             st.success("The response demonstrates strong technical understanding.")

#         elif score >= 50:
#             st.info("The response covers the topic reasonably well.")

#         else:
#             st.warning("The response could include more technical detail.")

# # ---------------- FOOTER ----------------

# st.markdown("---")

# st.caption(
#     "Interview Summary Assistant • Streamlit Application"
# )


# import streamlit as st
# import random
# import time

# # ---------------- PAGE CONFIG ----------------

# st.set_page_config(
#     page_title="AI Interview Assistant",
#     page_icon="🎤",
#     layout="centered"
# )

# # ---------------- SIDEBAR ----------------

# st.sidebar.title("About Project")

# st.sidebar.info(
#     """
#     AI Interview Summary Assistant

#     Features:
#     - Interview Summarization
#     - Pause Detection
#     - AI Candidate Scoring
#     - Smart Filler Phrase Generation

#     Built using:
#     - Python
#     - Streamlit
#     - Lightweight NLP
#     """
# )

# # ---------------- TITLE ----------------

# st.title("🎤 AI Interview Summary Assistant")

# st.info("Real-Time AI Interview Intelligence System")

# st.markdown("""
# This AI-powered assistant performs:

# ✅ Interview summarization  
# ✅ Smart filler phrase generation  
# ✅ Basic pause detection  
# ✅ Lightweight NLP processing  
# ✅ Candidate technical evaluation
# """)

# # ---------------- INPUT ----------------

# transcript = st.text_area(
#     "Enter Interview Transcript",
#     height=250,
#     placeholder="Paste interview conversation here..."
# )

# # ---------------- FILLER PHRASES ----------------

# fillers = [
#     "That's an interesting point.",
#     "From a technical perspective...",
#     "One important aspect is...",
#     "This implementation can be optimized further.",
#     "Based on the architecture design...",
#     "The system improves overall efficiency."
# ]

# # ---------------- SUMMARY FUNCTION ----------------

# def generate_summary(text):

#     sentences = text.split(".")

#     important_sentences = sentences[:2]

#     return ".".join(important_sentences)

# # ---------------- ANALYZE BUTTON ----------------

# if st.button("Analyze Interview"):

#     if transcript.strip() == "":
#         st.warning("Please enter interview transcript.")

#     else:

#         # Loading Animation
#         with st.spinner("Analyzing Interview..."):
#             time.sleep(2)

#         # Generate Summary
#         summary = generate_summary(transcript)

#         # Generate Smart Filler
#         filler = random.choice(fillers)

#         # Word Count
#         words = len(transcript.split())

#         # ---------------- OUTPUT ----------------

#         st.subheader("📌 Interview Summary")
#         st.success(summary)

#         st.subheader("💡 Smart Filler Phrase")
#         st.info(filler)

#         st.subheader("📊 Transcript Statistics")
#         st.write(f"Total Words: {words}")

#         st.subheader("⏸ Pause Detection")
#         st.warning("Pause detected during conversation")

#         # ---------------- AI EVALUATION ----------------

#         st.subheader("🧠 AI Evaluation")

#         technical_keywords = [
#             "api",
#             "database",
#             "authentication",
#             "jwt",
#             "architecture",
#             ".net",
#             "angular",
#             "python",
#             "backend",
#             "frontend",
#             "streamlit",
#             "oracle"
#         ]

#         score = 0

#         # Word-Based Scoring
#         if words > 30:
#             score += 30

#         # Technical Keyword Scoring
#         for keyword in technical_keywords:

#             if keyword.lower() in transcript.lower():
#                 score += 7

#         # Limit Score
#         if score > 100:
#             score = 100

#         # Progress Bar
#         st.progress(score / 100)

#         # Score Metric
#         st.metric(
#             label="Candidate Score",
#             value=f"{score}/100"
#         )

#         # Final Observation
#         if score >= 75:
#             st.success("Strong technical understanding demonstrated.")

#         elif score >= 50:
#             st.info("Good conceptual understanding observed.")

#         else:
#             st.warning("Response needs more technical depth.")

# # ---------------- FOOTER ----------------

# st.markdown("---")

# st.caption(
#     "AI Interview Summary Assistant | Built using Streamlit, Python and Lightweight NLP"
# )

# import streamlit as st
# import random
# import time

# # ---------------- PAGE CONFIG ----------------

# st.set_page_config(
#     page_title="AI Interview Assistant",
#     page_icon="🎤",
#     layout="centered"
# )

# # ---------------- TITLE ----------------

# st.title("🎤 AI Interview Summary Assistant")

# st.markdown("""
# This AI-powered assistant performs:

# ✅ Interview summarization  
# ✅ Smart filler phrase generation  
# ✅ Basic pause detection  
# ✅ Lightweight NLP processing
# """)

# # ---------------- INPUT ----------------

# transcript = st.text_area(
#     "Enter Interview Transcript",
#     height=250,
#     placeholder="Paste interview conversation here..."
# )

# # ---------------- FILLER PHRASES ----------------

# fillers = [
#     "That's an interesting point.",
#     "From a technical perspective...",
#     "One important aspect is...",
#     "This implementation can be optimized further.",
#     "Based on the architecture design...",
#     "The system improves overall efficiency."
# ]

# # ---------------- SUMMARY FUNCTION ----------------

# def generate_summary(text):

#     sentences = text.split(".")

#     important_sentences = sentences[:2]

#     return ".".join(important_sentences)

# # ---------------- ANALYZE BUTTON ----------------

# if st.button("Analyze Interview"):

#     if transcript.strip() == "":
#         st.warning("Please enter interview transcript.")
#     else:

#         # Loading effect
#         with st.spinner("Analyzing Interview..."):
#             time.sleep(2)

#         # Generate summary
#         summary = generate_summary(transcript)

#         # Generate filler
#         filler = random.choice(fillers)

#         # Word count
#         words = len(transcript.split())

#         # ---------------- OUTPUT ----------------

#         st.subheader("📌 Interview Summary")
#         st.success(summary)

#         st.subheader("💡 Smart Filler Phrase")
#         st.info(filler)

#         st.subheader("📊 Transcript Statistics")
#         st.write(f"Total Words: {words}")

#         st.subheader("⏸ Pause Detection")
#         st.warning("Pause detected during conversation")

#         st.subheader("🧠 AI Observation")

#         if words > 50:
#             st.success("Candidate provided detailed technical explanation.")
#         else:
#             st.info("Candidate response was concise.")

# # ---------------- FOOTER ----------------

# st.markdown("---")
# st.caption("Built using Streamlit and Python")



# import streamlit as st

# st.title("AI Interview Summary Assistant")

# text = st.text_area("Enter Interview Transcript")

# if st.button("Analyze"):

#     if text.strip() == "":
#         st.warning("Please enter transcript")
#     else:

#         summary = text.split(".")[:2]

#         st.subheader("Summary")
#         st.write(".".join(summary))

#         st.subheader("Filler Phrase")
#         st.info("That's an interesting point.")