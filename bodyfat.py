from PIL import Image
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd


# loading the saved models

bodyfat_model = pickle.load(open('bodyfat_model3.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Body Fat Prediction System',
                          ['Fat Prediction',
                           'Body Mass Index',
                           'Solution'],
                          icons=['activity','heart','person'],
                          default_index=0)
    

# Diabetes Prediction Page
if (selected == 'Fat Prediction'):
    
    # page title
    st.title('Body Fat Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    
    with col1:
        Age = st.text_input('Age of the Person')
        
    with col2:
        Weight = st.text_input('Weight of the Person')
    
    with col1:
        Height = st.text_input('Height in cm')
    
    with col2:
        Abdomen= st.text_input('Abdomen size in cm')
    
    with col1:
       Hip = st.text_input('Hip size value in cm')
    
   
    # code for Prediction
    fat_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Bodyfat Test Result'): 
        new_data = pd.DataFrame([[Age, Weight, Height, Abdomen, Hip,]])
        new_pred = bodyfat_model.predict(new_data)
        
    st.write('Predicted body fat percentage:')
    
    st.success(new_data)
        
    
    

        
if (selected == 'Body Mass Index'):
    
    # page title
    st.title('Body Mass Index')
    # page title
    image = Image.open('OPI.jpg')
    st.image(image, caption='BMI')
    st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
    st.header(" Hello  World !! Do you know your BMI?")

    st.write("The BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg/m²")
    display = ("male", "female")

    options = list(range(len(display)))

    value = st.sidebar.selectbox("Gender", options, format_func=lambda x: display[x])

    st.write(value)

    age = st.slider('How old are you?', 17,135)
    st.write("I'm ", age, 'years old')
    Weight= st.slider('What is your weight?', 15,200)
    st.write("My weight is", Weight, ' kg')
    Height=st.slider('What is your height',1.0, 2.10)
    st.write("My height is", Height, 'm')
    if (st.button("Click HERE to get your BMI")):
        Weight/(Height*Height)
    BMI=Weight/(Height*Height)
    # if a person has a BMI less than 16.5
    if BMI< 16.5:
        st.write( 'The person is famine')
    # if a person's BMI is at least 16.5 but less than 18.5
    elif BMI>= 16.5 and BMI <  18.5:
        st.write( 'The person is underweight')
    # if a person's BMI is at least 18.5 but less than 25
    elif BMI>= 18.5 and BMI < 25.0:
        st.write( 'The person is healthy weight')
    # if a person's BMI is at least 25 but less than 30
    elif BMI>= 25.0 and BMI < 30.0:
        st.write( 'The person is overweight')
    # if a person's BMI is at least 30 but less than 35
    elif BMI>= 30.0 and BMI < 35.0:
        st.write('The person is moderate obesity')
    # if a person's BMI is at least 35 but less than 40
    elif BMI>= 35.0 and BMI < 40.0:
        st.write('The person is severe obesity')
    else:
        st.write(' The person is morbid obesity')
        
        
        
        
        
if (selected == 'Solution'):
    
    # page title
    st.title('How to lose Fat')
    
    st.write('There are several ways to lose fat in your body, here are some effective strategies: ')
    st.write('1. Create a Caloric Deficit: In order to lose fat, you need to create a calorie deficit by consuming fewer calories than you burn. This can be achieved by reducing your food intake, increasing your physical activity, or a combination of both. Follow a Healthy Diet: Eating a healthy, balanced diet is essential for weight loss. Focus on consuming whole, nutrient-dense foods such as fruits, vegetables, lean proteins, and complex carbohydrates. Limit your intake of processed foods, sugary drinks, and high-fat foods. Increase Physical Activity: Incorporating regular physical activity into your routine can help you burn more calories and lose fat. Aim for at least 150 minutes of moderate-intensity activity or 75 minutes of vigorous-intensity activity per week.') 
    st.write('2. Resistance Training: Incorporating resistance training exercises, such as weight lifting or bodyweight exercises, can help you build muscle mass and increase your metabolism, which can help you burn more fat even at rest.')
    st.write('3. Get Enough Sleep: Sleep plays an important role in weight loss and fat loss. Aim for 7-9 hours of quality sleep per night. Lack of sleep can increase hunger and cravings, leading to overeating and weight gain. Manage Stress: Chronic stress can lead to weight gain and increased body fat. Incorporate stress-management techniques, such as meditation, deep breathing, or yoga, to help you manage stress and improve your overall health. Remember, losing fat takes time and effort.') 
    st.write('Its important to make sustainable lifestyle changes and be patient with the process. Consult with a healthcare professional before starting any weight loss program.')
    image2 = Image.open('diet.jpg')

    st.image(image2, caption='Your life is very precious')









