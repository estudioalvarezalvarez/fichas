import streamlit as st
from datetime import date

# Configuración de la página para celular
st.set_page_config(
    page_title="A&A - Análisis Previsional",
    page_icon="⚖️",
    layout="centered"
)

# Estilos CSS corporativos (Azul marino y celeste)
st.markdown("""
    <style>
    .main { background-color: #F8FAFC; }
    .stButton>button {
        background-color: #1B365D;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
        padding: 0.5rem;
    }
    h1, h2, h3 { color: #1B365D; }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO Y LOGO ---
col_logo, col_titulo = st.columns([1, 3])

with col_logo:
    try:
        # Aquí cargará tu logo en formato compatible
        st.image("alvarezalvarez_logo.tiff", width=80)
    except:
        st.markdown("### ⚖️ A&A")

with col_titulo:
    st.markdown("### ALVAREZ & ALVAREZ")
    st.markdown("<p style='color: #00A3FF; font-weight: bold; margin-top: -15px;'>ANÁLISIS PREVISIONAL</p>", unsafe_allow_html=True)

st.markdown("---")

# --- MENÚ DE NAVEGACIÓN ---
menu = st.sidebar.selectbox(
    "Menú de Navegación",
    ["1. Ficha del Cliente", "2. Historial de Aportes", "3. Cálculo de Derecho y Haber"]
)

# ==========================================
# 1. FICHA DEL CLIENTE
# ==========================================
if menu == "1. Ficha del Cliente":
    st.header("👤 Ficha del Cliente")
    
    with st.form("form_cliente"):
        nombre = st.text_input("Nombre y Apellido", "CABEZON MARCELO ADRIAN")
        cuil = st.text_input("CUIL", "20-16169317-1")
        clave_fiscal = st.text_input("Clave Fiscal", type="password")
        clave_ss = st.text_input("Clave de la Seguridad Social", type="password")
        fecha_nac = st.date_input("Fecha de Nacimiento", value=date(1962, 2, 1))
        
        submitted = st.form_submit_button("Guardar Datos")
        if submitted:
            st.success(f"¡Datos de {nombre} actualizados para la sesión!")

# ==========================================
# 2. HISTORIAL DE APORTES (Empresas y Períodos)
# ==========================================
elif menu == "2. Historial de Aportes":
    st.header("📋 Historial de Aportes")
    st.markdown("**Cliente:** CABEZON MARCELO ADRIAN | **CUIL:** 20-16169317-1")
    
    # Métricas rápidas para ver en el celu
    c1, c2 = st.columns(2)
    with c1:
        st.metric(label="Años Computables", value="28 Años y 5 Meses")
    with c2:
        st.metric(label="Empleadores", value="6 Empresas")
        
    st.markdown("### 🏢 Detalle de Empleadores")
    
    # Tabla clara para consultar en la calle
    empresas_data = [
        {"Empresa": "AGRO INDUSTRIAS INCA S A", "Desde": "07/1994", "Hasta": "11/1999"},
        {"Empresa": "LA COLINA S A", "Desde": "11/1999", "Hasta": "06/2004"},
        {"Empresa": "AGRO INDUSTRIAS EL NIHUIL SA", "Desde": "05/2008", "Hasta": "03/2025"},
        {"Empresa": "ALIMENTOS PREMIUN S A", "Desde": "05/2008", "Hasta": "08/2020"},
        {"Empresa": "DIELO S A", "Desde": "03/2009", "Hasta": "09/2026"},
        {"Empresa": "SANTIAGO SAENZ S A", "Desde": "08/2016", "Hasta": "09/2026"}
    ]
    
    st.dataframe(empresas_data, use_container_width=True)
    st.info("💡 **Pluriempleo detectado:** Tramos con superposición de aportes entre 2008 y 2026.")

# ==========================================
# 3. CÁLCULO DE DERECHO Y HABER
# ==========================================
elif menu == "3. Cálculo de Derecho y Haber":
    st.header("⚖️ Estado de Derecho y Haber")
    
    st.success("🟢 **DERECHO CUMPLIDO:** El cliente supera los requisitos de edad y aportes exigidos por el SIPA.")
    
    st.markdown("### Resumen Financiero Estimado")
    st.metric(label="Haber Mensual Estimado", value="$ 1.803.258,37")
    
    st.markdown("---")
    if st.button("📤 Enviar Reporte por WhatsApp"):
        st.info("Generando enlace directo para compartir con el cliente...")
  
