import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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
try:
        fruit_choice = streamlit.text_input('What fruit would you like information about?')
if  not fruit_choice:
        streamlit.error("Please select fruit to get information.")
  else:
 #streamlit.write('The user entered ', fruit_choice)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response)
#streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
        streamlit.dataframe(fruityvice_normalized)
except URLError as e:
          streamlit.error()
    
  streamlit.stop()
#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT  * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_rows= my_cur.fetchall()
#streamlit.text("Incha ALLAH, the fruit load list contains:")
#streamlit.text(my_data_row)
streamlit.header("Incha ALLAH, the fruit load list contains:")
#streamlit.dataframe(my_data_row)
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)

my_cur.execute("INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('From Streamlit')")


