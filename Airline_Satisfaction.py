# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:44:25 2021

@author: jeshm
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class AirlineSatisfaction(BaseModel):
    age: float
    inflight_wifi_service: float
    departure_arrival_time_convenient: float
    ease_of_online_booking: float
    gate_location: float
    food_and_drink: float
    online_boarding: float
    seat_comfort: float
    inflight_entertainment: float
    onboard_service: float
    leg_room_service: float
    baggage_handling: float
    checkin_service: float
    inflight_service: float
    cleanliness: float
    departure_delay_in_minutes : float
    arrival_delay_in_minutes: float
    gender_Male: float
    customer_type_disloyalCustomer: float	
    type_of_travel_PersonalTravel:float	
    customer_class_Eco: float	
    customer_class_EcoPlus:float
