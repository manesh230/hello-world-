import streamlit as st

# Set page config
st.set_page_config(
    page_title="Hello World App",
    page_icon="👋",
    layout="centered"
)

# Main content
st.markdown("# Hello World! 👋")
st.write("Welcome to my Streamlit app.")
st.success("This app is running successfully!")

# Add a button
if st.button("Click me!"):
    st.balloons()
    st.write("🎉 You clicked the button!")
