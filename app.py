import streamlit as st
import pickle 

# Load the saved model (adjust based on your saving method)
with open('model.pkl', 'rb') as file:
    model = pickle.load(file) 

# ... (Your user input handling and prediction logic here)