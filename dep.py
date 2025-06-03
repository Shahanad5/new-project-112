import streamlit as st

import joblib
sn=joblib.load("lung_model.pkl")
s=joblib.load("scaler.pkl")


st.title('Lung Cancer Data Analysis')

st.write("Enter Lung Cancer Description")
                     
AGE = st.number_input("Enter Age",key="age")
GENDER = st.number_input("GENDER, Enter 1 IF MALE OR 0 FOR FEMALE",key="gender")  
SMOKING = st.number_input(" DO YOU SMOKE, Enter 1 IF YES OR 0 IF NO",key="smoking")  
FINGER_DISCOLORATION = st.number_input(" FINGER_DISCOLORATION, Enter 1 IF YES OR 0 IF NO",key="finger_discoloration")  
MENTAL_STRESS = st.number_input("MENTAL STRESS, Enter 1 IF YES OR 0 IF NO",key="mental_stress")  
EXPOSURE_TO_POLLUTION = st.number_input(" EXPOSURE TO POLUTION,Enter 1 IF YES OR 0 IF NO",key="exp_to_pol")  
LONG_TERM_ILLNESS = st.number_input("ANY LONG TERM ILLNESS, Enter 1 IF YES OR 0 IF NO",key="long_ter_ill")  
ENERGY_LEVEL = st.number_input("Enter ENERGY LEVEL(Range from 30-77)",key="energy_level")  
IMMUNE_WEAKNESS =st.number_input(" ARE YOU IMMUNE WEAK, Enter 1 IF YES OR 0 IF NO",key="immune")  
BREATHING_ISSUE = st.number_input(" ANY BREATHING ISSUE, Enter 1 IF YES OR 0 IF NO",key="breathing")  
ALCOHOL_CONSUMPTION =st.number_input(" DO YOU CONSUME ALCOHOL, Enter 1 IF YES OR 0 IF NO",key="alcohol")  
THROAT_DISCOMFORT = st.number_input(" ANY THROAT DISCOMFORT, Enter 1 IF YES OR 0 IF NO",key="throat")  
OXYGEN_SATURATION =st.number_input("Enter OXYGEN SATURAION (range from 90 to 99 ",key="oxygen")  
CHEST_TIGHTNESS = st.number_input("DO YOUU HAVE CHEST TITENESS, Enter 1 IF YES OR 0 IF NO",key="chest")  
FAMILY_HISTORY =st.number_input("ANYBODY IN FAMILY HAS THIS DISEASE, Enter 1 IF YES OR 0 IF NO",key="family")  
SMOKING_FAMILY_HISTORY =st.number_input("DOES ANY OF YOUR FAMILY MEMBER HAS HISTORY OF SMOKING, Enter 1 IF YES OR 0 IF NO",key="smoking_family")  
STRESS_IMMUNE =st.number_input(" DO YOU HAVE STRESS IMMUNITY ISSUES, Enter 1 IF YES OR 0 IF NO",key="stress")  

if st.button('predict'):
    result=sn.predict([[AGE,GENDER,SMOKING,FINGER_DISCOLORATION,MENTAL_STRESS,EXPOSURE_TO_POLLUTION,LONG_TERM_ILLNESS,ENERGY_LEVEL,IMMUNE_WEAKNESS,BREATHING_ISSUE,ALCOHOL_CONSUMPTION,THROAT_DISCOMFORT,OXYGEN_SATURATION,CHEST_TIGHTNESS,FAMILY_HISTORY,SMOKING_FAMILY_HISTORY,STRESS_IMMUNE]])[0] 
    st.success('the output is {} (1 for yes and 0 for no)'.format(result))
    