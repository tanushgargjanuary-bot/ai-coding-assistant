import streamlit as st

st.set_page_config(page_title="AI Coding Assistant", page_icon="🛠️")
st.title("🛠️ AI Coding Assistant")
st.write("Your AI partner for code explanation, debugging, and generation")

# Tabs for different features
tab1, tab2, tab3 = st.tabs(["🧠 Code Explainer", "🐛 Debug Assistant", "⚡ Code Generator"])

with tab1:
    st.header("Understand Any Code")
    code_input = st.text_area("Paste your code here:", height=150, placeholder="def example():\n    print('Hello World')")
    if st.button("Explain This Code"):
        st.info("Code explanation feature coming soon!")
        
with tab2:
    st.header("Find and Fix Bugs")
    buggy_code = st.text_area("Paste buggy code:", height=150, placeholder="def calculate_sum(a, b):\n    return a - b  # Intentional bug")
    if st.button("Analyze for Bugs"):
        st.info("Bug detection feature coming soon!")

with tab3:
    st.header("Generate Code from Description")
    description = st.text_area("Describe what you want to code:", placeholder="A function that reverses a string")
    if st.button("Generate Code"):
        st.info("Code generation feature coming soon!")
