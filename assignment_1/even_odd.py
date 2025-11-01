#UI app User will enter the numbershould display it is even or odd number
import streamlit as st 
st.write("Welcome to the Even–Odd  App! Enter a number below to see whether its even or odd.")
st.title("Even or Odd App")
user=st.number_input("Enter the number to check even or odd")
if st.button("check"):
    if user%2==0:
        st.success(f"The number {user} is Even")
    else:
        st.success(f"The number {user} id Odd")
