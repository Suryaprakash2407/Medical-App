import streamlit as st
st.title('MEDICAL DIAGNOSTIC WEB APP')
st.subheader("Is the patient Diabetic?")
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
#step 1: Load the pickled model 
model = open('rfc.pickle','rb')
clf = pickle.load(model)
model.close()

# step 2 : Get the input from the front end user 
pregs = st.number_input('Pregnancies',0,17,0)
glucose = st.slider('Glucose',40,200,40)
bp = st.slider('BloodPressure',20,140,20)
skin = st.slider('SkinThickness',7.0,99.0,7.0)
insulin = st.slider('Insulin',14,50,14)
bmi = st.slider('BMI',18,67,18)
diabetics = st.slider('DiabetesPedigreeFunction',0.05,2.50,0.05)
age = st.slider('Age',20,90,20)

## step 3 : Collect the front end user input as model input data 
data = {
    'Pregnancies':pregs,
    'Glucose':glucose,
    'BloodPressure': bp,
    'SkinThickness':skin,
    'Insulin':insulin,
    'BMI':bmi,
    'DiabetesPedigreeFunction':dpf,
    'Age':age
}
input_data = pd.DataFrame([data])

##step 4 : Get the predictions and print the results 
preds = clf.predict(input_data)[0]
if str.button('Predict'):
    if preds == 1: 
        st.error('Diabetic')
    if preds == 0:
        st.success('Non Diabetic')
