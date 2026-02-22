import streamlit as st
import numpy as np

st.title("Clase 4 - Numpy")
st.sidebar.image("logo.png")
st.sidebar.title("Parámetros")

elemetos = st.sidebar.slider("Ingrese la cantidad de elementos:",1, 60)

arreglo=np.arange(elemetos)

st.write(arreglo)

st.sidebar.write("Elaborado por:")
st.sidebar.write("Jeancarlos Amaya")