import streamlit as st 
st.write("This is my addition app")
st.title("Addition App")
st.header("Add two numbers")
n1=st.number_input("enter the number n1")
n2=st.number_input(" enter the number n2")
if st.button("Add"):
    c=n1+n2
    st.success(f"the addition of n1 {n1} and  {n2} is :{c}")

