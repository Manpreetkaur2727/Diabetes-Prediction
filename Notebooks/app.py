import streamlit as st
import pandas as pd
import pickle
from sklearn.datasets import load_diabetes

st.title("This app is to predict the glucose level in the blood of a diabetic patient")


model_ridge=pickle.load(open('/Users/manpreetkaur/Documents/Diabetes_Prediction/Models/model_ridge.pkl','rb'))


#load the dataset
diab=load_diabetes()
X=pd.DataFrame(diab.data,columns=diab.feature_names)

# user dat
user_input={}

for col in X.columns:
    user_input[col]=st.slider(col,X[col].min(),X[col].max())

df=pd.DataFrame(user_input,index=[0])

st.write(df)

models={"Ridge":model_ridge}

selected_model=st.selectbox("Select a model",("Linear Regression","Elastic Net","Ridge"))

if st.button("Predict"):
    prediction=models[selected_model].predict(df)[0]
    st.write(f'The predicted glucose level is {prediction}')
