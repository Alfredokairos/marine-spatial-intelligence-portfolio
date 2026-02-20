import streamlit as st


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
- Identificación de hotspots térmicos  
- Planeación de monitoreo adaptativo  
- Integración con alertas tempranas  
""")