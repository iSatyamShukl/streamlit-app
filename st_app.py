import streamlit as st

x=st.number_input("Enter first number: ")
y=st.number_input("Enter second number: ")
z=st.number_input("Enter third number: ")

st.write(f"The largest number out of {x},{y} & {z} is {max(x,y,z)}")