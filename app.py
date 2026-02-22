import streamlit as st

st.set_page_config(
    page_title="Luis Alfredo Carrillo | Marine Spatial Intelligence Specialist",
    layout="wide"
)
st.markdown("""
<style>

/* Oculta el icono original */
button[data-testid="collapsedControl"] svg {
    display: none;
}

/* Agrega el icono hamburguesa */
button[data-testid="collapsedControl"]::before {
    content: "☰";
    font-size: 22px;
}

/* Agrega texto debajo */
button[data-testid="collapsedControl"]::after {
    content: " Menú";
    font-size: 14px;
    display: block;
    margin-top: -2px;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## ☰")
st.sidebar.markdown("Menú")

st.title("🌊 Marine Spatial Intelligence Portfolio")
st.subheader("M en C. Luis Alfredo Carrillo Aguilar")
st.markdown("""
correo: raya.torpedo@gmail.com

celular: 6121072580
""")
with open("CV_Luis_Alfredo_Carrillo_2026.pdf", "rb") as file:
    st.download_button(
        label="Descargar CV",
        data=file,
        file_name="CV_Luis_Alfredo_Carrillo_2026.pdf",
        mime="application/pdf")
st.markdown("""
Especialista en análisis espacial marino, fotogrametría 3D y modelado ambiental aplicado a conservación.

Este portafolio muestra herramientas interactivas desarrolladas para apoyar la toma de decisiones en conservación marina.
""")

#st.image("D:/Users/User/Desktop/2026/Portafolio/assets/mapa_3d.png", use_container_width=True)
st.video("assets/comparacion_mapas_final.mp4")
st.markdown("Comparación de cobertura coralina entre diciembre 2023 y febrero 2024 en el mismo parche arrecifal.")

st.markdown("---")
st.markdown("Selecciona un proyecto en el menú lateral.")