import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Obesity & Weight Loss Program",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default elements
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Load and display the HTML application
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

components.html(html_content, height=3000, scrolling=True)
