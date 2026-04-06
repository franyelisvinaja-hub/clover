
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Configuración de la página
st.set_page_config(  page_title="Four Essences",   page_icon="🌿",   layout="wide")

# ENCABEZADO
st.markdown("""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <img src="C:\Users\milei\Downloads\Diseño sin título.png" 
        style="width:100%; height:150px; object-fit: cover; border-radius: 10px;">
    </div>

# Estética
st.markdown(""" <style>   .main {    background-color: #f5f7f1;  }
    .stTitle {
        color: #2e4a31;
        font-family: 'Helvetica', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAV ---
st.sidebar.title("🌿 Four Essences")
st.sidebar.markdown("---")
pagina = st.sidebar.radio(
    "Navegación",
    ["Sobre nosotros", "Línea cosmética 'CLOVER'", "Aceites esenciales"]
)

st.sidebar.info("Innovación química y natural desde Venezuela.")

# --- SECCIÓN: SOBRE NOSOTROS ---
if pagina == "Sobre nosotros":
    st.title("Sobre Nosotros")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Nuestra Esencia")
        st.write("""
            En **Four Essences**, fusionamos el rigor de la ingeniería química con la pureza de la 
            naturaleza. Nos dedicamos a la investigación y desarrollo de productos que 
            resaltan el bienestar a través de procesos optimizados y materias primas de alta calidad.
        """)
        st.write("**Misión:** Transformar extractos botánicos en soluciones cosméticas de grado industrial.")
  
# --- SECCIÓN: LÍNEA CLOVER ---
elif pagina == "Línea cosmética 'CLOVER'":
    st.title("🍀 Línea Cosmética CLOVER")
    st.markdown("### Cuidado botánico avanzado")
    
    st.write("""
        CLOVER es nuestra línea insignia, diseñada bajo principios de formulación técnica 
        y estabilidad química. Cada producto está pensado para ofrecer resultados reales 
        respetando la barrera cutánea.
    """)
    
    # Grid de productos
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("**Sérum Facial**")
        st.caption("Alta concentración de activos.")
    with col_b:
        st.markdown("**Tónico Equilibrante**")
        st.caption("Hidratación profunda.")
    with col_c:
        st.markdown("**Crema Hidratante**")
        st.caption("Textura ligera y nutritiva.")

# --- SECCIÓN: ACEITES ESENCIALES ---
elif pagina == "Aceites esenciales":
    st.title("💧 Aceites Esenciales")
    st.write("""
        Nuestros aceites y hidrolatos son obtenidos mediante procesos de **destilación por arrastre de vapor**, 
        asegurando la máxima pureza y preservación de compuestos químicos clave.
    """)
    
    # Expander para detalles técnicos
    with st.expander("Ver métodos de extracción"):
        st.write("""
            - **Destilación:** Control riguroso de temperatura y tiempo.
            - **Pureza:** Sin fragancias sintéticas añadidas.
            - **Origen:** Botánicos seleccionados localmente.
        """)
    
    # Ejemplo de lista de aceites
    aceites = ["Orégano", "Clavo de olor", "Eucalipto"]
    st.selectbox("Consulta disponibilidad de aceite:", aceites)
