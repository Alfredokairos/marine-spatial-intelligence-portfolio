import streamlit as st
import streamlit.components.v1 as components

st.title("🗺 Mapas Interactivos de Conservación")

st.header("El Problema")

st.markdown("""
Los datos espaciales suelen presentarse de forma estática, dificultando exploración y toma de decisiones.
""")

st.subheader("Hotspot espaciales por especie") 

with open("data/Temporada por especie.html", "r", encoding="utf-8") as f:
    html_map = f.read()

components.html(html_map, height=700, width=1000)

st.subheader("Distribución espacial de pesca por arponeo")

with open("data/pesca.html", "r", encoding="utf-8") as f:
    html_map = f.read()

components.html(html_map, height=700, width=1000)

st.header("Aplicación")

st.markdown("""
- Visualización de incidentes
- Monitoreo de fauna
- Planeación espacial marina
""")