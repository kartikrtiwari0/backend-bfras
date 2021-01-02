import streamlit as st
import pyrebase
import pandas as pd
import json
from pathlib import Path
from pandas import read_excel

import numpy as np



config = {
  "apiKey": "AIzaSyAIx800R8uEyErKdDDC4nuF9j42s6MqmVA",
  "authDomain": "bfras-d8b76.firebaseapp.com",
  "databaseURL": "https://bfras-d8b76-default-rtdb.firebaseio.com",
  "storageBucket": "bfras-d8b76.appspot.com"
}

firebase = pyrebase.initialize_app(config)
firebase.database()
db = firebase.database()


st.title('VISUALIZER FOR BEAUTY FACE RECCOMEDATION AND ANALYSIS SYSTEM')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
    .reportview-container .main footer {visibility: hidden;}  
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
input = st.sidebar.text_input('Enter your full name')



if st.button('Fetch data'):
     user = db.child("Responses").get()
     
     st.header('LINE CHART')
     st.line_chart(data=user.val(), width=250, height=250, use_container_width=True)
     st.header('BAR CHART')

     st.bar_chart(data=user.val(), width=250, height=250, use_container_width=True)
     st.header('DATA')
     st.dataframe(data=user.val(), width=None, height=None)
   