from llm import call_llm_groq, call_llm_pai
from constants import LLM_SERVICE

def call_llm():
    if LLM_SERVICE == 'GROQ':
        return call_llm_groq
    else:
        return call_llm_pai