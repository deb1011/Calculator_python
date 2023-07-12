import streamlit as st;
import math

def sin(x):
  return math.sin(x)

def cos(x):
  return math.cos(x)

def tan(x):
  return math.tan(x)

def log(x):
  return math.log(x)

def main():
    st.write("Enter your Data")
    x=st.number_input("Enter the value")
    operation=st.selectbox("Select Operation",['Sin','Cos','Tan','Log'])
    if operation=='Sin':
        st.write(sin(x))
    elif operation=='Cos':
        st.write(cos(x))
    elif operation=='Tan':
        st.write(tan(x))
    elif operation=='Log':
        st.write(log(x))
if __name__=='__main__':
    main()