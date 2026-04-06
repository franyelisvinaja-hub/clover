import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Four Essences",
    page_icon="🌿",
    layout="wide"
)

# 2. Estética: Limpieza profunda y Estilo Elegante
st.markdown("""
    <style>
    /* --- ELIMINAR TEXTO 'keyboard_double_arrow' Y HEADER --- */
    header, [data-testid="stHeader"], .st-emotion-cache-6q9sum, .st-action-button {
        visibility: hidden;
        height: 0% !important;
        display: none !important;
    }
    
    /* Bloqueo específico para que no aparezca el texto del icono */
    button span {
        display: none !important;
    }

    /* --- FONDO Y FUENTES --- */
    .stApp {
        background-color: #F5F5DC; /* Beige Claro */
    }
    
    html, body, [class*="css"], .stMarkdown, p, span {
        font-family: 'Georgia', serif !important;
        color: #2D4739; 
    }

    /* --- SIDEBAR --- */
    [data-testid="stSidebar"] {
        background-color: #588157 !important; /* Verde Musgo solicitado */
    }

    /* Títulos */
    h1, h2, h3, .stTitle {
        font-family: 'Georgia', serif !important;
        color: #1B3022 !important;
        font-weight: 700;
    }

    /* --- BARRAS DE NAVEGACIÓN --- */
    div[role="radiogroup"] > label {
        background-color: #2D4739 !important; /* Verde Follaje */
        border: 1px solid #4B5D43 !important;
        padding: 12px 20px !important;
        border-radius: 8px !important;
        margin-bottom: 10px !important;
        width: 100% !important;
    }

    /* Texto blanco en las barras */
    div[role="radiogroup"] > label div[data-testid="stMarkdownContainer"] p {
        color: white !important;
        font-size: 1.1rem !important;
    }

    /* Ocultar círculo de selección */
    div[role="radiogroup"] > label > div:first-child {
        display: none !important;
    }
    
    /* Efecto al pasar el mouse */
    div[role="radiogroup"] > label:hover {
        background-color: #4B5D43 !important;
    }

    /* Texto pequeño inferior */
    .footer-text {
        color: #D4D4AC !important;
        font-size: 0.85rem !important;
        text-align: center;
        font-style: italic;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ENCABEZADO (LOGO)
st.markdown("""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <img src="https://github.com/franyelisvinaja-hub/clover/blob/main/logo.png?raw=true" 
        style="width:100%; height:300px; object-fit: cover; border-radius: 10px;"
        onerror="this.style.display='none'">
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color: white; text-align: center; font-family: Georgia;'>🌿 Menú</h2>", unsafe_allow_html=True)
    st.write("") 
    
    pagina = st.radio(
        label="nav", 
        options=["Sobre nosotros", "Línea cosmética 'CLOVER'", "Aceites esenciales"],
        label_visibility="collapsed" 
    )
    
    st.markdown("---")
    st.markdown('<p class="footer-text">FOUR ESSENCES</p>', unsafe_allow_html=True)

# --- CONTENIDO ---
if pagina == "Sobre nosotros":
    st.title("Sobre Nosotros")
    st.subheader("Ciencia y Naturaleza en Armonía")
    st.write("En **Four Essences**, desarrollamos soluciones cosméticas basadas en la investigación química...")

elif pagina == "Línea cosmética 'CLOVER'":
    st.title("🍀 Línea Cosmética CLOVER")
    st.write("Explora nuestra gama de productos con aceites esenciales de orégano y clavo...")

elif pagina == "Aceites esenciales":
    st.title("💧 Aceites Esenciales")
    st.write("Calidad premium obtenida mediante procesos optimizados de destilación...")
