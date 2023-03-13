
import streamlit as st
from PIL import Image
image = Image.open('Pros-with-a-Diploma-in-Nutrition-Know-BMI-Can’t-Distinguish-Between-Muscle-and-Fat.jpg')
st.title(' Body Masse Index - Web Application')
st.image(image, caption='Sunrise by the mountains- SY Ousmane')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
st.header(" Hello  World !! Do you know your BMI?")

st.write(
"The BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg/m²")
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


with st.container():
    st.write("---")
    st.header("Get In Touch With Me About my Web Application!")
    st.write("##")

    # Documention: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/syousmanesy@yahoo.fr" method ="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
st.file_uploader('FILE UPLOAD')