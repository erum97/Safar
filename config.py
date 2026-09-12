# config.py
import os

import streamlit as st
from dotenv import load_dotenv


load_dotenv()


def get_secret(name: str):
    """
    First checks Streamlit Cloud Secrets.
    If unavailable, checks the local .env file.
    """

    try:
        value = st.secrets.get(name)

        if value:
            return value

    except Exception:
        pass

    return os.getenv(name)


GROQ_API_KEY = get_secret("GROQ_API_KEY")

# Model available in your Groq dashboard
GROQ_MODEL = "openai/gpt-oss-20b"

# Free-tier usage controls
MAX_HISTORY_MESSAGES = 8
MAX_TOKENS = 700
TEMPERATURE = 0.4
