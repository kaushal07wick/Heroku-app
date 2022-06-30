import streamlit as st
import pandas as pd
import numpy as np
import pickle
import datetime as dt
from sklearn.preprocessing import LabelEncoder
from lightgbm import LGBMRegressor
import gzip, pickle, pickletools

st.header("Cheapest flight price prediction")
st.write("""
This is a Flight price prediction web-app, developed by Kaushal Choudhary.
It predicts the prices of flight, based on the five inputs provided by you. It's prediction model is based on 
lightGBM machine learning model, which has been trained on 3 million+ historic flight prices data.
""")
dict1 = {'B': 0, 'E': 1 ,'PE': 2}
dict2 = {'Amritsar' : 0, 'Bagdogra' : 1, 'Bengaluru' : 2, 'Bhubaneswar' : 3 , 'Chandigarh':4 , 'Chennai' :5 , 'Coimbatore':6 , 'Goa' : 7 , 'Guwahati' : 8, 'Hyderabad' : 9, 'Indore' : 10 , 'Jaipur' : 11 , 'Kochi' : 12  , 'Kolkata' : 13 , 'Kozhikode' :14 , 'Lucknow':15 , 'Mangalore':16 , 'Mumbai':17 , 'Nagpur' :18 , 'New Delhi':19 , 'Patna':20 , 'Port Blair' :21 , 'Pune': 22 , 'Raipur': 23 , 'Ranchi':24 , 'Srinagar': 25 , 'Thiruvananthapuram' : 26 ,'Tiruchirappalli' :27 ,'Varanasi' : 28 , 'Visakhapatnam': 29 }

Cabin = st.sidebar.radio('Class', ({'B': 0, 'E': 1 ,'PE': 2}))
Dept_city = st.sidebar.selectbox('From',({'Amritsar' : 0, 'Bagdogra' : 1, 'Bengaluru' : 2, 'Bhubaneswar' : 3 , 'Chandigarh':4 , 'Chennai' :5 , 'Coimbatore':6 , 'Goa' : 7 , 'Guwahati' : 8, 'Hyderabad' : 9, 'Indore' : 10 , 'Jaipur' : 11 , 'Kochi' : 12  , 'Kolkata' : 13 , 'Kozhikode' :14 , 'Lucknow':15 , 'Mangalore':16 , 'Mumbai':17 , 'Nagpur' :18 , 'New Delhi':19 , 'Patna':20 , 'Port Blair' :21 , 'Pune': 22 , 'Raipur': 23 , 'Ranchi':24 , 'Srinagar': 25 , 'Thiruvananthapuram' : 26 ,'Tiruchirappalli' :27 ,'Varanasi' : 28 , 'Visakhapatnam': 29 }))
arrival_city = st.sidebar.selectbox('To',({'Amritsar' : 0, 'Bagdogra' : 1, 'Bengaluru' : 2, 'Bhubaneswar' : 3 , 'Chandigarh':4 , 'Chennai' :5 , 'Coimbatore':6 , 'Goa' : 7 , 'Guwahati' : 8, 'Hyderabad' : 9, 'Indore' : 10 , 'Jaipur' : 11 , 'Kochi' : 12  , 'Kolkata' : 13 , 'Kozhikode' :14 , 'Lucknow':15 , 'Mangalore':16 , 'Mumbai':17 , 'Nagpur' :18 , 'New Delhi':19 , 'Patna':20 , 'Port Blair' :21 , 'Pune': 22 , 'Raipur': 23 , 'Ranchi':24 , 'Srinagar': 25 , 'Thiruvananthapuram' : 26 ,'Tiruchirappalli' :27 ,'Varanasi' : 28 , 'Visakhapatnam': 29 }))   
Dept_date = st.sidebar.date_input("Date of Journey", dt.date(2022, 6, 24))
dept_hours = st.sidebar.selectbox('Time (in Hours)',(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)) 
traveller = st.sidebar.selectbox('Number of Passengers',(1, 2 ,3 ,4, 5, 6, 7, 8, 9, 10))  

#displaying the essentials
if st.sidebar.button('Submit'):
    pass
else:
    pass

cabin = dict1[Cabin]
dept_city = dict2[Dept_city]
arr_city = dict2[arrival_city]
optimal_time = abs(dept_hours - 4)
weekday = Dept_date.weekday()

#make the final input array for model
format_input_list = [cabin, dept_city, arr_city, optimal_time, weekday]
data = np.asarray(format_input_list)


#Load in model
with gzip.open('lgbm.pickle', 'rb') as f:
    p = pickle.Unpickler(f)
    load_clf = p.load()

if st.button('Predict'):
     st.write('Predicting')
     # Apply model to make predictions
     prediction = load_clf.predict(data.reshape(1,-1).astype(float))
     st.write('Price', (traveller*prediction))
else:
    st.write('Please click on this button to predict')


st.write("The price predicted is calculated on internal parameter named as optimal time, which assumes that the time of flight booking is 4 hours before flight departure!")
st.write("So, please book your flight 4 hours before takeoff.")












