import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=450)

with col2:
    st.title("Dzmitryi Lazarchyk")
    content = """
    Hello! I am Dzmitryi! I am Phython developer. Check out my study projects,
    that I provided below."""
    st.info(content)

st.write("""Please, don't hesitate to contact me if you have any qestions for me.
Or if you simply want to chat about Phython.""")