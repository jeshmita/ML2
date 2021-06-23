# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:17:02 2021

@author: jeshm
"""

import numpy as np
# 1. Library imports
import uvicorn
import pandas as pd
from fastapi import FastAPI
from Airline_Satisfaction import AirlineSatisfaction
import pickle


tt = pd.read_csv("airline_means.csv", index_col=False)
tt.head(2)



# load pca fit

# Create the app object
app = FastAPI()
pickle_in = open('XGB2.pkl',"rb")
xGB=pickle.load(pickle_in)
variety_mappings = {0: 'Not Satisfied or Neutral', 1: 'Satisfied'}


# Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Welcome to Passenger Satisfaction Assessment Application'}

# Route with a single parameter, returns the parameter within a message
# Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome ': f'{name}'}

# Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_satisfaction(data:AirlineSatisfaction):
    data = data.dict()
    age = (data['age']-tt.iloc[0,0])/tt.iloc[0,1]
    inflight_wifi_service = (data['inflight_wifi_service']-tt.iloc[1,0])/tt.iloc[1,1]
    departure_arrival_time_convenient = (data['departure_arrival_time_convenient']-tt.iloc[2,0])/tt.iloc[2,1]
    ease_of_online_booking = (data['ease_of_online_booking']-tt.iloc[3,0])/tt.iloc[3,1]
    gate_location = (data['gate_location']-tt.iloc[4,0])/tt.iloc[4,1]
    food_and_drink = (data['food_and_drink']-tt.iloc[5,0])/tt.iloc[5,1]
    online_boarding = (data['online_boarding']-tt.iloc[6,0])/tt.iloc[6,1]
    seat_comfort = (data['seat_comfort']-tt.iloc[7,0])/tt.iloc[7,1]
    onboard_service = (data['onboard_service']-tt.iloc[8,0])/tt.iloc[8,1]
    leg_room_service = (data['leg_room_service']-tt.iloc[9,0])/tt.iloc[9,1]
    baggage_handling = (data['baggage_handling']-tt.iloc[10,0])/tt.iloc[10,1]
    checkin_service = (data['checkin_service']-tt.iloc[11,0])/tt.iloc[11,1]
    inflight_service = (data['inflight_service']-tt.iloc[12,0])/tt.iloc[12,1]
    cleanliness = (data['cleanliness']-tt.iloc[13,0])/tt.iloc[13,1]
    arrival_delay_in_minutes=(data['arrival_delay_in_minutes']-tt.iloc[14,0])/tt.iloc[14,1]
    gender_Male = data['gender_Male']
    customer_type_disloyalCustomer = data['customer_type_disloyalCustomer']
    type_of_travel_PersonalTravel  = data['type_of_travel_PersonalTravel']	
    customer_class_Eco  =data['customer_class_Eco']	
    customer_class_EcoPlus =data['customer_class_EcoPlus']
    features = np.array([age, inflight_wifi_service, departure_arrival_time_convenient, ease_of_online_booking, gate_location, food_and_drink, online_boarding, seat_comfort, onboard_service, leg_room_service, baggage_handling, checkin_service, inflight_service, cleanliness, arrival_delay_in_minutes, gender_Male, customer_type_disloyalCustomer, type_of_travel_PersonalTravel, customer_class_Eco, customer_class_EcoPlus])
    test = features.reshape(1,-1)
    prediction = variety_mappings[xGB.predict(test)[0]]
    return {'prediction': prediction}

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
