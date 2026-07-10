import streamlit as st

st.title("Meli's Mathelogik")

first_digit = st.number_input("Erste Zahl")
operator = st.selectbox("Operator", ["+", "-", "*", "/"])
second_digit = st.number_input("Zweite Zahl")

if st.button("Berechnen"):

    if operator == "+":
        result = first_digit + second_digit

    elif operator == "-":
        result = first_digit - second_digit

    elif operator == "*":
        result = first_digit * second_digit

    elif operator == "/":
        if second_digit == 0:
            st.error("Division durch 0 geht nicht")
            st.stop()
        result = first_digit / second_digit

    st.write(f"{first_digit:g} {operator} {second_digit:g} = {result:g}")
