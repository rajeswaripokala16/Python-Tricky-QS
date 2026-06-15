import streamlit as st
# adjust the import to your function name
try:
    from Magiccode6 import process
except Exception:
    def process(text):
        return "Replace with Magiccode6 processing: " + text

st.title("Magic Code Web UI")
user_input = st.text_area("Enter input", height=200)
if st.button("Run"):
    with st.spinner("Running..."):
        try:
            out = process(user_input)
            st.success("Done")
            st.code(out)
        except Exception as e:
            st.error(f"Error: {e}")
