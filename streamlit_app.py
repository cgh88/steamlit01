import streamlit as st

st.title("Streamlit Test")
st.write("hello world")
st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')
st.write("""
# MarkDown
> comment
- one
- two
- three
- four
- five
""")
st.divider()
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')