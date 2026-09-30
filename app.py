import streamlit as st
st.title(" Student Grade Calculatot .")
st.write ("Enter your marks below: ")
math = st.number_input("Math" , min_value= 0.0, max_value= 100.0)
physics = st.number_input("Physics ", min_value=0.0 , max_value= 100.0)
chemistry = st.number_input ("Chemistry ", min_value=0.0, max_value= 100.0)
if st.button("Calculate Result"):
    average = (math + physics + chemistry)/3 
    if average >= 80:
       grade = "A"
    elif average >= 70:
       grade = "B"
    elif average >= 60:
       grade = "C"
    else: 
       grade = "F"
    if average >= 40:
       result= "Pass"
    else:
       result = "Fail"
    st.subheader("Result")
    st.write("Average: ", round(average, 2))
    st.write("Grade: ", grade)
    st.write("Result: ", result)