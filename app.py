import streamlit as st

st.title("My Calculator 🧮")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

op = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if op == "Add":
        st.success(f"Result: {num1 + num2}")
    elif op == "Subtract":
        st.success(f"Result: {num1 - num2}")
    elif op == "Multiply":
        st.success(f"Result: {num1 * num2}")
    elif op == "Divide":
        if num2 == 0:
            st.error("Cannot divide by zero!")
        else:
            st.success(f"Result: {num1 / num2}")