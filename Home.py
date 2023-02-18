import streamlit as st
import pandas

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

df = pandas.read_csv("data.csv", sep=";")
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:len(df)//2].iterrows():
        st.header(row['title'])
        st.image(f"images/{row['image']}", width=300)
        st.write(row['description'])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[len(df)//2:].iterrows():
        st.header(row['title'])
        st.image(f"images/{row['image']}", width=300)
        st.write(row['description'])
        st.write(f"[Source code]({row['url']})")


st.write('##')
st.write('##')
st.write('##')
st.write("""Please, don't hesitate to contact me if you have any questions for me.
Or if you simply want to chat about Phython.""")