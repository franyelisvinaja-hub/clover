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

# 3. Estética: Hack para convertir Radio Buttons en Barras/Botones
st.markdown("""
    <style>
    /* Fondo general */
    .main {
        background-color: #F0F2EB;
    }
    
    /* Estilo del Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1B3022;
    }

    /* ESTILO DE BARRAS PARA EL MENÚ */
    /* Ocultamos el círculo original */
    div[data-testid="stMarkdownContainer"] p {
        font-weight: 600;
    }
    
    /* Convertir cada opción en una barra */
    div[role="radiogroup"] > label {
        background-color: #2D4739; /* Verde un poco más claro que el fondo */
        color: white !important;
        padding: 15px 20px;
        border-radius: 5px;
        border: 1px solid #4B5D43;
        margin-bottom: 10px;
        width: 100%;
        transition: all 0.3s ease;
    }

    /* Efecto cuando pasas el mouse (Hover) */
    div[role="radiogroup"] > label:hover {
        background-color: #588157;
        border-color: #A3B18A;
        cursor: pointer;
    }

    /* Estilo cuando la opción está seleccionada */
    div[role="radiogroup"] [data-checked="true"] > div {
        background-color: #588157 !important;
        font-weight: bold;
    }

    /* Esconder el círculo pequeño de radio button */
    div[role="radiogroup"] > label > div:first-child {
        display: none;
    }

    /* Títulos de la página principal */
    .stTitle, h1, h2, h3 {
        color: #1B3022;
        font-family: 'Georgia', serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color: white; text-align: center;'>🌿 Menú</h2>", unsafe_allow_html=True)
    st.write("") # Espacio
    
    # CORRECCIÓN: Agregamos una cadena vacía "" como label antes de la lista
    pagina = st.radio(
        label="", 
        options=["Sobre nosotros", "Línea cosmética 'CLOVER'", "Aceites esenciales"],
        label_visibility="collapsed" 
    )
    
    st.markdown("---")
    st.markdown("<p style='color: #A3B18A; font-size: 0.8rem; text-align: center;'>Four Essences</p>", 
                unsafe_allow_html=True)
    
# --- LÓGICA DE PÁGINAS ---
if pagina == "Sobre nosotros":
    st.title("Sobre Nosotros")
    st.subheader("Nuestra Esencia")
    st.write("En **Four Essences**, fusionamos el rigor de la ingeniería química con la pureza de la naturaleza...")

elif pagina == "Línea cosmética 'CLOVER'":
    st.title("🍀 Línea Cosmética CLOVER")
    st.write("Contenido de la línea Clover...")

elif pagina == "Aceites esenciales":
    st.title("💧 Aceites Esenciales")
    st.write("Contenido de aceites...")
