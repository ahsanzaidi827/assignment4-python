# STREAMLIT WEBSITE

import streamlit as st

st.set_page_config(page_title="My fisrt website" , layout="centered")

st.title("Welcome to my first Python Website")  #title

st.sidebar.title("Navigation") # navigate
page= st.sidebar.radio("Go to", ["Home" , "About" , "Contact"])

if page =="Home":
    st.header("Homepage")
    st.write("This is a homepage build with Python and Streamlit")
    name = st.text_input("Tell me your name")

    if name:
        st.success(f"Hello {name}! Thanks for visiting my website")

#About
elif page =="About":
    st.header("About")
    st.write("This is an About page to enquire about us")
    

elif page =="Contact":
    st.header("Contact")
    st.write("This is a Contact page for any query you can connect with us")
    email_for_query = st.text_input("Your gmail")

    if st.button("Submit"):
        st.success(f"Email Received: We will contact you soon on {email_for_query}")









