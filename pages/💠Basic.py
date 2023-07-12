import streamlit as st;
st.title("Basic Calculator")
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def main():
    num1=st.number_input("Enter 1st Data")
    num2=st.number_input("Enter 2nd Data")
    operation=st.selectbox("Select Operation",['Add','Subtract','Multiply','Divide'])
    if operation=='Add':
        st.write(add(num1,num2))
    elif operation == "Subtract":
        st.write(sub(num1, num2))
    elif operation == "Multiply":
        st.write(mul(num1, num2))
    elif operation == "Divide":
        st.write(div(num1, num2))
if __name__== '__main__':
    main()