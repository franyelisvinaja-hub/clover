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

# 3. Estética: Fuentes Elegantes, Fondo Beige y Texto Blanco
st.markdown("""
    <style>
    /* IMPORTAR FUENTE ELEGANTE (Opcional, pero Georgia ya viene en el sistema) */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');

    /* FONDO DE LA PÁGINA: Beige Claro */
    .stApp {
        background-color: #F5F5DC; 
    }
    
    /* FUENTE GLOBAL: Forzamos Georgia o Times New Roman */
    html, body, [class*="css"], .stMarkdown, p, span {
        font-family: 'Georgia', 'Times New Roman', serif !important;
        color: #2D4739; /* Un verde muy oscuro para el texto, casi negro */
    }

    /* ESTILO DEL SIDEBAR */
    [data-testid="stSidebar"] {
        background-color: #1B3022 !important; /* Verde Bosque */
    }

    /* TÍTULOS ELEGANTES */
    h1, h2, h3, .stTitle {
        font-family: 'Georgia', serif !important;
        color: #1B3022 !important;
        font-weight: 700;
    }

    /* BARRAS DE NAVEGACIÓN (Radio Buttons como botones) */
    div[role="radiogroup"] > label {
        background-color: #2D4739 !important; /* Verde intermedio */
        border: 1px solid #4B5D43 !important;
        padding: 12px 20px !important;
        border-radius: 8px !important;
        margin-bottom: 10px !important;
        width: 100% !important;
    }

    /* TEXTO DE LAS BARRAS: Blanco Total */
    div[role="radiogroup"] > label div[data-testid="stMarkdownContainer"] p {
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: 400 !important;
    }

    /* EFECTO HOVER (Pasar el mouse) */
    div[role="radiogroup"] > label:hover {
        background-color: #588157 !important;
        cursor: pointer;
    }

    /* OCULTAR EL CÍRCULO DEL RADIO */
    div[role="radiogroup"] > label > div:first-child {
        display: none !important;
    }
    
    /* LÍNEA DIVISORA */
    hr {
        border-top: 1px solid #D4D4AC !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color: white; text-align: center; font-family: Georgia;'>Four Essences</h2>", unsafe_allow_html=True)
    st.write("") 
    
    pagina = st.radio(
        label="", 
        options=["Sobre nosotros", "Línea cosmética 'CLOVER'", "Aceites esenciales"],
        label_visibility="collapsed" 
    )
    
    st.markdown("---")
    st.markdown("<p style='color: #F5F5DC; text-align: center; font-style: italic;'>Innovación desde el laboratorio</p>", unsafe_allow_html=True)

# --- CONTENIDO ---
if pagina == "Sobre nosotros":
    st.title("Nuestra Historia")
    st.write("En **Four Essences**, creemos en la ciencia aplicada a la naturaleza...")

elif pagina == "Línea cosmética 'CLOVER'":
    st.title("Línea CLOVER")
    st.write("Productos diseñados con extractos de orégano y clavo...")

elif pagina == "Aceites esenciales":
    st.title("Extractos Puros")
    st.write("Destilación por arrastre de vapor de alta pureza...")
