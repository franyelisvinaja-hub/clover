import streamlit as st

# 1. Configuración de la página
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

# 3. Estética: Fuentes Elegantes, Fondo Beige y Texto Blanco en Sidebar
st.markdown("""
    <style>
    /* FONDO DE LA PÁGINA: Beige Claro */
    .stApp {
        background-color: #F5F5DC; 
    }
    
    /* FUENTE GLOBAL: Forzamos Georgia */
    html, body, [class*="css"], .stMarkdown, p, span {
        font-family: 'Georgia', serif !important;
        color: #2D4739; 
    }

    /* ESTILO DEL SIDEBAR */
    [data-testid="stSidebar"] {
        background-color: #588157 !important; 
    }

    /* TÍTULOS ELEGANTES */
    h1, h2, h3, .stTitle {
        font-family: 'Georgia', serif !important;
        color: #1B3022 !important;
        font-weight: 700;
    }

    /* BARRAS DE NAVEGACIÓN (Botones del Sidebar) */
    div[role="radiogroup"] > label {
        background-color: #2D4739 !important; 
        border: 1px solid #4B5D43 !important;
        padding: 12px 20px !important;
        border-radius: 8px !important;
        margin-bottom: 10px !important;
        width: 100% !important;
    }

    /* TEXTO DE LAS BARRAS: Blanco */
    div[role="radiogroup"] > label div[data-testid="stMarkdownContainer"] p {
        color: white !important;
        font-size: 1.1rem !important;
    }

    /* OCULTAR EL CÍRCULO DEL RADIO */
    div[role="radiogroup"] > label > div:first-child {
        display: none !important;
    }
    
    /* EFECTO HOVER */
    div[role="radiogroup"] > label:hover {
        background-color: #588157 !important;
    }

    /* Ajuste para el texto pequeño de abajo */
    .footer-text {
        color: #D4D4AC !important;
        font-size: 0.85rem !important;
        text-align: center;
        font-style: italic;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    # Título superior del menú
    st.markdown("<h2 style='color: white; text-align: center; font-family: Georgia;'>🌿 Menu </h2>", unsafe_allow_html=True)
    st.write("") 
    
    # Navegación por barras
    pagina = st.radio(
        label="", 
        options=["Sobre nosotros", "Línea cosmética 'CLOVER'", "Aceites esenciales"],
        label_visibility="collapsed" 
    )
    
    st.markdown("---")
    
    # Detalle inferior: #four essences en pequeño
    st.markdown('<p class="footer-text">FOUR ESSENCES</p>', unsafe_allow_html=True)

# --- CONTENIDO DINÁMICO ---
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
