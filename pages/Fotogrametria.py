import streamlit as st

st.title("🪸 Fotogrametría 3D de Arrecifes")

st.header("El Problema")

st.markdown("""
Los arrecifes de coral están experimentando degradación acelerada debido al calentamiento oceánico y disturbios locales.
Sin mediciones precisas, es difícil cuantificar cambios en complejidad y rugosidad.
""")

st.header("La Solución Técnica")

st.markdown("""
- Modelos 3D generados en Agisoft Metashape  
- Cálculo de rugosidad y mediciones estructurales  
- Análisis espacial en QGIS  
""")

st.header("Modelo 3D / Imagen")

st.image("assets/mapa_coral.jpeg", use_container_width=True)

st.header("Aplicación en Conservación")

st.markdown("""
Permite:
- Medir cambios estructurales post-blanqueamiento
- Priorizar zonas de restauración
- Evaluar éxito de intervenciones
""")