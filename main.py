import streamlit as st

st.title('Weather Forecast for the Next Days')
st.write('Place')
place = st.text_input(label="Place:", placeholder="Add a place")
st.write('Forecast Days')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help="Select the number of forecasted Days")
st.write('Select Days to view')
option = st.selectbox('Select Data to View', ["Temperature", "Sky"])
st.subheader(f'{option} for the next {days} days in {place}')
