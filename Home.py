import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("image.png")

with col2:
    st.title("Manisha Kaur")
    content = """
    Hello, I'm Manisha! I am a mathematics student learning Python.
    Listed here are some of the projects I've finished or intend to finish.
    Some may include default links if the project has not been completed
    """
    st.info(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        st.write(f"[Link to application]({row['link']}")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        st.write(f"[Link to application]({row['link']}")
