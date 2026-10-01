import warnings
import logging

warnings.filterwarnings("ignore")
logging.getLogger("google_genai").setLevel(logging.ERROR)

from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()

# ---------------- Page Config ----------------
st.set_page_config(page_title="URL Q&A Bot", page_icon="🤖", layout="centered")

# ---------------- Robotic Dark Theme CSS ----------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700;900&display=swap');

    .stApp {
        background-color: #05070a;
        background-image:
            linear-gradient(rgba(0,255,170,0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,255,170,0.04) 1px, transparent 1px);
        background-size: 28px 28px;
        color: #d6ffe9;
        font-family: 'Share Tech Mono', monospace;
    }

    h1 {
        font-family: 'Orbitron', sans-serif;
        text-align: center;
        color: #00ffb3;
        text-shadow: 0 0 12px rgba(0,255,179,0.6);
        letter-spacing: 2px;
    }

    .subtitle {
        text-align: center;
        color: #5fd9b4;
        font-family: 'Share Tech Mono', monospace;
        margin-bottom: 25px;
    }

    .stTextInput input, .stTextArea textarea {
        background-color: #0b0f14 !important;
        color: #00ffb3 !important;
        border: 1px solid #00ffb3 !important;
        border-radius: 6px !important;
        font-family: 'Share Tech Mono', monospace !important;
    }

    .stButton button {
        background-color: #001f16;
        color: #00ffb3;
        border: 1px solid #00ffb3;
        border-radius: 6px;
        font-weight: 700;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 1px;
        padding: 10px 0;
        box-shadow: 0 0 10px rgba(0,255,179,0.25);
    }
    .stButton button:hover {
        background-color: #00ffb3;
        color: #05070a;
        box-shadow: 0 0 20px rgba(0,255,179,0.7);
    }

    .result-card {
        background-color: #0b0f14;
        border: 1px solid #00ffb3;
        border-radius: 10px;
        padding: 20px;
        margin-top: 15px;
        line-height: 1.7;
        box-shadow: 0 0 15px rgba(0,255,179,0.15);
    }

    .status-line {
        font-family: 'Share Tech Mono', monospace;
        color: #5fd9b4;
        font-size: 13px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🤖 URL Q&A BOT</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>&gt; TARGET URL SCAN + QUERY MODULE ONLINE_</p>", unsafe_allow_html=True)

# ---------------- Model ----------------
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0.7
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question', 'text']
)

chain = prompt | model | parser

# ---------------- Session State ----------------
if "page_content" not in st.session_state:
    st.session_state.page_content = None
if "loaded_url" not in st.session_state:
    st.session_state.loaded_url = None

# ---------------- URL Input ----------------
url = st.text_input("TARGET URL >", placeholder="https://example.com/page")

if st.button("LOAD PAGE", use_container_width=True):
    if url.strip() == "":
        st.warning("> ERROR: URL FIELD EMPTY")
    else:
        with st.spinner("SCANNING PAGE..."):
            try:
                loader = WebBaseLoader(url)
                docs = loader.load()
                st.session_state.page_content = docs[0].page_content
                st.session_state.loaded_url = url
                st.success("> PAGE LOADED SUCCESSFULLY. READY FOR QUERIES.")
            except Exception as e:
                st.error(f"> SCAN FAILED: {e}")

# ---------------- Show loaded status ----------------
if st.session_state.page_content:
    st.markdown(f"<p class='status-line'>&gt; ACTIVE TARGET: {st.session_state.loaded_url}</p>", unsafe_allow_html=True)

    st.markdown("---")

    question = st.text_input("YOUR QUERY >", placeholder="What is this page about?")

    if st.button("ASK", use_container_width=True):
        if question.strip() == "":
            st.warning("> ERROR: QUERY FIELD EMPTY")
        else:
            with st.spinner("PROCESSING QUERY..."):
                answer = chain.invoke({
                    'question': question,
                    'text': st.session_state.page_content
                })
            st.markdown(f"<div class='result-card'>{answer}</div>", unsafe_allow_html=True)