import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open("linreg.pkl", "rb"))

gender = ['F', 'M']
ssc_b = ['Central', 'Others']
hsc_b = ['Central', 'Others']
hsc_s = ['Arts', 'Commerce', 'Science']
degree_t = ['Comm&Mgmt', 'Others', 'Sci&Tech']
workex = ['No', 'Yes']
specialisation = ['Mkt&Fin', 'Mkt&HR']
status = ['Not Placed', 'Placed']

st.title("Fresher Salary Prediction")
a1 = st.number_input("SL_NO")
a2 = st.selectbox("Gender", gender)
a3 = st.number_input("SSC_P")
a4 = st.selectbox("SSC_B", ssc_b)
a5 = st.number_input("HSC_P")
a6 = st.selectbox("HSC_B", hsc_b)
a7 = st.selectbox("HSC_S", hsc_s)
a8 = st.number_input("Degree P")
a9 = st.selectbox("Degree T", degree_t)
a10 = st.selectbox("Workex", workex)
a11 = st.number_input("Etest P")
a12 = st.selectbox("Specialisation", specialisation)
a13 = st.number_input("MBA P")
a14 = st.selectbox("Status", status)

if st.button("Predict"):
    a2 = gender.index(a2)
    a4 = ssc_b.index(a4)
    a6 = hsc_b.index(a6)
    a7 = hsc_s.index(a7)
    a9 = degree_t.index(a9)
    a10 = workex.index(a10)
    a12 = specialisation.index(a12)
    a14 = status.index(a14)

    test = np.array([[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14]])
    res = model.predict(test)
    print(res)
    st.success("Salary: " + str(res[0]))
