import streamlit as st
from models.llm import get_response

st.title("AI Teacher Effectiveness Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask something:")

if user_input:
    st.session_state.messages.append(("user", user_input))
    
    response = get_response(user_input)
    
    st.session_state.messages.append(("bot", response))

for role, msg in st.session_state.messages:
    if role == "user":
        st.write(f"🧑 {msg}")
    else:
        st.write(f"🤖 {msg}")