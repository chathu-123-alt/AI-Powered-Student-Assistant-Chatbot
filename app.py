import streamlit as st
from utils.rag_utils import search_knowledge
from utils.web_utils import open_google
from utils.ml_utils import predict_score

st.set_page_config(page_title="AI Teacher Assistant", layout="wide")

st.title("🎓 AI Teacher Assistant Chatbot")

st.markdown("### 📊 Enter Details for Prediction")
class_size = st.slider("Class Size", 10, 100, 30)
student_score = st.slider("Student Score", 0, 100, 75)

if "messages" not in st.session_state:
    st.session_state.messages = []

mode = st.radio("Response Mode", ["Concise", "Detailed"], horizontal=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask your question...")

def get_rule_based_response(question, mode):
    question = question.lower()

    if "teacher effectiveness" in question:
        return "Teacher effectiveness improves student outcomes." if mode == "Concise" else \
               """Teacher effectiveness refers to how well a teacher enhances student learning and performance.

🔍 Key Points:
• Teaching quality  
• Student engagement  
• Performance measurement"""

    if "class size" in question:
        return "Class size affects attention." if mode == "Concise" else \
               """Class size plays a crucial role in learning.

🔍 Key Points:
• Smaller classes improve interaction  
• More individual attention  
• Better student engagement"""

    return None

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    if "predict" in user_input.lower():
        try:
            features = [class_size, student_score]
            result = predict_score(features)
            response = f"📊 Predicted Teacher Effectiveness Score: {result}"
        except:
            response = "⚠️ Error in prediction model."

    else:
        rag_response = search_knowledge(user_input)

        if rag_response:
            if mode == "Concise":
                response = rag_response
            else:
                response = f"""
📘 Detailed Explanation:

{rag_response}

🔍 Key Points:
• It focuses on improving student outcomes  
• Includes teaching methods and communication  
• Helps evaluate classroom performance  

📊 Why It Matters:
Effective teaching directly impacts student success and learning quality.
"""
        else:
            rule_response = get_rule_based_response(user_input, mode)

            if rule_response:
                response = rule_response
            else:
                response = "🌐 Searching on Google..."
                open_google(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.write(response)
