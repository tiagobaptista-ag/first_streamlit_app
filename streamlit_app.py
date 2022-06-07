import streamlit 

streamlit.title('Too many cooks')

streamlit.header('Too many cooks')
streamlit.text('Too many cooks')
streamlit.text('Too many cooks')
streamlit.text('Too many cooks')
streamlit.text('Too many cooks')
                
streamlit.text('It takes a lot to make a stew')
streamlit.text('A pinch of salt and laughter too')
streamlit.text('A scoop of kids to add the spice')
streamlit.text('A dash of love to make it nice')
streamlit.text('And you ve got...')
streamlit.text('🥣 🥗 🐔 🥑🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
               
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# display list
streamlit.dataframe(my_fruit_list)
