import streamlit as st
from streamlit_option_menu import option_menu
import joblib
import numpy as np


# web title
st.set_page_config(
    page_title="Mine and Rock",
)

# navigation/option
with st.sidebar:
   selected = option_menu(
        menu_title="Main Menu",  
        options=["Home", "Demo"], 
        icons=["house", "record-circle"],  
        menu_icon="cast",  # optional
        default_index=0,  # optional         
)

# option : Home
if selected == "Home":
    st.write("#Mine Rock prediction App")
   
    
    st.caption("Created by *Alden Silaban*")

# option : Demo 
if selected == "Demo":
    st.title("Mine and Rock Prediction")
    st.write("Customize the input below ")

    i1 = st.number_input("i1")
    i2 = st.number_input("i2")
    i3 = st.number_input("i3")



    ok = st.button ("predict")

    if ok:
      model=joblib.load('logistic_model.joblib')
      input_data = (i1,i2,i3)

      # changing the input_data to a numpy array
      input_data_as_numpy_array = np.asarray(input_data)

      # reshape the np array as we are predicting for one instance
      input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

      prediction = model.predict(input_data_reshaped)
        if (prediction[0]=='R'):
           st.write('The object is a Rock')
        else:
           st.write('The object is a mine')
