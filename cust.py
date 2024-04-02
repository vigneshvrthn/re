import streamlit as st
st.title("Loan")
a=st.text_input("enter your name")
c=st.number_input("enter your age")
b=st.number_input("enter the amt you required")
d=st.number_input("enter your salary")


if st.button("click the button to claculate"):
    if b/10<=d:
        st.write("you are eligibe")
    else:
        st.write("you are not eligible")
