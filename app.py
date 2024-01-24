import pandas as pd
import numpy as np
import streamlit as st
import pickle as pk
import base64
from PIL import Image

im = Image.open('lung.png')
st.set_page_config(page_title="Heart Disease Predictor", page_icon = im)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('h.jpg')

st.sidebar.title('Feature Selection Menu')
choice = st.sidebar.radio("Select any",("Cardiovascular Disease Predictor","Disease Prescription"))

if choice=="Cardiovascular Disease Predictor":

    model = pk.load(open('Cardiovascular_disease.pkl', 'rb'))    
    data = pd.read_excel('health_data.xlsx')

    st.header('Heart Disease Predictor')

    gender = st.selectbox('Choose Gender', data['gender'].unique())
    if gender == 'Male':
        gender = 1
    else:
        gender = 0
   

    age = st.number_input('Enter Age',min_value=0, max_value=150,value=45,step=5)
    cholesterol	 = st.number_input('patient cholesterol',min_value=0, max_value=2,step=1)
    gluc	 = st.number_input('Enter gluc level',min_value=0, max_value=2,step=1)
    smoke	 = st.number_input('Is patient smoking',min_value=0, max_value=1,step=1)
    alco	 = st.number_input('Is patient alcoholic',min_value=0, max_value=1,step=1)
    active = st.number_input('Is patient active',min_value=0, max_value=1,step=1)
    height	 = st.number_input('Enter height',min_value=0, max_value=500,value=162,step=5)
    weight	 = st.number_input('Enter weight',min_value=0, max_value=300,value=52,step=1)
    syst_bp = st.number_input('Enter syst_bp',min_value=0, max_value=200,value=110,step=10)
    diast_bp	 = st.number_input('Enter diast_bp',min_value=0, max_value=150,value=80,step=10)

    hide_default_format = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_default_format, unsafe_allow_html=True)

    if st.button('Predict'):
        input = np.array([gender,age,cholesterol,gluc,smoke,smoke,alco,active,height,weight,syst_bp,diast_bp]).reshape(1, -1)
 
        bmi = int(weight/((height / 100 ) ** 2))
        inp = np.array([bmi,age,syst_bp,diast_bp]).reshape(1,-1)
        output = model.predict(inp)
        if output[0] == 0:
            stn = 'Patient is Healthy,No heart Disease'
        else:
            stn = 'Patient may have Heart Disease'
        st.markdown(stn)
        

    copyright_html = """
    <div style="text-align: center; padding: 10px;">
    <p style="margin: 0;">&copy; 2024 Your Company. All rights reserved.</p>
    </div>
    """
    st.markdown(copyright_html, unsafe_allow_html=True)


elif choice == 'Disease Prescription':

    st.title("Disease Prescription")
    st.header("Cardiovascular-Disease")
    st.write("Cardiovascular disease (CVD), also known as heart disease, encompasses a group of disorders affecting the heart and blood vessels. These disorders impair the circulatory system's ability to effectively deliver oxygen and nutrients throughout the body, leading to various health complications. Currently solving this issue, which is why this was developed.Thus predictable.This forecast is predicated on the attribute shown below.Following this, determine whether cardiovascular disease is present or not.")
    st.subheader("BMI (Body Mass Index)")
    st.write("BMI is a useful measure of overweight and obesity. It is calculated from your height and weight. BMI is an estimate of body fat and a good gauge of your risk for diseases that can occur with more body fat. The higher your BMI, the higher your risk for certain diseases such as heart disease, high blood pressure, type 2 diabetes, gallstones, breathing problems, and certain cancers.")
    st.write("A dimensionless measure of relative weight and height used to categorize an individual's potential risk of health conditions linked to body weight.")
    st.write("                    bmi = weight(kg)/(height(cm))2")
    st.subheader("Range:")
    st.markdown("- 	Underweight: Below 18.5 kg/m²")
    st.markdown("- 	Normal weight: 18.5 - 24.9 kg/m²")
    st.markdown("- 	Overweight: 25 - 29.9 kg/m²")
    st.markdown("- 	Obese: 30 kg/m² and above")
    st.subheader("Blood pressure:")
    st.write("Systolic pressure is the maximum pressure exerted by the blood against the walls of arteries during the contraction phase of the heart, representing the peak pressure within the cardiac cycle.")
    st.write("Diastolic pressure is the minimum pressure exerted by the blood against the walls of arteries during the relaxation phase of the heart, representing the residual pressure within the cardiac cycle.")
    st.markdown("Below is the range:")
    st.image("bp.jpg")
    st.subheader("Cholesterol:")
    st.write("A waxy, fat-like substance naturally produced by the liver and found in certain foods. It plays essential roles in the body, but high levels can contribute to the development of heart disease and other health problems.")
    st.write("Here is used,")
    st.markdown("- Normal ")
    st.markdown("- Above Normal")
    st.markdown("- Well above normal ")
    st.subheader("Glucose:")
    st.write("A simple sugar molecule, also known as dextrose, that constitutes the primary energy source for most living organisms. It plays a vital role in cellular metabolism and is a key regulator of various physiological processes.")
    st.write("Here is used,")
    st.markdown("- Normal ")
    st.markdown("- Above Normal")
    st.markdown("- Well above normal ")
    st.subheader("Others attribute:")
    st.write("Smoking,alcohol intake and physical activity are also effected to cardiovascular.")
    st.markdown("- Smoking: A binary variable indicating whether someone smokes or not (smoke).")    
    st.markdown("- Alcohol intake: A binary variable indicating whether someone consumes alcohol or not (alco).")    
    st.markdown("- Physical activity: A binary variable indicating whether someone is physically active or not (active)")    
    st.subheader('Risk Factors for Health Topics Associated With Obesity')
    st.write('Risk Factors')
    st.markdown('- High blood pressure (hypertension)')
    st.markdown('- High LDL cholesterol ("bad" cholesterol)')
    st.markdown('- Low HDL cholesterol ("good" cholesterol))')
    st.markdown('- High triglycerides')
    st.markdown('- High blood glucose (sugar)')
    st.markdown('- Physical inactivity')
    st.markdown('- Smoking')

else :
    def simple_chatbot(user_input, history):
        if user_input == 'what is project theme?':
            return "Our Project Theme is Heart disease predictor, it is called Apollo 20"
        elif user_input == 'Tell me about heart disease':
            return "Please refer to the disease and prescription page."
        elif user_input == 'Hi, how are you?':
            return "I'm good. What about you?"
        elif user_input == 'I am also good':
            return "Sounds Good"
        elif user_input == 'Help':
            return "Do you need any help?"
        else:
            return "I'm sorry, I didn't understand that."

    def main():
        st.title("Simple Chatbot")

        # Initialize history list
        history = []

        user_input = st.text_input("You:", "")
        
        if st.button("Submit"):
            response = simple_chatbot(user_input, history)
            history.append((user_input, response))

        # Display history
        for user_query, bot_response in history[-5:]:  # Display the last 5 entries
            st.text(f"You: {user_query}")
            st.text(f"Bot: {bot_response}")
            st.text("----")

    if __name__ == "__main__":
        main()
