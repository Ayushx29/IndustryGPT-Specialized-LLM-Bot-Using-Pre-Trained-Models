import streamlit as st
import requests
import json

# 🔧 Page setup
st.set_page_config(page_title="💬 Finance Chatbot")

# 📌 Sidebar: Info + ngrok URL
with st.sidebar:
    st.title('💬 Finance Chatbot')
    st.write('This chatbot uses a fine-tuned TinyLlama model for finance-related queries.')
    ngrok_url = st.text_input('Enter ngrok URL:', value="").strip()

if not ngrok_url:
    st.warning('Please enter the ngrok URL!', icon='⚠️')

# 🔁 Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# 📡 Function to query Flask endpoint
def generate_response(prompt_input):
    headers = {"Content-Type": "application/json"}
    payload = {"prompt": prompt_input}
    try:
        response = requests.post(f"{ngrok_url}/generate", headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json().get('generated_text', '')
    except requests.exceptions.RequestException as e:
        st.error(f"🚨 Request failed: {e}")
        return None
    except json.JSONDecodeError:
        st.error("🚨 JSON decoding failed.")
        return None

# 💬 Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 🧹 Clear chat history
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button("🗑️ Clear Chat History", on_click=clear_chat_history)

# ⌨️ Input
if prompt := st.chat_input("Enter your message:", disabled=not ngrok_url):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # 🤖 Bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt)
            if response:
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
