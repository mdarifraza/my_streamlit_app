import streamlit as st 
st.write("This is my Calculator App")
st.title("calculator app")
st.header("perform basic arithmetic operations")

num1=st.number_input("Enter the first number (num1)")
num2=st.number_input("Enter the second number (num2)")
operation=st.selectbox("Select an operation",["Addition","Subtraction","Multiplication","Division"])

if st.button("Calculate"):
    if operation=="Addition":
        result=num1+ num2
        st.success(f"The result of adding {num1} and {num2} is:{result}")
    elif operation=="Subtraction":
        result=num1 - num2
        st.success(f"The result of subtracting {num2} from {num1} is:{result}")
    elif operation=="Multiplication":
        result=num1 * num2
        st.success(f"The result of multiplying {num1} and {num2} is:{result}")
    elif operation=="Division":
        if num2!=0:
            result=num1 / num2
            st.success(f"The result of dividing {num1} by {num2} is:{result}")
        else:
            st.error("Error: Division by zero is not allowed.")