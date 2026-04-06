
import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st

# 1. Configuración de la página (DEBE SER LA PRIMERA LÍNEA DE STREAMLIT)
st.set_page_config(
    page_title="Four Essences",
    page_icon="🌿",
    layout="wide"
)

# 2. ENCABEZADO 
st.markdown("""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <img src="logo.png" 
        style="width:100%; height:150px; object-fit: cover; border-radius: 10px;">
    </div>
    """, unsafe_allow_html=True)

# 3. Estética 
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Georgia', sans-serif;
    }
    [data-testid="stSidebar"] {
        background-color: #1B3022; 
        color: white;
     } 
    /* Color de fondo de la aplicación (usando un verde muy claro/crema) */
    .main {
        background-color: #F0F2EB;
    }
    /* Color de los títulos (un verde oscuro profundo) */
    .stTitle, h1, h2, h3 {
        color: #1B3022;
    </style>
    """, unsafe_allow_html=True)

# SIDEBAR
pagina = st.sidebar.radio(
with st.sidebar:
    st.header("🌱 Sobre nosotros")
    st.header("🪴 Productos CLOVER")
    st.header("🍃 Aceites esenciales")
    

# --- SECCIÓN: SOBRE NOSOTROS ---
if pagina == "Sobre nosotros":
    st.title("Sobre Nosotros")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Nuestra Esencia")
        # Usamos comillas triples para textos largos
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
    # Corregido: Puse comillas triples para que el texto pueda fluir sin errores
    st.write("""
        Nuestros aceites e hidrolatos son obtenidos mediante procesos de **destilación por arrastre de vapor**, 
        asegurando la máxima pureza y preservación de compuestos químicos clave.
    """)
    
    aceites = ["Orégano", "Clavo de olor", "Eucalipto"]
    st.selectbox("Consulta disponibilidad de aceite:", aceites)
