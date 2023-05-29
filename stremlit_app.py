import streamlit
import pandas
streamlit.title('My Parents New Healthy Dinner incha ALLAH')
streamlit.header('Breakfast Menu Incha ALLAH')
streamlit.text('🥣 Omega 3 Blueberry oatmeal incha ALLAH')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie incha ALLAH')
streamlit.text('🐔 Hard-Boiled Free range-Egg incha ALLAH')
streamlit.text('🥑 Avocado Toast incha ALLAH')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
