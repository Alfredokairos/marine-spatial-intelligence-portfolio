import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Luis Alfredo Carrillo | Marine Spatial Intelligence Specialist",
    layout="wide"
)

st.markdown("""
<style>

div[data-baseweb="radio"] div {
    font-size: 22px !important;
    font-weight: 600 !important;
}

</style>
""", unsafe_allow_html=True)

pagina = st.radio(
    "☰ Menú",
    ["Inicio", "Climatologías", "Fotogrametría", "Mapas interactivos"],
    horizontal=True
)
st.divider()
if pagina == "Inicio":
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
 
elif pagina == "Fotogrametría":
    st.title("🪸 Fotogrametría 3D de Arrecifes")

    st.header("El Problema")

    st.markdown("""
    Los arrecifes de coral están experimentando degradación acelerada debido al calentamiento oceánico y disturbios locales.
    Sin mediciones precisas, es difícil cuantificar cambios en complejidad y rugosidad.
    """)

    st.header("La Solución Técnica")

    st.markdown("""
    - Modelos 3D generados en Agisoft Metashape.  
    - Cálculo de rugosidad y mediciones estructurales.  
    - Análisis espacial en QGIS.  
    """)

    st.header("Modelo 3D / Imagen")

    st.image("assets/mapa_coral.jpeg", use_container_width=True)

    st.header("Aplicación en Conservación")

    st.markdown("""
    Permite:
    - Medir cambios estructurales post-blanqueamiento.
    - Priorizar zonas de restauración.
    - Evaluar éxito de intervenciones.
    """)
        
elif pagina == "Climatologías":
    st.title("🌡 Climatología de Temperatura y Clorofila")

    st.header("El Problema")

    st.markdown("""
    Las anomalías térmicas están asociadas a eventos de blanqueamiento.
    Entender patrones espaciales de temperatura y productividad es clave.
    """)

    st.header("Visualización")
    st.subheader("Temperatura superficial del mar")
    st.image("assets/temperatura.png", width="stretch")
    st.subheader("Clorofila")
    st.image("assets/clorofila.png", width="stretch")



    st.header("Aplicación")

    st.markdown("""
    - Identificación de hotspots térmicos.  
    - Planeación de monitoreo adaptativo. 
    - Integración con alertas tempranas.  
    """)
    
elif pagina == "Mapas interactivos":
    st.title("🗺 Mapas Interactivos de Conservación")

    st.header("El Problema")

    st.markdown("""
    Los datos espaciales suelen presentarse de forma estética, dificultando exploración y toma de decisiones.
    """)

    st.subheader("Hotspot espaciales por especie") 
    st.info("🗂️ Selecciona una especie en el ícono de capas (arriba a la derecha del mapa).")

    with open("data/Temporada por especie.html", "r", encoding="utf-8") as f:
        html_map = f.read()
    html_map = html_map.replace(
        "scrollWheelZoom: true",
        "scrollWheelZoom: false"
    )

    components.html(html_map, height=450)

    st.subheader("Distribución espacial de pesca por arponeo")

    with open("data/pesca.html", "r", encoding="utf-8") as f:
        html_map = f.read()

    components.html(html_map, height=450)

    st.header("Aplicación")

    st.markdown("""
    - Visualización de incidentes.
    - Monitoreo de fauna.
    - Planeación espacial marina.
    """)
    