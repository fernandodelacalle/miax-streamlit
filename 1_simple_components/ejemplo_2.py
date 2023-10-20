import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Along with magic commands, st.write() is Streamlit's "Swiss Army knife".
# You can pass almost anything to st.write(): text, data, Matplotlib figures,
# Altair charts, and more. Don't worry, Streamlit will figure it out and render 
# things the right way.

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.write(fig)
