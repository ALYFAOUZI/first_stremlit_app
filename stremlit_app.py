import streamlit
import pandas
import requests


streamlit.title('My Parents New Healthy Dinner incha ALLAH')
streamlit.header('Breakfast Menu Incha ALLAH')
streamlit.text('🥣 Omega 3 Blueberry oatmeal incha ALLAH')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie incha ALLAH')
streamlit.text('🐔 Hard-Boiled Free range-Egg incha ALLAH')
streamlit.text('🥑 Avocado Toast incha ALLAH')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)
streamlit.text(fruityvice_response.jzon())
