"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

# Any time that Streamlit sees a variable or a literal value on its own line,
# it automatically writes that to your app using st.write(). 
# For more information, refer to the documentation on magic commands.
df
