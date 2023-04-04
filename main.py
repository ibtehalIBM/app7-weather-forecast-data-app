import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')
st.write('Place')
place = st.text_input(label="Place:", placeholder="Add a place")
st.write('Forecast Days')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help="Select the number of forecasted Days")
st.write('Select Days to view')
option = st.selectbox('Select Data to View', ["Temperature", "Sky"])
st.subheader(f'{option} for the next {days} days in {place}')

# def get_data(days):
#     dates = ['2023-5-2', '2023-4-1', '2023-12-8']
#     temperatures = [10, 20, 30]
#     temperatures = [temp * days for temp in temperatures]
#     return dates, temperatures

if place:
    filtered_data = get_data(place, days)
    if option == 'Temperature':
        t = [data['main']['temp'] for data in filtered_data]
        d = [data['dt'] for data in filtered_data]
        figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature'})
        st.plotly_chart(figure)
    if option == 'Sky':
        sky_conditions = [data['weather'][0]['main'] for data in filtered_data]
        print(sky_conditions)
        images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png', 'Rain': 'images/rain.png',
                  'Snow': 'images/snow.png'}
        images_path =[images[image] for image in sky_conditions]
        st.image(images_path,width=115)
