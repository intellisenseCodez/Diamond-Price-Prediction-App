import pickle
import streamlit as st
import numpy as np
import sklearn

with open(file="./diamond_linear_model.pickle", mode="rb") as model_file:
    model = pickle.load(model_file)


def predict(carat, cut, color, clarity, dept, table, x_length, y_length, z_length):
    
    if cut == "Fair":
        cut_fair = 1
        cut_good, cut_very_good, cut_premium, cut_ideal = 0,0,0,0
    elif cut == "Good":
        cut_good = 1
        cut_fair, cut_very_good, cut_premium, cut_ideal = 0,0,0,0
    elif cut == "Very Good":
        cut_very_good = 1
        cut_fair, cut_good, cut_premium, cut_ideal = 0,0,0,0   
    elif cut == "Premium":
        cut_premium = 1
        cut_fair, cut_good, cut_very_good, cut_ideal = 0,0,0,0
    elif cut == "Ideal":
        cut_ideal = 1
        cut_fair, cut_good, cut_very_good, cut_premium = 0,0,0,0
        
        
    if color == "J":
        color_J = 1
        color_I, color_H, color_G, color_F, color_E, color_D = 0,0,0,0,0,0
    elif color == "I":
        color_I = 1
        color_J, color_H, color_G, color_F, color_E, color_D = 0,0,0,0,0,0 
    elif color == "H":
        color_H = 1
        color_J, color_I, color_G, color_F, color_E, color_D = 0,0,0,0,0,0  
    elif color == "G":
        color_G = 1
        color_J, color_I, color_H, color_F, color_E, color_D = 0,0,0,0,0,0
    elif color == "F":
        color_F = 1
        color_J, color_I, color_H, color_G, color_E, color_D = 0,0,0,0,0,0 
    elif color == "E":
        color_E = 1
        color_J, color_I, color_H, color_G, color_F, color_D = 0,0,0,0,0,0   
    elif color == "D":
        color_D = 1
        color_J, color_I, color_H, color_G, color_F, color_E = 0,0,0,0,0,0 
        
    if clarity == "I1":
        clarity_I1 = 1
        clarity_SI2, clarity_SI1, clarity_VS2, clarity_VS1, clarity_VVS2, clarity_VVS1, clarity_IF = 0,0,0,0,0,0,0
    elif clarity == "SI2":
        clarity_SI2 = 1
        clarity_I1, clarity_SI1, clarity_VS2, clarity_VS1, clarity_VVS2, clarity_VVS1, clarity_IF = 0,0,0,0,0,0,0
    elif clarity == "SI1":
        clarity_SI1 = 1
        clarity_I1, clarity_SI2, clarity_VS2, clarity_VS1, clarity_VVS2, clarity_VVS1, clarity_IF = 0,0,0,0,0,0,0
    elif clarity == "VS2":
        clarity_VS2 = 1
        clarity_I1, clarity_SI2, clarity_SI1, clarity_VS1, clarity_VVS2, clarity_VVS1, clarity_IF = 0,0,0,0,0,0,0
    elif clarity == "VS1":
        clarity_VS1 = 1
        clarity_I1, clarity_SI2, clarity_SI1, clarity_VS2, clarity_VVS2, clarity_VVS1, clarity_IF = 0,0,0,0,0,0,0
    elif clarity == "VVS2":
        clarity_VVS2 = 1
        clarity_I1, clarity_SI2, clarity_SI1, clarity_VS2, clarity_VS1, clarity_VVS1, clarity_IF = 0,0,0,0,0,0,0
    elif clarity == "VVS1":
        clarity_VVS1 = 1
        clarity_I1, clarity_SI2, clarity_SI1, clarity_VS2, clarity_VS1, clarity_VVS2, clarity_IF = 0,0,0,0,0,0,0
    elif clarity == "IF":
        clarity_IF = 1
        clarity_I1, clarity_SI2, clarity_SI1, clarity_VS2, clarity_VS1, clarity_VVS2, clarity_VVS1 = 0,0,0,0,0,0,0

   
    X_test = np.array([[carat, dept, table, x_length, y_length, z_length, cut_fair, cut_good, cut_ideal, cut_premium, cut_very_good, color_D, color_E, color_F, color_G, color_H, color_I, color_J, clarity_I1, clarity_IF, clarity_SI1, clarity_SI2, clarity_VS1, clarity_VS2, clarity_VVS1, clarity_VVS2 ]])
    
    
    y_predict = model.predict(X_test)
    
    return y_predict

st.title("Diamond Price Predictor")
st.write("The ML App enables Dealers or Cutormers to Predict the price of Diamond.")

st.header("Enter the characteristics of the diamond.")

# carat input
carat = st.number_input(label="Carat Weight:", min_value=0.1, max_value=10.0, value=1.0)

#  cut input
cut = st.selectbox(label="Cut Rating", options=["Fair", "Good", "Very Good", "Premium", "Ideal"])

# color input
color = st.selectbox(label="Color Rating", options=["J", "I", "H", "G", "F", "E", "D"])

# clarity input
clarity = st.selectbox(label="Clarity Rating", options=['SI2', 'SI1', 'VS1', 'VS2', 'VVS2', 'VVS1', 'I1', 'IF'])

# dept input
dept = st.number_input(label="Diamond Depth Percentage:", min_value=0.1, max_value=100.0, value=1.0)

# dept input
table = st.number_input(label="Diamond Table Percentage:", min_value=0.1, max_value=100.0, value=1.0)

# x input
x_length = st.number_input(label="Diamond Length (X) in mm:", min_value=0.1, max_value=10.0, value=1.0)

# y input
y_length = st.number_input(label="Diamond Length (Y) in mm:", min_value=0.1, max_value=10.0, value=1.0)

# z input
z_length = st.number_input(label="Diamond Length (Z) in mm:", min_value=0.1, max_value=10.0, value=1.0)


if st.button(label="Predict Price"):
    price = predict(carat, cut, color, clarity, dept, table, x_length, y_length, z_length)
    
    st.success(f"The Predicted Price of the Diamond is ${price[0]:.2f} USD")