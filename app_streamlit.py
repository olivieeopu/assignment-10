import streamlit as st
import requests

st.title("Spaceship Titanic Prediction")

# INPUT USER
Name = st.text_input("Name", "John Doe")
PassengerId = st.text_input("PassengerId", "0001_01")
HomePlanet = st.selectbox("HomePlanet", ["Earth", "Europa", "Mars"])
CryoSleep = st.selectbox("CryoSleep", [True, False])
Cabin = st.text_input("Cabin", "B/0/P")
Destination = st.selectbox("Destination", ["TRAPPIST-1e", "PSO J318.5-22", "55 Cancri e"])
Age = st.number_input("Age", 0, 100, 25)
VIP = st.selectbox("VIP", [True, False])
RoomService = st.number_input("RoomService", 0.0)
FoodCourt = st.number_input("FoodCourt", 0.0)
ShoppingMall = st.number_input("ShoppingMall", 0.0)
Spa = st.number_input("Spa", 0.0)
VRDeck = st.number_input("VRDeck", 0.0)

# PREDICT VIA API
if st.button("Predict"):
    data = {
        "PassengerId": PassengerId,
        "HomePlanet": HomePlanet,
        "CryoSleep": CryoSleep,
        "Cabin": Cabin,
        "Destination": Destination,
        "Age": Age,
        "VIP": VIP,
        "RoomService": RoomService,
        "FoodCourt": FoodCourt,
        "ShoppingMall": ShoppingMall,
        "Spa": Spa,
        "VRDeck": VRDeck,
        "Name": Name
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        result = response.json()

        if result["prediction"] == 1:
            st.success("Transported")
        else:
            st.error("Not Transported")

    except:
        st.error("errors")