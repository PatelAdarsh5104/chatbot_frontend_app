import streamlit as st
from functions import handle_chatbot_response

# if 'system_prompt' not in st.session_state:
#     st.session_state.system_prompt = "You are a helpful assistant."


st.title("Chatbot")

# st.sidebar
question = str(st.chat_input("Ask me anything"))

# st.sidebar.text_input("System Prompt", st.session_state.system_prompt, key="system_prompt")

if question:
    # print(question)
    response = handle_chatbot_response(question, "user")
    # print(type(response))
    st.chat_message("assistant").write(response)