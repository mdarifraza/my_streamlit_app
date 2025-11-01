import streamlit as st
st.write("Login Page")
st.title("Welcome to the Login Page")

username=st.text_input("Enter your username")
password=st.text_input("enter your password",type="password")
login_button=st.button("Login") 

if login_button:
    if username=="Arif" and password=="1234":
        st.success("login successfully")
        st.write("Welcome to the application, Arif!")
    elif username!="Arif":
        st.error("invalid username but your password is correct")
    elif password!="1234":
        st.error("invalid password but your username is correct")   
    else:
        st.error("Invalid username or password. Please try again.")
        