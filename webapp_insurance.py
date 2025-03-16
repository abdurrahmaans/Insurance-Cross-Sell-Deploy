import streamlit as st
import pandas as pd 
import joblib

st.title("Vehicle Insurance Response Prediction")

#Read the dataset to fill te values in the drop list

df = pd.read_csv('train.csv')

#crate a input fields
Gender = st.selectbox("Gender",pd.unique(df['Gender']))
Age = st.number_input("Age")
Driving_License = st.number_input("Driving_License")
Region_Code = st.number_input("Region_Code")
Previously_Insured = st.number_input("Previously_Insured")
Vehicle_Age = st.selectbox("Vehicle_Age",pd.unique(df['Vehicle_Age']))
Vehicle_Damage = st.selectbox("Vehicle_Damage",pd.unique(df['Vehicle_Damage']))
Annual_Premium = st.number_input("Annual_Premium")
Policy_Sales_Channel = st.number_input("Policy_Sales_Channel")
Vintage = st.number_input("Vintage")
inputs= {"Gender" : Gender,
         "Age" : Age,
         "Driving_License" : Driving_License,
         "Region_Code" : Region_Code,
         "Previously_Insured" : Previously_Insured,
         "Vehicle_Age" : Vehicle_Age,
         "Vehicle_Damage" : Vehicle_Damage,
         "Annual_Premium" : Annual_Premium,
         "Policy_Sales_Channel" : Policy_Sales_Channel,
         "Vintage" : Vintage
        }

#Click for prediction 
if st.button("Predict") :
    model = joblib.load("job_pipeline_model_voting_cross_sell.pkl")
    X_input = pd.DataFrame(inputs,index=[0])
    prediction = model.predict(X_input)
    st.write(prediction)
        

