import streamlit
import pandas
import snowflake.connector
from urllib.error import URLError

streamlit.title('My New Healty Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#Snowflake-related functions
#def get_fruit_load_list():
def get_emp_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM v_employees")
        return my_cur.fetchall()
      
