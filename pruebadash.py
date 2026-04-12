import streamlit as st
import pandas as pd
import numpy as np
import hashlib
import os
import altair as alt

# =========================================================
# CONFIG GENERAL
# =========================================================
st.set_page_config(
    page_title="SmartLogistics | Forecast Dashboard",
    page_icon="📈",
    layout="wide"
)

# =========================================================
# LOGIN
# =========================================================
ALLOWED_EMAIL = "peyaridergt@pedidosya.com"
PASSWORD_HASH = hashlib.sha256("Peya123!".encode()).hexdigest()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    st.markdown(
        """
        <div class="login-wrap">
            <div class="login-box">
                <div class="login-badge">🚀 Forecasting • IA • Data Intelligence</div>
                <h1>Smart Logistics</h1>
                <p class="login-subtitle">
                    Predicción inteligente de órdenes y análisis de precisión 
                    para impulsar decisiones operativas basadas en datos.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    c1, c2, c3 = st.columns([1, 1.1, 1])
    with c2:
        st.markdown("### Iniciar sesión")
        email = st.text_input("Correo")
        password = st.text_input("Password", type="password")

        if st.button("Ingresar", use_container_width=True):
            if email.strip().lower() != ALLOWED_EMAIL:
                st.error("No tienes acceso a este dashboard.")
                st.markdown("</div>", unsafe_allow_html=True)
                return

            if hash_password(password) != PASSWORD_HASH:
                st.error("Password incorrecta.")
                st.markdown("</div>", unsafe_allow_html=True)
                return

            st.session_state["logged_in"] = True
            st.session_state["user"] = email.strip().lower()
            st.session_state["page"] = "home"
            st.rerun()

        st.markdown(
            """
            <div class="hint-box">
                <b>Credenciales de prueba</b><br>
                Correo: peyaridergt@pedidosya.com<br>
                Password: Peya123!
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

def logout():
    st.session_state["logged_in"] = False
    st.session_state["user"] = None
    st.session_state["page"] = "home"
    st.rerun()

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "user" not in st.session_state:
    st.session_state["user"] = None

if "page" not in st.session_state:
    st.session_state["page"] = "home"

if not st.session_state["logged_in"]:
    # =========================================================
    # ESTILO
    # =========================================================
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(180deg, #f8f9fc 0%, #eef2ff 100%);
        }

        .login-wrap {
            padding-top: 30px;
            padding-bottom: 10px;
            text-align: center;
        }

        .login-box h1 {
            font-size: 3rem;
            margin-bottom: 0.25rem;
            color: #111827;
        }

        .login-subtitle {
            color: #6b7280;
            font-size: 1rem;
            margin-bottom: 0.5rem;
        }

        .login-badge {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 999px;
            background: linear-gradient(90deg, #111827, #374151);
            color: white;
            font-size: 0.85rem;
            margin-bottom: 14px;
        }

        .panel {
            background: rgba(255,255,255,0.85);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.7);
            border-radius: 22px;
            padding: 24px;
            box-shadow: 0 12px 35px rgba(17,24,39,0.08);
        }

        .hint-box {
            margin-top: 14px;
            padding: 12px;
            border-radius: 14px;
            background: #f3f4f6;
            color: #374151;
            font-size: 0.9rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    login()
    st.stop()

# ESTILO GENERAL
# =========================================================
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;800&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet">

    <style>
    /* =========================
       FUENTES
    ========================= */
    html, body, p, label, input, textarea, .stApp, .stMarkdown, .stText {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 400;
    }

    h1, h2, h3, h4, h5, h6,
    .hero h1,
    .section-title,
    .module-card h4,
    .login-box h1,
    .login-subtitle,
    div[data-testid="stMetricLabel"],
    div[data-testid="stMetricValue"] {
        font-family: 'Outfit', sans-serif !important;
    }

    /* Mantener íconos del sistema sanos */
    .material-icons {
        font-family: 'Material Icons' !important;
        font-weight: normal !important;
        font-style: normal !important;
        font-size: 24px !important;
        line-height: 1 !important;
        letter-spacing: normal !important;
        text-transform: none !important;
        display: inline-block !important;
        white-space: nowrap !important;
        direction: ltr !important;
        -webkit-font-smoothing: antialiased !important;
    }

    .material-symbols-outlined {
        font-family: 'Material Symbols Outlined' !important;
        font-weight: normal !important;
        font-style: normal !important;
        font-size: 20px !important;
        line-height: 1 !important;
        letter-spacing: normal !important;
        text-transform: none !important;
        display: inline-block !important;
        white-space: nowrap !important;
        direction: ltr !important;
        -webkit-font-smoothing: antialiased !important;
    }

    /* No romper el botón nativo del sidebar */
    button[kind="header"] {
        background: transparent !important;
        color: inherit !important;
        border: none !important;
        box-shadow: none !important;
        font-family: inherit !important;
        transform: none !important;
    }

    [data-testid="collapsedControl"] * {
        font-family: 'Material Symbols Outlined', 'Material Icons' !important;
    }

    /* =========================
       LAYOUT GENERAL
    ========================= */
    .stApp {
        background: #f7f8fc;
    }

    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }

    .panel {
        background: #FFFFFF;
        border-radius: 22px;
        padding: 20px;
        box-shadow: 0 8px 28px rgba(17,24,39,0.06);
        border: 1px solid #eef2f7;
    }

    /* =========================
       HERO / HEADER
    ========================= */
    .hero {
        position: relative;
        background: linear-gradient(135deg, rgba(250, 0, 80, 0.88) 0%, rgba(255, 45, 111, 0.82) 100%);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        padding: 30px 34px;
        border-radius: 28px;
        color: #FFFFFF;
        border: 1px solid rgba(255, 255, 255, 0.18);
        box-shadow: 
            0 18px 45px rgba(250, 0, 80, 0.24),
            inset 0 1px 0 rgba(255, 255, 255, 0.18);
        margin-bottom: 22px;
        overflow: hidden;
    }

    .hero::before {
        content: "";
        position: absolute;
        top: -40px;
        right: -60px;
        width: 240px;
        height: 240px;
        background: radial-gradient(circle, rgba(255,255,255,0.22) 0%, rgba(255,255,255,0.00) 70%);
        pointer-events: none;
    }

    .hero::after {
        content: "";
        position: absolute;
        bottom: -30px;
        left: 40px;
        width: 180px;
        height: 180px;
        background: radial-gradient(circle, rgba(255,255,255,0.10) 0%, rgba(255,255,255,0.00) 72%);
        pointer-events: none;
    }

    .hero-container {
        position: relative;
        z-index: 2;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 24px;
    }

    .hero-text {
        max-width: 68%;
    }

    .hero h1 {
        margin: 0;
        font-size: 2.5rem;
        color: #FFFFFF;
        font-weight: 800;
        line-height: 1.05;
    }

    .hero p {
        margin-top: 12px;
        margin-bottom: 0;
        color: rgba(255,255,255,0.96);
        font-weight: 700;
        font-size: 1.05rem;
        line-height: 1.4;
        max-width: 760px;
    }

    .hero-logo img {
        height: 74px;
        object-fit: contain;
        opacity: 0.98;
        filter: drop-shadow(0 6px 16px rgba(0,0,0,0.12));
    }    
    
    /* =========================
       HOME / CARDS
    ========================= */
    .module-card {
        background: #FFFFFF;
        border-radius: 22px;
        padding: 22px;
        border: 1px solid #EDEDED;
        box-shadow: 0 10px 28px rgba(17,24,39,0.05);
        min-height: 160px;
    }

    .module-card h4 {
        margin-top: 0;
        margin-bottom: 10px;
        color: #000000;
        font-size: 1.15rem;
        font-weight: 700;
    }

    .module-card p {
        color: #4B5563;
        font-size: 0.95rem;
        line-height: 1.5;
        font-weight: 400;
    }

    .mini-tag {
        display: inline-block;
        padding: 6px 10px;
        border-radius: 999px;
        background: #EDEDED;
        color: #000000;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .section-title {
        font-size: 1.15rem;
        font-weight: 800;
        color: #111827;
        margin-bottom: 0.5rem;
    }

    .subtle {
        color: #6b7280;
        font-size: 0.92rem;
    }

    /* =========================
       MÉTRICAS
    ========================= */
    div[data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #edf0f6;
        border-radius: 20px;
        padding: 14px 16px;
        box-shadow: 0 8px 24px rgba(17,24,39,0.05);
    }

    div[data-testid="stMetricLabel"] {
        color: #6b7280;
        font-weight: 700;
    }

    div[data-testid="stMetricValue"] {
        color: #111827;
        font-weight: 800;
    }

    /* =========================
       TABS
    ========================= */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        background: #EDEDED;
        border-radius: 14px;
        padding: 10px 18px;
        border: 1px solid #E0E0E0;
        transition: all 0.25s ease;
        color: #000000 !important;
        font-weight: 700 !important;
        font-family: 'Outfit', sans-serif !important;
    }

    .stTabs [data-baseweb="tab"]:hover {
        background: #FA0050;
        color: #FFFFFF !important;
        border: 1px solid #FA0050;
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(250,0,80,0.20);
    }

    .stTabs [aria-selected="true"] {
        background: #FA0050 !important;
        color: #FFFFFF !important;
        border: 1px solid #FA0050 !important;
    }

    .stTabs [data-baseweb="tab-highlight"] {
        background: transparent !important;
    }

    /* =========================
       BOTONES
    ========================= */
    div.stButton > button {
        height: 48px;
        border-radius: 14px;
        font-weight: 700 !important;
        font-family: 'Outfit', sans-serif !important;
        transition: all 0.25s ease;
        border: 1px solid #000000 !important;
        background: #000000 !important;
        color: #FFFFFF !important;
        white-space: nowrap;
    }

    div.stButton > button:hover {
        background: #FA0050 !important;
        color: #FFFFFF !important;
        border: 1px solid #FA0050 !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(250,0,80,0.25);
    }

    div.stButton > button:active {
        transform: scale(0.98);
    }

    /* Botones deshabilitados */
    div.stButton > button:disabled {
        background: #000000 !important;
        color: #FFFFFF !important;
        border: 1px solid #000000 !important;
        opacity: 0.65;
        cursor: not-allowed;
    }

    /* =========================
       LOGIN
    ========================= */
    .login-wrap {
        padding-top: 30px;
        padding-bottom: 10px;
        text-align: center;
    }

    .login-box h1 {
        font-size: 3rem;
        margin-bottom: 0.25rem;
        color: #111827;
        font-weight: 800;
    }

    .login-subtitle {
        color: #6b7280;
        font-size: 1rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }

    .login-badge {
        display: inline-block;
        padding: 8px 14px;
        border-radius: 999px;
        background: #FA0050;
        color: #FFFFFF;
        font-size: 0.85rem;
        margin-bottom: 14px;
        font-weight: 700;
    }

    .hint-box {
        margin-top: 14px;
        padding: 12px;
        border-radius: 14px;
        background: #f3f4f6;
        color: #374151;
        font-size: 0.9rem;
    }

    .top-actions {
        margin-top: 10px;
    }

    /* =========================
       SIDEBAR GENERAL
    ========================= */
    section[data-testid="stSidebar"] {
        background: #F7F8FC !important;
        border-right: 1px solid #EDEDED;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.2rem;
        padding-bottom: 1rem;
    }

    /* Título principal del sidebar */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4 {
        color: #111827 !important;
        font-weight: 800 !important;
        font-family: 'Outfit', sans-serif !important;
    }

    /* Labels */
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] .stMarkdown,
    section[data-testid="stSidebar"] p {
        color: #111827 !important;
        font-weight: 700 !important;
        font-family: 'Outfit', sans-serif !important;
    }

    /* =========================
       INPUTS / SELECTS / DATE
    ========================= */
    section[data-testid="stSidebar"] div[data-baseweb="input"] > div,
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div,
    section[data-testid="stSidebar"] div[data-baseweb="base-input"] {
        background: #FFFFFF !important;
        border: 1px solid #E5E7EB !important;
        border-radius: 16px !important;
        box-shadow: none !important;
    }

    section[data-testid="stSidebar"] div[data-baseweb="input"] > div:hover,
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover,
    section[data-testid="stSidebar"] div[data-baseweb="base-input"]:hover {
        border: 1px solid #FA0050 !important;
    }

    section[data-testid="stSidebar"] div[data-baseweb="input"] > div:focus-within,
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div:focus-within,
    section[data-testid="stSidebar"] div[data-baseweb="base-input"]:focus-within {
        border: 1px solid #FA0050 !important;
        box-shadow: 0 0 0 3px rgba(250, 0, 80, 0.12) !important;
    }

    /* Texto interno */
    section[data-testid="stSidebar"] input,
    section[data-testid="stSidebar"] .stDateInput input,
    section[data-testid="stSidebar"] .stMultiSelect div,
    section[data-testid="stSidebar"] .stSelectbox div {
        color: #111827 !important;
        font-family: 'Outfit', sans-serif !important;
    }

    /* =========================
       TAGS DEL MULTISELECT
    ========================= */
    section[data-testid="stSidebar"] span[data-baseweb="tag"] {
        background: #FA0050 !important;
        color: #FFFFFF !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: 700 !important;
        font-family: 'Outfit', sans-serif !important;
    }

    section[data-testid="stSidebar"] span[data-baseweb="tag"] * {
        color: #FFFFFF !important;
    }

    /* Botón de cerrar tag */
    section[data-testid="stSidebar"] span[data-baseweb="tag"] svg {
        fill: #FFFFFF !important;
    }

    /* =========================
       DROPDOWN MENU
    ========================= */
    div[role="listbox"] {
        background: #FFFFFF !important;
        border: 1px solid #E5E7EB !important;
        border-radius: 14px !important;
        box-shadow: 0 12px 28px rgba(17,24,39,0.10) !important;
    }

    div[role="option"] {
        color: #111827 !important;
        font-family: 'Outfit', sans-serif !important;
    }

    div[role="option"]:hover {
        background: rgba(250, 0, 80, 0.08) !important;
    }

    /* =========================
       SEPARADOR ACCIONES
    ========================= */
    section[data-testid="stSidebar"] hr {
        border: none !important;
        border-top: 1px solid #E5E7EB !important;
        margin-top: 1rem !important;
        margin-bottom: 1rem !important;
    }

    /* =========================
       BOTONES DEL SIDEBAR
    ========================= */
    section[data-testid="stSidebar"] div.stButton > button {
        background: #000000 !important;
        border: 1px solid #000000 !important;
        border-radius: 16px !important;
        font-weight: 700 !important;
        font-family: 'Outfit', sans-serif !important;
        height: 48px !important;
        transition: all 0.25s ease !important;
    }

    /* 🔥 FORZAR TODO EL TEXTO INTERNO */
    section[data-testid="stSidebar"] div.stButton > button,
    section[data-testid="stSidebar"] div.stButton > button * {
        color: #FFFFFF !important;
    }

    /* Hover */
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background: #FA0050 !important;
        border: 1px solid #FA0050 !important;
    }

    /* Hover texto */
    section[data-testid="stSidebar"] div.stButton > button:hover * {
        color: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] div.stButton > button:hover {
        background: #FA0050 !important;
        color: #FFFFFF !important;
        border: 1px solid #FA0050 !important;
        box-shadow: 0 8px 18px rgba(250,0,80,0.20) !important;
        transform: translateY(-1px);
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# CARGA DE DATOS
# =========================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEST_FILE = os.path.join(BASE_DIR, "forecast_ordenes_total_dia_test.csv")
FORECAST_FILE = os.path.join(BASE_DIR, "forecast_ordenes_total_dia_future.csv")
CITY_TEST_FILE = os.path.join(BASE_DIR, "forecast_share_ciudad_desde_pais_test.csv")
CITY_FORECAST_FILE = os.path.join(BASE_DIR, "forecast_share_ciudad_desde_pais_future.csv")
VERTICAL_TEST_FILE = os.path.join(BASE_DIR, "forecast_share_vertical_desde_pais_test.csv")
VERTICAL_FUTURE_FILE = os.path.join(BASE_DIR, "forecast_share_vertical_desde_pais_future.csv")
FAIL_RATE_TEST_FILE = os.path.join(BASE_DIR, "forecast_cancelled_amarrado_total_pais_test.csv")
FAIL_RATE_FUTURE_FILE = os.path.join(BASE_DIR, "forecast_cancelled_amarrado_total_pais_future.csv")
NON_SEAMLESS_TEST_FILE = os.path.join(BASE_DIR, "forecast_non_seamless_amarrado_total_pais_test.csv")
NON_SEAMLESS_FUTURE_FILE = os.path.join(BASE_DIR, "forecast_non_seamless_amarrado_total_pais_future.csv")

@st.cache_data
def load_data():
    test_df = pd.read_csv(TEST_FILE)
    future_df = pd.read_csv(FORECAST_FILE)

    # Filtrar solo el forecast que queremos
    if "job_name" in test_df.columns and "target" in test_df.columns:
        test_df = test_df[
            (test_df["job_name"] == "forecast_ordenes_total_dia") &
            (test_df["target"] == "ordenes")
        ].copy()

    if "job_name" in future_df.columns and "target" in future_df.columns:
        future_df = future_df[
            (future_df["job_name"] == "forecast_ordenes_total_dia") &
            (future_df["target"] == "ordenes")
        ].copy()

    # Fechas
    test_df["date"] = pd.to_datetime(test_df["date"], errors="coerce")
    future_df["date"] = pd.to_datetime(future_df["date"], errors="coerce")

    # Columnas de modelos
    model_cols = [
        "Orbit + XGBoost",
        "Prophet + XGBoost",
        "Holt-Winters + XGBoost",
        "RF + ETS + LightGBM",
        "Ensamble Automático"
    ]

    # Crear columnas faltantes por si acaso
    for col in model_cols:
        if col not in test_df.columns:
            test_df[col] = np.nan
        if col not in future_df.columns:
            future_df[col] = np.nan

    if "actual" not in test_df.columns:
        test_df["actual"] = np.nan

    if "actual" not in future_df.columns:
        future_df["actual"] = np.nan

    if "day_name" not in test_df.columns:
        test_df["day_name"] = test_df["date"].dt.day_name()

    if "day_name" not in future_df.columns:
        future_df["day_name"] = future_df["date"].dt.day_name()

    if "is_holiday" not in test_df.columns:
        test_df["is_holiday"] = 0

    if "is_holiday" not in future_df.columns:
        future_df["is_holiday"] = 0

    if "is_payday" not in test_df.columns:
        test_df["is_payday"] = 0

    if "is_payday" not in future_df.columns:
        future_df["is_payday"] = 0

    # Convertir numéricos
    test_df["actual"] = pd.to_numeric(test_df["actual"], errors="coerce")
    future_df["actual"] = pd.to_numeric(future_df["actual"], errors="coerce")

    test_df["is_holiday"] = pd.to_numeric(test_df["is_holiday"], errors="coerce").fillna(0).astype(int)
    future_df["is_holiday"] = pd.to_numeric(future_df["is_holiday"], errors="coerce").fillna(0).astype(int)

    test_df["is_payday"] = pd.to_numeric(test_df["is_payday"], errors="coerce").fillna(0).astype(int)
    future_df["is_payday"] = pd.to_numeric(future_df["is_payday"], errors="coerce").fillna(0).astype(int)

    for col in model_cols:
        test_df[col] = pd.to_numeric(test_df[col], errors="coerce")
        future_df[col] = pd.to_numeric(future_df[col], errors="coerce")

    # Quitar filas sin fecha
    test_df = test_df.dropna(subset=["date"]).copy()
    future_df = future_df.dropna(subset=["date"]).copy()

    # Orden de días
    day_order = [
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"
    ]

    # =========================
    # MÉTRICAS DE TESTING
    # =========================
    for col in model_cols:
        test_df[f"AE__{col}"] = (test_df["actual"] - test_df[col]).abs()
        test_df[f"APE__{col}"] = np.where(
            test_df["actual"].notna() & (test_df["actual"] != 0),
            (test_df[f"AE__{col}"] / test_df["actual"]) * 100,
            np.nan
        )

    ape_cols = [f"APE__{col}" for col in model_cols]

    if len(test_df) > 0:
        test_df["best_model"] = test_df[ape_cols].idxmin(axis=1).str.replace("APE__", "", regex=False)
        test_df["best_mape"] = test_df[ape_cols].min(axis=1)
    else:
        test_df["best_model"] = np.nan
        test_df["best_mape"] = np.nan

    # =========================
    # RECOMENDACIÓN POR DÍA
    # =========================
    weekday_perf_rows = []

    for day in day_order:
        day_slice = test_df[test_df["day_name"] == day].copy()
        if day_slice.empty:
            continue

        row = {"day_name": day}
        for col in model_cols:
            row[col] = day_slice[f"APE__{col}"].mean()
        weekday_perf_rows.append(row)

    weekday_perf = pd.DataFrame(weekday_perf_rows)

    if not weekday_perf.empty:
        weekday_perf["recommended_model"] = weekday_perf[model_cols].idxmin(axis=1)
        weekday_perf["recommended_mape"] = weekday_perf[model_cols].min(axis=1)

        test_df = test_df.merge(
        weekday_perf[["day_name", "recommended_model", "recommended_mape"]],
        on="day_name",
        how="left"
    )

        future_df = future_df.merge(
            weekday_perf[["day_name", "recommended_model", "recommended_mape"]],
            on="day_name",
            how="left"
        )

        def pick_recommended_prediction(row):
            model = row.get("recommended_model", np.nan)
            if pd.isna(model):
                return np.nan
            if model not in row.index:
                return np.nan
            return row[model]

        future_df["recommended_prediction"] = future_df.apply(
            pick_recommended_prediction,
            axis=1
        )

        future_df["difference_vs_ensemble"] = (
            future_df["recommended_prediction"] - future_df["Ensamble Automático"]
        )
    else:
        weekday_perf = pd.DataFrame(columns=(
            ["day_name"] + model_cols + ["recommended_model", "recommended_mape"]
        ))
        future_df["recommended_model"] = np.nan
        future_df["recommended_mape"] = np.nan
        future_df["recommended_prediction"] = np.nan
        future_df["difference_vs_ensemble"] = np.nan

    return test_df, future_df, model_cols, weekday_perf, day_order

@st.cache_data
def load_city_data():
    city_test_df = pd.read_csv(CITY_TEST_FILE)
    city_future_df = pd.read_csv(CITY_FORECAST_FILE)

    city_test_df["date"] = pd.to_datetime(city_test_df["date"], errors="coerce")
    city_future_df["date"] = pd.to_datetime(city_future_df["date"], errors="coerce")

    city_test_df = city_test_df.dropna(subset=["date"]).copy()
    city_future_df = city_future_df.dropna(subset=["date"]).copy()

    # Asegurar columnas mínimas
    required_test_cols = [
        "date", "city_name", "ordenes_ciudad_actual", "ordenes_ciudad_forecast",
        "share_ciudad", "ordenes_pais_actual", "ordenes_pais_forecast"
    ]
    required_future_cols = [
        "date", "city_name", "ordenes_ciudad_forecast",
        "share_ciudad", "ordenes_pais_forecast"
    ]

    for col in required_test_cols:
        if col not in city_test_df.columns:
            city_test_df[col] = np.nan

    for col in required_future_cols:
        if col not in city_future_df.columns:
            city_future_df[col] = np.nan

    # Tipos numéricos
    numeric_test_cols = [
        "ordenes_pais_actual",
        "ordenes_pais_forecast",
        "share_ciudad",
        "ordenes_ciudad_actual",
        "ordenes_ciudad_forecast"
    ]

    numeric_future_cols = [
        "ordenes_pais_forecast",
        "share_ciudad",
        "ordenes_ciudad_forecast"
    ]

    for col in numeric_test_cols:
        city_test_df[col] = pd.to_numeric(city_test_df[col], errors="coerce")

    for col in numeric_future_cols:
        city_future_df[col] = pd.to_numeric(city_future_df[col], errors="coerce")

    # Completar columnas auxiliares
    city_test_df["day_name"] = city_test_df["date"].dt.day_name()
    city_future_df["day_name"] = city_future_df["date"].dt.day_name()

    if "is_holiday" not in city_test_df.columns:
        city_test_df["is_holiday"] = 0
    if "is_holiday" not in city_future_df.columns:
        city_future_df["is_holiday"] = 0

    if "is_payday" not in city_test_df.columns:
        city_test_df["is_payday"] = 0
    if "is_payday" not in city_future_df.columns:
        city_future_df["is_payday"] = 0

    city_test_df["is_holiday"] = pd.to_numeric(city_test_df["is_holiday"], errors="coerce").fillna(0).astype(int)
    city_future_df["is_holiday"] = pd.to_numeric(city_future_df["is_holiday"], errors="coerce").fillna(0).astype(int)

    city_test_df["is_payday"] = pd.to_numeric(city_test_df["is_payday"], errors="coerce").fillna(0).astype(int)
    city_future_df["is_payday"] = pd.to_numeric(city_future_df["is_payday"], errors="coerce").fillna(0).astype(int)

    # Error de forecast en testing
    city_test_df["AE__forecast_ciudad"] = (
        city_test_df["ordenes_ciudad_actual"] - city_test_df["ordenes_ciudad_forecast"]
    ).abs()

    city_test_df["APE__forecast_ciudad"] = np.where(
        city_test_df["ordenes_ciudad_actual"].notna() & (city_test_df["ordenes_ciudad_actual"] != 0),
        (city_test_df["AE__forecast_ciudad"] / city_test_df["ordenes_ciudad_actual"]) * 100,
        np.nan
    )

    return city_test_df, city_future_df

@st.cache_data
def load_vertical_data():
    vertical_test_df = pd.read_csv(VERTICAL_TEST_FILE)
    vertical_future_df = pd.read_csv(VERTICAL_FUTURE_FILE)

    vertical_test_df["date"] = pd.to_datetime(vertical_test_df["date"], errors="coerce")
    vertical_future_df["date"] = pd.to_datetime(vertical_future_df["date"], errors="coerce")

    vertical_test_df = vertical_test_df.dropna(subset=["date"]).copy()
    vertical_future_df = vertical_future_df.dropna(subset=["date"]).copy()

    # Asegurar columnas mínimas
    required_test_cols = [
        "date", "vertical", "ordenes_vertical_actual", "ordenes_vertical_forecast",
        "share_vertical", "ordenes_pais_actual", "ordenes_pais_forecast"
    ]
    required_future_cols = [
        "date", "vertical", "ordenes_vertical_forecast",
        "share_vertical", "ordenes_pais_forecast"
    ]

    for col in required_test_cols:
        if col not in vertical_test_df.columns:
            vertical_test_df[col] = np.nan

    for col in required_future_cols:
        if col not in vertical_future_df.columns:
            vertical_future_df[col] = np.nan

    # Tipos numéricos
    numeric_test_cols = [
        "ordenes_pais_actual",
        "ordenes_pais_forecast",
        "share_vertical",
        "ordenes_vertical_actual",
        "ordenes_vertical_forecast"
    ]

    numeric_future_cols = [
        "ordenes_pais_forecast",
        "share_vertical",
        "ordenes_vertical_forecast"
    ]

    for col in numeric_test_cols:
        vertical_test_df[col] = pd.to_numeric(vertical_test_df[col], errors="coerce")

    for col in numeric_future_cols:
        vertical_future_df[col] = pd.to_numeric(vertical_future_df[col], errors="coerce")

    # Columnas auxiliares
    vertical_test_df["day_name"] = vertical_test_df["date"].dt.day_name()
    vertical_future_df["day_name"] = vertical_future_df["date"].dt.day_name()

    if "is_holiday" not in vertical_test_df.columns:
        vertical_test_df["is_holiday"] = 0
    if "is_holiday" not in vertical_future_df.columns:
        vertical_future_df["is_holiday"] = 0

    if "is_payday" not in vertical_test_df.columns:
        vertical_test_df["is_payday"] = 0
    if "is_payday" not in vertical_future_df.columns:
        vertical_future_df["is_payday"] = 0

    vertical_test_df["is_holiday"] = pd.to_numeric(vertical_test_df["is_holiday"], errors="coerce").fillna(0).astype(int)
    vertical_future_df["is_holiday"] = pd.to_numeric(vertical_future_df["is_holiday"], errors="coerce").fillna(0).astype(int)

    vertical_test_df["is_payday"] = pd.to_numeric(vertical_test_df["is_payday"], errors="coerce").fillna(0).astype(int)
    vertical_future_df["is_payday"] = pd.to_numeric(vertical_future_df["is_payday"], errors="coerce").fillna(0).astype(int)

    # Error de forecast en testing
    vertical_test_df["AE__forecast_vertical"] = (
        vertical_test_df["ordenes_vertical_actual"] - vertical_test_df["ordenes_vertical_forecast"]
    ).abs()

    vertical_test_df["APE__forecast_vertical"] = np.where(
        vertical_test_df["ordenes_vertical_actual"].notna() & (vertical_test_df["ordenes_vertical_actual"] != 0),
        (vertical_test_df["AE__forecast_vertical"] / vertical_test_df["ordenes_vertical_actual"]) * 100,
        np.nan
    )

    return vertical_test_df, vertical_future_df

@st.cache_data
def load_fail_rate_data():
    fail_test_df = pd.read_csv(FAIL_RATE_TEST_FILE)
    fail_future_df = pd.read_csv(FAIL_RATE_FUTURE_FILE)

    fail_test_df["date"] = pd.to_datetime(fail_test_df["date"], errors="coerce")
    fail_future_df["date"] = pd.to_datetime(fail_future_df["date"], errors="coerce")

    fail_test_df = fail_test_df.dropna(subset=["date"]).copy()
    fail_future_df = fail_future_df.dropna(subset=["date"]).copy()

    required_test_cols = [
        "date", "ordenes_pais_actual", "ordenes_pais_forecast", "city_name", "vertical",
        "share_city_vertical", "cancel_rate", "total_orders_segment_actual",
        "total_orders_segment_forecast", "cancelled_orders_forecast",
        "cancelled_orders_actual_estimado", "job_name"
    ]

    required_future_cols = [
        "date", "ordenes_pais_forecast", "city_name", "vertical",
        "share_city_vertical", "cancel_rate", "total_orders_segment_forecast",
        "cancelled_orders_forecast", "job_name"
    ]

    for col in required_test_cols:
        if col not in fail_test_df.columns:
            fail_test_df[col] = np.nan

    for col in required_future_cols:
        if col not in fail_future_df.columns:
            fail_future_df[col] = np.nan

    numeric_test_cols = [
        "ordenes_pais_actual",
        "ordenes_pais_forecast",
        "share_city_vertical",
        "cancel_rate",
        "total_orders_segment_actual",
        "total_orders_segment_forecast",
        "cancelled_orders_forecast",
        "cancelled_orders_actual_estimado"
    ]

    numeric_future_cols = [
        "ordenes_pais_forecast",
        "share_city_vertical",
        "cancel_rate",
        "total_orders_segment_forecast",
        "cancelled_orders_forecast"
    ]

    for col in numeric_test_cols:
        fail_test_df[col] = pd.to_numeric(fail_test_df[col], errors="coerce")

    for col in numeric_future_cols:
        fail_future_df[col] = pd.to_numeric(fail_future_df[col], errors="coerce")

    fail_test_df["city_name"] = fail_test_df["city_name"].astype(str).str.strip()
    fail_future_df["city_name"] = fail_future_df["city_name"].astype(str).str.strip()

    fail_test_df["vertical"] = fail_test_df["vertical"].astype(str).str.strip()
    fail_future_df["vertical"] = fail_future_df["vertical"].astype(str).str.strip()

    fail_test_df["day_name"] = fail_test_df["date"].dt.day_name()
    fail_future_df["day_name"] = fail_future_df["date"].dt.day_name()

    if "is_holiday" not in fail_test_df.columns:
        fail_test_df["is_holiday"] = 0
    if "is_holiday" not in fail_future_df.columns:
        fail_future_df["is_holiday"] = 0

    if "is_payday" not in fail_test_df.columns:
        fail_test_df["is_payday"] = 0
    if "is_payday" not in fail_future_df.columns:
        fail_future_df["is_payday"] = 0

    fail_test_df["is_holiday"] = pd.to_numeric(fail_test_df["is_holiday"], errors="coerce").fillna(0).astype(int)
    fail_future_df["is_holiday"] = pd.to_numeric(fail_future_df["is_holiday"], errors="coerce").fillna(0).astype(int)

    fail_test_df["is_payday"] = pd.to_numeric(fail_test_df["is_payday"], errors="coerce").fillna(0).astype(int)
    fail_future_df["is_payday"] = pd.to_numeric(fail_future_df["is_payday"], errors="coerce").fillna(0).astype(int)

    # Fail Rate real/estimado en testing
    fail_test_df["fail_rate_actual_pct"] = np.where(
        fail_test_df["total_orders_segment_actual"].notna() & (fail_test_df["total_orders_segment_actual"] != 0),
        (fail_test_df["cancelled_orders_actual_estimado"] / fail_test_df["total_orders_segment_actual"]) * 100,
        np.nan
    )

    fail_test_df["fail_rate_forecast_pct"] = np.where(
        fail_test_df["total_orders_segment_forecast"].notna() & (fail_test_df["total_orders_segment_forecast"] != 0),
        (fail_test_df["cancelled_orders_forecast"] / fail_test_df["total_orders_segment_forecast"]) * 100,
        np.nan
    )

    fail_future_df["fail_rate_forecast_pct"] = np.where(
        fail_future_df["total_orders_segment_forecast"].notna() & (fail_future_df["total_orders_segment_forecast"] != 0),
        (fail_future_df["cancelled_orders_forecast"] / fail_future_df["total_orders_segment_forecast"]) * 100,
        np.nan
    )

    return fail_test_df, fail_future_df

@st.cache_data
def load_non_seamless_data():
    ns_test_df = pd.read_csv(NON_SEAMLESS_TEST_FILE)
    ns_future_df = pd.read_csv(NON_SEAMLESS_FUTURE_FILE)

    ns_test_df["date"] = pd.to_datetime(ns_test_df["date"], errors="coerce")
    ns_future_df["date"] = pd.to_datetime(ns_future_df["date"], errors="coerce")

    ns_test_df = ns_test_df.dropna(subset=["date"]).copy()
    ns_future_df = ns_future_df.dropna(subset=["date"]).copy()

    required_test_cols = [
        "date", "ordenes_pais_actual", "ordenes_pais_forecast", "city_name",
        "share_ciudad", "non_seamless_rate", "total_orders_city_actual",
        "total_orders_city_forecast", "non_seamless_orders_forecast",
        "non_seamless_orders_actual_estimado", "job_name"
    ]

    required_future_cols = [
        "date", "ordenes_pais_forecast", "city_name", "share_ciudad",
        "non_seamless_rate", "total_orders_city_forecast",
        "non_seamless_orders_forecast", "job_name"
    ]

    for col in required_test_cols:
        if col not in ns_test_df.columns:
            ns_test_df[col] = np.nan

    for col in required_future_cols:
        if col not in ns_future_df.columns:
            ns_future_df[col] = np.nan

    numeric_test_cols = [
        "ordenes_pais_actual",
        "ordenes_pais_forecast",
        "share_ciudad",
        "non_seamless_rate",
        "total_orders_city_actual",
        "total_orders_city_forecast",
        "non_seamless_orders_forecast",
        "non_seamless_orders_actual_estimado"
    ]

    numeric_future_cols = [
        "ordenes_pais_forecast",
        "share_ciudad",
        "non_seamless_rate",
        "total_orders_city_forecast",
        "non_seamless_orders_forecast"
    ]

    for col in numeric_test_cols:
        ns_test_df[col] = pd.to_numeric(ns_test_df[col], errors="coerce")

    for col in numeric_future_cols:
        ns_future_df[col] = pd.to_numeric(ns_future_df[col], errors="coerce")

    ns_test_df["city_name"] = ns_test_df["city_name"].astype(str).str.strip()
    ns_future_df["city_name"] = ns_future_df["city_name"].astype(str).str.strip()

    ns_test_df["day_name"] = ns_test_df["date"].dt.day_name()
    ns_future_df["day_name"] = ns_future_df["date"].dt.day_name()

    if "is_holiday" not in ns_test_df.columns:
        ns_test_df["is_holiday"] = 0
    if "is_holiday" not in ns_future_df.columns:
        ns_future_df["is_holiday"] = 0

    if "is_payday" not in ns_test_df.columns:
        ns_test_df["is_payday"] = 0
    if "is_payday" not in ns_future_df.columns:
        ns_future_df["is_payday"] = 0

    ns_test_df["is_holiday"] = pd.to_numeric(ns_test_df["is_holiday"], errors="coerce").fillna(0).astype(int)
    ns_future_df["is_holiday"] = pd.to_numeric(ns_future_df["is_holiday"], errors="coerce").fillna(0).astype(int)

    ns_test_df["is_payday"] = pd.to_numeric(ns_test_df["is_payday"], errors="coerce").fillna(0).astype(int)
    ns_future_df["is_payday"] = pd.to_numeric(ns_future_df["is_payday"], errors="coerce").fillna(0).astype(int)

    # Seamless % = del total, las que NO son non seamless
    ns_test_df["seamless_pct_actual"] = np.where(
        ns_test_df["total_orders_city_actual"].notna() & (ns_test_df["total_orders_city_actual"] != 0),
        ((ns_test_df["total_orders_city_actual"] - ns_test_df["non_seamless_orders_actual_estimado"]) / ns_test_df["total_orders_city_actual"]) * 100,
        np.nan
    )

    ns_test_df["seamless_pct_forecast"] = np.where(
        ns_test_df["total_orders_city_forecast"].notna() & (ns_test_df["total_orders_city_forecast"] != 0),
        ((ns_test_df["total_orders_city_forecast"] - ns_test_df["non_seamless_orders_forecast"]) / ns_test_df["total_orders_city_forecast"]) * 100,
        np.nan
    )

    ns_future_df["seamless_pct_forecast"] = np.where(
        ns_future_df["total_orders_city_forecast"].notna() & (ns_future_df["total_orders_city_forecast"] != 0),
        ((ns_future_df["total_orders_city_forecast"] - ns_future_df["non_seamless_orders_forecast"]) / ns_future_df["total_orders_city_forecast"]) * 100,
        np.nan
    )

    return ns_test_df, ns_future_df

# =========================
# CARGA DE DATOS (OBLIGATORIO)
# =========================
try:
    test_df, future_df, model_cols, weekday_perf, day_order = load_data()
except Exception as e:
    st.error(f"Error cargando datos: {e}")
    st.stop()
try:
    city_test_df, city_future_df = load_city_data()
except Exception as e:
    st.error(f"Error cargando forecast por ciudad: {e}")
    st.stop()
try:
    vertical_test_df, vertical_future_df = load_vertical_data()
except Exception as e:
    st.error(f"Error cargando forecast por vertical: {e}")
    st.stop()
try:
    fail_test_df, fail_future_df = load_fail_rate_data()
except Exception as e:
    st.error(f"Error cargando forecast fail rate: {e}")
    st.stop()
try:
    ns_test_df, ns_future_df = load_non_seamless_data()
except Exception as e:
    st.error(f"Error cargando forecast non seamless: {e}")
    st.stop()

# =========================================================
# FUNCIONES
# =========================================================
def go_to(page_name):
    st.session_state["page"] = page_name
    st.rerun()

import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def render_topbar(title, subtitle):
    logo_base64 = get_base64_image(
        r"C:\Users\nancy.valdes\Desktop\Dashboard RT y Forecast\Logotipo-Negativo-horizontal.png"
    )

    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-container">
                <div class="hero-text">
                    <h1>{title}</h1>
                    <p>{subtitle}</p>
                </div>
                <div class="hero-logo">
                    <img src="data:image/png;base64,{logo_base64}" />
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def build_combined_chart(test_filtered, future_filtered):
    frames = []

    if len(test_filtered):
        tmp_test = test_filtered[["date", "actual", "Ensamble Automático"]].copy()
        tmp_test["period"] = "Testing"
        tmp_test["series_name"] = "Actual"
        frames.append(
            tmp_test[["date", "period", "series_name", "actual"]].rename(columns={"actual": "value"})
        )

        tmp_test_ens = test_filtered[["date", "Ensamble Automático"]].copy()
        tmp_test_ens["period"] = "Testing"
        tmp_test_ens["series_name"] = "Forecast ensamble"
        frames.append(
            tmp_test_ens.rename(columns={"Ensamble Automático": "value"})
        )

    if len(future_filtered):
        tmp_future = future_filtered[["date", "Ensamble Automático"]].copy()
        tmp_future["period"] = "Forecast"
        tmp_future["series_name"] = "Forecast ensamble"
        frames.append(
            tmp_future.rename(columns={"Ensamble Automático": "value"})
        )

        if "recommended_prediction" in future_filtered.columns:
            tmp_future_rec = future_filtered[["date", "recommended_prediction"]].copy()
            tmp_future_rec["period"] = "Forecast"
            tmp_future_rec["series_name"] = "Forecast sugerido"
            frames.append(
                tmp_future_rec.rename(columns={"recommended_prediction": "value"})
            )

    if not frames:
        return None

    plot_df = pd.concat(frames, ignore_index=True)
    plot_df = plot_df.dropna(subset=["value"]).copy()

    # Padding para que no quede pegado arriba
    y_min = plot_df["value"].min()
    y_max = plot_df["value"].max()
    y_range = y_max - y_min

    if y_range == 0:
        y_range = y_max * 0.1 if y_max != 0 else 1000

    padded_min = max(0, y_min - y_range * 0.4)
    padded_max = y_max + y_range * 0.25

    # Colores PeYa
    color_scale = alt.Scale(
        domain=["Actual", "Forecast ensamble", "Forecast sugerido"],
        range=["#FA0050", "#00D9FC", "#FFE438"]
    )

    # Base chart
    base = alt.Chart(plot_df).encode(
        x=alt.X("date:T", title="Fecha"),
        y=alt.Y(
            "value:Q",
            title="Órdenes",
            scale=alt.Scale(domain=[padded_min, padded_max])
        ),
        color=alt.Color("series_name:N", title="Serie", scale=color_scale),
        tooltip=[
            alt.Tooltip("date:T", title="Fecha"),
            alt.Tooltip("series_name:N", title="Serie"),
            alt.Tooltip("period:N", title="Periodo"),
            alt.Tooltip("value:Q", title="Órdenes", format=",.0f")
        ]
    )

    # 🔥 TESTING → línea sólida
    line_testing = base.transform_filter(
        alt.datum.period == "Testing"
    ).mark_line(
        point=True,
        strokeWidth=3.2
    )

    # 🔥 FORECAST → línea punteada
    line_forecast = base.transform_filter(
        alt.datum.period == "Forecast"
    ).mark_line(
        point=True,
        strokeWidth=3.2,
        strokeDash=[6, 6]
    )

    chart = (line_testing + line_forecast).properties(height=430)

    return chart

def build_city_chart(city_test_filtered, city_future_filtered):
    frames = []

    if len(city_test_filtered):
        actual_daily = (
            city_test_filtered.groupby("date", as_index=False)["ordenes_ciudad_actual"]
            .sum()
            .rename(columns={"ordenes_ciudad_actual": "value"})
        )
        actual_daily["period"] = "Testing"
        actual_daily["series_name"] = "Actual"
        frames.append(actual_daily)

        forecast_test_daily = (
            city_test_filtered.groupby("date", as_index=False)["ordenes_ciudad_forecast"]
            .sum()
            .rename(columns={"ordenes_ciudad_forecast": "value"})
        )
        forecast_test_daily["period"] = "Testing"
        forecast_test_daily["series_name"] = "Forecast ciudad"
        frames.append(forecast_test_daily)

    if len(city_future_filtered):
        forecast_future_daily = (
            city_future_filtered.groupby("date", as_index=False)["ordenes_ciudad_forecast"]
            .sum()
            .rename(columns={"ordenes_ciudad_forecast": "value"})
        )
        forecast_future_daily["period"] = "Forecast"
        forecast_future_daily["series_name"] = "Forecast ciudad"
        frames.append(forecast_future_daily)

    if not frames:
        return None

    plot_df = pd.concat(frames, ignore_index=True)
    plot_df = plot_df.dropna(subset=["value"]).copy()

    y_min = plot_df["value"].min()
    y_max = plot_df["value"].max()
    y_range = y_max - y_min

    if y_range == 0:
        y_range = y_max * 0.1 if y_max != 0 else 1000

    padded_min = max(0, y_min - y_range * 0.4)
    padded_max = y_max + y_range * 0.25

    color_scale = alt.Scale(
        domain=["Actual", "Forecast ciudad"],
        range=["#FA0050", "#00D9FC"]
    )

    base = alt.Chart(plot_df).encode(
        x=alt.X("date:T", title="Fecha"),
        y=alt.Y(
            "value:Q",
            title="Órdenes ciudad",
            scale=alt.Scale(domain=[padded_min, padded_max])
        ),
        color=alt.Color("series_name:N", title="Serie", scale=color_scale),
        tooltip=[
            alt.Tooltip("date:T", title="Fecha"),
            alt.Tooltip("series_name:N", title="Serie"),
            alt.Tooltip("period:N", title="Periodo"),
            alt.Tooltip("value:Q", title="Órdenes", format=",.0f")
        ]
    )

    line_testing = base.transform_filter(
        alt.datum.period == "Testing"
    ).mark_line(
        point=True,
        strokeWidth=3.2
    )

    line_forecast = base.transform_filter(
        alt.datum.period == "Forecast"
    ).mark_line(
        point=True,
        strokeWidth=3.2,
        strokeDash=[6, 6]
    )

    return (line_testing + line_forecast).properties(height=430)

def build_vertical_chart(vertical_test_filtered, vertical_future_filtered):
    frames = []

    if len(vertical_test_filtered):
        actual_daily = (
            vertical_test_filtered.groupby("date", as_index=False)["ordenes_vertical_actual"]
            .sum()
            .rename(columns={"ordenes_vertical_actual": "value"})
        )
        actual_daily["period"] = "Testing"
        actual_daily["series_name"] = "Actual"
        frames.append(actual_daily)

        forecast_test_daily = (
            vertical_test_filtered.groupby("date", as_index=False)["ordenes_vertical_forecast"]
            .sum()
            .rename(columns={"ordenes_vertical_forecast": "value"})
        )
        forecast_test_daily["period"] = "Testing"
        forecast_test_daily["series_name"] = "Forecast vertical"
        frames.append(forecast_test_daily)

    if len(vertical_future_filtered):
        forecast_future_daily = (
            vertical_future_filtered.groupby("date", as_index=False)["ordenes_vertical_forecast"]
            .sum()
            .rename(columns={"ordenes_vertical_forecast": "value"})
        )
        forecast_future_daily["period"] = "Forecast"
        forecast_future_daily["series_name"] = "Forecast vertical"
        frames.append(forecast_future_daily)

    if not frames:
        return None

    plot_df = pd.concat(frames, ignore_index=True)
    plot_df = plot_df.dropna(subset=["value"]).copy()

    y_min = plot_df["value"].min()
    y_max = plot_df["value"].max()
    y_range = y_max - y_min

    if y_range == 0:
        y_range = y_max * 0.1 if y_max != 0 else 1000

    padded_min = max(0, y_min - y_range * 0.4)
    padded_max = y_max + y_range * 0.25

    color_scale = alt.Scale(
        domain=["Actual", "Forecast vertical"],
        range=["#FA0050", "#00D9FC"]
    )

    base = alt.Chart(plot_df).encode(
        x=alt.X("date:T", title="Fecha"),
        y=alt.Y(
            "value:Q",
            title="Órdenes vertical",
            scale=alt.Scale(domain=[padded_min, padded_max])
        ),
        color=alt.Color("series_name:N", title="Serie", scale=color_scale),
        tooltip=[
            alt.Tooltip("date:T", title="Fecha"),
            alt.Tooltip("series_name:N", title="Serie"),
            alt.Tooltip("period:N", title="Periodo"),
            alt.Tooltip("value:Q", title="Órdenes", format=",.0f")
        ]
    )

    line_testing = base.transform_filter(
        alt.datum.period == "Testing"
    ).mark_line(
        point=True,
        strokeWidth=3.2
    )

    line_forecast = base.transform_filter(
        alt.datum.period == "Forecast"
    ).mark_line(
        point=True,
        strokeWidth=3.2,
        strokeDash=[6, 6]
    )

    return (line_testing + line_forecast).properties(height=430)

def build_fail_rate_chart(fail_test_filtered, fail_future_filtered):
    frames = []

    if len(fail_test_filtered):
        actual_daily = (
            fail_test_filtered.groupby("date", as_index=False)["cancelled_orders_actual_estimado"]
            .sum()
            .rename(columns={"cancelled_orders_actual_estimado": "value"})
        )
        actual_daily["period"] = "Testing"
        actual_daily["series_name"] = "Cancelled actual"
        frames.append(actual_daily)

        forecast_test_daily = (
            fail_test_filtered.groupby("date", as_index=False)["cancelled_orders_forecast"]
            .sum()
            .rename(columns={"cancelled_orders_forecast": "value"})
        )
        forecast_test_daily["period"] = "Testing"
        forecast_test_daily["series_name"] = "Cancelled forecast"
        frames.append(forecast_test_daily)

    if len(fail_future_filtered):
        forecast_future_daily = (
            fail_future_filtered.groupby("date", as_index=False)["cancelled_orders_forecast"]
            .sum()
            .rename(columns={"cancelled_orders_forecast": "value"})
        )
        forecast_future_daily["period"] = "Forecast"
        forecast_future_daily["series_name"] = "Cancelled forecast"
        frames.append(forecast_future_daily)

    if not frames:
        return None

    plot_df = pd.concat(frames, ignore_index=True)
    plot_df = plot_df.dropna(subset=["value"]).copy()

    if plot_df.empty:
        return None

    y_min = plot_df["value"].min()
    y_max = plot_df["value"].max()
    y_range = y_max - y_min

    if y_range == 0:
        y_range = y_max * 0.1 if y_max != 0 else 1

    padded_min = max(0, y_min - y_range * 0.25)
    padded_max = y_max + y_range * 0.25

    color_scale = alt.Scale(
        domain=["Cancelled actual", "Cancelled forecast"],
        range=["#FA0050", "#00D9FC"]
    )

    base = alt.Chart(plot_df).encode(
        x=alt.X("date:T", title="Fecha"),
        y=alt.Y(
            "value:Q",
            title="Órdenes cancelled",
            scale=alt.Scale(domain=[padded_min, padded_max])
        ),
        color=alt.Color("series_name:N", title="Serie", scale=color_scale),
        tooltip=[
            alt.Tooltip("date:T", title="Fecha"),
            alt.Tooltip("series_name:N", title="Serie"),
            alt.Tooltip("period:N", title="Periodo"),
            alt.Tooltip("value:Q", title="Órdenes cancelled", format=",.2f")
        ]
    )

    line_testing = base.transform_filter(
        alt.datum.period == "Testing"
    ).mark_line(
        point=True,
        strokeWidth=3.2
    )

    line_forecast = base.transform_filter(
        alt.datum.period == "Forecast"
    ).mark_line(
        point=True,
        strokeWidth=3.2,
        strokeDash=[6, 6]
    )

    return (line_testing + line_forecast).properties(height=430)

def build_non_seamless_chart(ns_test_filtered, ns_future_filtered):
    frames = []

    if len(ns_test_filtered):
        actual_daily = (
            ns_test_filtered.groupby("date", as_index=False)["non_seamless_orders_actual_estimado"]
            .sum()
            .rename(columns={"non_seamless_orders_actual_estimado": "value"})
        )
        actual_daily["period"] = "Testing"
        actual_daily["series_name"] = "Non seamless actual"
        frames.append(actual_daily)

        forecast_test_daily = (
            ns_test_filtered.groupby("date", as_index=False)["non_seamless_orders_forecast"]
            .sum()
            .rename(columns={"non_seamless_orders_forecast": "value"})
        )
        forecast_test_daily["period"] = "Testing"
        forecast_test_daily["series_name"] = "Non seamless forecast"
        frames.append(forecast_test_daily)

    if len(ns_future_filtered):
        forecast_future_daily = (
            ns_future_filtered.groupby("date", as_index=False)["non_seamless_orders_forecast"]
            .sum()
            .rename(columns={"non_seamless_orders_forecast": "value"})
        )
        forecast_future_daily["period"] = "Forecast"
        forecast_future_daily["series_name"] = "Non seamless forecast"
        frames.append(forecast_future_daily)

    if not frames:
        return None

    plot_df = pd.concat(frames, ignore_index=True)
    plot_df = plot_df.dropna(subset=["value"]).copy()

    if plot_df.empty:
        return None

    y_min = plot_df["value"].min()
    y_max = plot_df["value"].max()
    y_range = y_max - y_min

    if y_range == 0:
        y_range = y_max * 0.1 if y_max != 0 else 1

    padded_min = max(0, y_min - y_range * 0.25)
    padded_max = y_max + y_range * 0.25

    color_scale = alt.Scale(
        domain=["Non seamless actual", "Non seamless forecast"],
        range=["#FA0050", "#00D9FC"]
    )

    base = alt.Chart(plot_df).encode(
        x=alt.X("date:T", title="Fecha"),
        y=alt.Y(
            "value:Q",
            title="Órdenes non seamless",
            scale=alt.Scale(domain=[padded_min, padded_max])
        ),
        color=alt.Color("series_name:N", title="Serie", scale=color_scale),
        tooltip=[
            alt.Tooltip("date:T", title="Fecha"),
            alt.Tooltip("series_name:N", title="Serie"),
            alt.Tooltip("period:N", title="Periodo"),
            alt.Tooltip("value:Q", title="Órdenes non seamless", format=",.2f")
        ]
    )

    line_testing = base.transform_filter(
        alt.datum.period == "Testing"
    ).mark_line(point=True, strokeWidth=3.2)

    line_forecast = base.transform_filter(
        alt.datum.period == "Forecast"
    ).mark_line(point=True, strokeWidth=3.2, strokeDash=[6, 6])

    return (line_testing + line_forecast).properties(height=430)

def apply_filters(df, start_date, end_date, selected_days, selected_holiday, selected_payday):
    out = df.copy()
    out = out[(out["date"].dt.date >= start_date) & (out["date"].dt.date <= end_date)]

    if selected_days:
        out = out[out["day_name"].isin(selected_days)]

    if selected_holiday:
        out = out[out["is_holiday"].isin(selected_holiday)]

    if "is_payday" in out.columns and selected_payday:
        out = out[out["is_payday"].isin(selected_payday)]

    return out

def apply_city_filters(df, start_date, end_date, selected_days, selected_holiday, selected_payday, selected_cities):
    out = df.copy()
    out = out[(out["date"].dt.date >= start_date) & (out["date"].dt.date <= end_date)]

    if selected_days is not None and len(selected_days) > 0:
        out = out[out["day_name"].isin(selected_days)]

    if selected_holiday is not None and len(selected_holiday) > 0:
        out = out[out["is_holiday"].isin(selected_holiday)]

    if "is_payday" in out.columns and selected_payday is not None and len(selected_payday) > 0:
        out = out[out["is_payday"].isin(selected_payday)]

    if selected_cities is not None and len(selected_cities) > 0:
        out = out[out["city_name"].isin(selected_cities)]

    return out

def apply_vertical_filters(df, start_date, end_date, selected_days, selected_holiday, selected_payday, selected_verticals):
    out = df.copy()
    out = out[(out["date"].dt.date >= start_date) & (out["date"].dt.date <= end_date)]

    if selected_days is not None and len(selected_days) > 0:
        out = out[out["day_name"].isin(selected_days)]

    if selected_holiday is not None and len(selected_holiday) > 0:
        out = out[out["is_holiday"].isin(selected_holiday)]

    if "is_payday" in out.columns and selected_payday is not None and len(selected_payday) > 0:
        out = out[out["is_payday"].isin(selected_payday)]

    if selected_verticals is not None and len(selected_verticals) > 0:
        out = out[out["vertical"].isin(selected_verticals)]

    return out

def apply_fail_rate_filters(
    df,
    start_date,
    end_date,
    selected_days,
    selected_holiday,
    selected_payday,
    selected_cities,
    selected_verticals
):
    out = df.copy()
    out = out[(out["date"].dt.date >= start_date) & (out["date"].dt.date <= end_date)]

    if selected_days is not None and len(selected_days) > 0:
        out = out[out["day_name"].isin(selected_days)]

    if selected_holiday is not None and len(selected_holiday) > 0:
        out = out[out["is_holiday"].isin(selected_holiday)]

    if "is_payday" in out.columns and selected_payday is not None and len(selected_payday) > 0:
        out = out[out["is_payday"].isin(selected_payday)]

    if selected_cities is not None and len(selected_cities) > 0:
        out = out[out["city_name"].astype(str).str.strip().isin(selected_cities)]

    if selected_verticals is not None and len(selected_verticals) > 0:
        out = out[out["vertical"].astype(str).str.strip().isin(selected_verticals)]

    return out

def apply_non_seamless_filters(
    df,
    start_date,
    end_date,
    selected_days,
    selected_holiday,
    selected_payday,
    selected_cities
):
    out = df.copy()
    out = out[(out["date"].dt.date >= start_date) & (out["date"].dt.date <= end_date)]

    if selected_days is not None and len(selected_days) > 0:
        out = out[out["day_name"].isin(selected_days)]

    if selected_holiday is not None and len(selected_holiday) > 0:
        out = out[out["is_holiday"].isin(selected_holiday)]

    if "is_payday" in out.columns and selected_payday is not None and len(selected_payday) > 0:
        out = out[out["is_payday"].isin(selected_payday)]

    if selected_cities is not None and len(selected_cities) > 0:
        out = out[out["city_name"].astype(str).str.strip().isin(selected_cities)]

    return out

# =========================================================
# HOME
# =========================================================
if st.session_state["page"] == "home":
    render_topbar(
        "SmartLogistics",
        "Centro de herramientas de IA para forecast, simulación y toma de decisiones"
    )

    st.write("")

    row1 = st.columns(3)
    row2 = st.columns(2)

    with row1[0]:
        st.markdown(
            """
            <div class="module-card">
                <div class="mini-tag">Activo</div>
                <h4>Forecast AI</h4>
                <p>Explora testing, forecast futuro, precisión de modelos y sugerencias automáticas por día.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Entrar a Forecast AI", use_container_width=True):
            go_to("forecast_ai")

    with row1[1]:
        st.markdown(
            """
            <div class="module-card">
                <div class="mini-tag">Próximamente</div>
                <h4>Simulación de acciones</h4>
                <p>Escenarios de sensibilidad y evaluación del impacto esperado ante cambios operativos.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.button("Próximamente", key="btn_coming_1", use_container_width=True, disabled=True)

    with row1[2]:
        st.markdown(
            """
            <div class="module-card">
                <div class="mini-tag">Próximamente</div>
                <h4>Prevención de demanda</h4>
                <p>Alertas anticipadas para días de riesgo, anomalías y variaciones esperadas de volumen.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.button("Próximamente", key="btn_coming_2", use_container_width=True, disabled=True)

    with row2[0]:
        st.markdown(
            """
            <div class="module-card">
                <div class="mini-tag">Próximamente</div>
                <h4>Contingencia</h4>
                <p>Apoyo para decisiones en días atípicos, feriados, eventos especiales o presión operativa.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.button("Próximamente", key="btn_coming_3", use_container_width=True, disabled=True)

    with row2[1]:
        st.markdown(
            """
            <div class="module-card">
                <div class="mini-tag">Próximamente</div>
                <h4>Insights IA</h4>
                <p>Hallazgos ejecutivos, resúmenes automáticos y lectura rápida del desempeño del forecast.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.button("Próximamente", key="btn_coming_4", use_container_width=True, disabled=True)

    st.stop()

# =========================================================
# FORECAST AI
# =========================================================
if st.session_state["page"] == "forecast_ai":
    render_topbar(
        "Forecast GT",
        "Forecasting inteligente utilizando modelos XGBoost + Prophet"
    )

    st.sidebar.markdown("## Filtrar:")

    global_min_date = min(test_df["date"].min(), future_df["date"].min()).date()
    global_max_date = max(test_df["date"].max(), future_df["date"].max()).date()

    sidebar_mode = st.sidebar.selectbox(
        "Vista de filtros",
        ["General", "Ciudad", "Vertical"]
    )

    date_range = st.sidebar.date_input(
        "Fechas:",
        value=(global_min_date, global_max_date),
        min_value=global_min_date,
        max_value=global_max_date
    )

    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date, end_date = global_min_date, global_max_date

    all_days = sorted(
        list(
            set(test_df["day_name"].dropna().unique().tolist()) |
            set(future_df["day_name"].dropna().unique().tolist())
        ),
        key=lambda x: day_order.index(x) if x in day_order else 99
    )

    all_days_selected = st.sidebar.checkbox("Todos los días", value=True)

    if all_days_selected:
        selected_days = all_days
    else:
        selected_days = st.sidebar.multiselect(
            "Día de la semana",
            all_days,
            default=[]
        )

        if selected_days:
            st.sidebar.caption("Días seleccionados: " + ", ".join(selected_days))
        else:
            st.sidebar.caption("Días seleccionados: Ninguno")

    all_holiday_selected = st.sidebar.checkbox("Todos los holiday", value=True)

    if all_holiday_selected:
        selected_holiday = [0, 1]
    else:
        holiday_options = {
            "Sí": 1,
            "No": 0
        }

        holiday_selected_labels = st.sidebar.multiselect(
            "Holiday",
            list(holiday_options.keys()),
            default=[]
        )

        selected_holiday = [holiday_options[x] for x in holiday_selected_labels]

        if holiday_selected_labels:
            st.sidebar.caption("Holiday seleccionado: " + ", ".join(holiday_selected_labels))
        else:
            st.sidebar.caption("Holiday seleccionado: Ninguno")

    all_payday_selected = st.sidebar.checkbox("Todos los payday", value=True)

    if all_payday_selected:
        selected_payday = [0, 1]
    else:
        payday_options = {
            "Sí": 1,
            "No": 0
        }

        payday_selected_labels = st.sidebar.multiselect(
            "Payday",
            list(payday_options.keys()),
            default=[]
        )

        selected_payday = [payday_options[x] for x in payday_selected_labels]

        if payday_selected_labels:
            st.sidebar.caption("Payday seleccionado: " + ", ".join(payday_selected_labels))
        else:
            st.sidebar.caption("Payday seleccionado: Ninguno")

    # =========================
    # FILTRO CIUDAD
    # =========================
    all_cities = sorted(
        list(
            set(city_test_df["city_name"].dropna().astype(str).unique().tolist()) |
            set(city_future_df["city_name"].dropna().astype(str).unique().tolist())
        )
    )

    if sidebar_mode == "Ciudad":
        all_cities_selected = st.sidebar.checkbox("Todas las ciudades", value=True)

        if all_cities_selected:
            selected_cities = all_cities
        else:
            selected_cities = st.sidebar.multiselect(
                "Ciudad",
                all_cities,
                default=[]
            )

            if selected_cities:
                st.sidebar.caption("Ciudades seleccionadas: " + ", ".join(selected_cities))
            else:
                st.sidebar.caption("Ciudades seleccionadas: Ninguna")
    else:
        selected_cities = all_cities

    # =========================
    # FILTRO VERTICAL
    # =========================
    all_verticals = sorted(
        list(
            set(vertical_test_df["vertical"].dropna().astype(str).unique().tolist()) |
            set(vertical_future_df["vertical"].dropna().astype(str).unique().tolist())
        )
    )

    if sidebar_mode == "Vertical":
        all_verticals_selected = st.sidebar.checkbox("Todas las verticales", value=True)

        if all_verticals_selected:
            selected_verticals = all_verticals
        else:
            selected_verticals = st.sidebar.multiselect(
                "Vertical",
                all_verticals,
                default=[]
            )

            if selected_verticals:
                st.sidebar.caption("Verticales seleccionadas: " + ", ".join(selected_verticals))
            else:
                st.sidebar.caption("Verticales seleccionadas: Ninguna")
    else:
        selected_verticals = all_verticals

    # =========================
    # ACCIONES
    # =========================
    st.sidebar.markdown("### Acciones")

    col1, col2 = st.sidebar.columns(2)

    with col1:
        if st.button("Ir a inicio", key="btn_inicio_sidebar", use_container_width=True):
            go_to("home")

    with col2:
        if st.button("Salir", key="btn_salir_sidebar", use_container_width=True):
            logout()

    # =========================
    # DATOS FILTRADOS
    # =========================
    test_filtered = apply_filters(
        test_df,
        start_date,
        end_date,
        selected_days,
        selected_holiday,
        selected_payday
    )

    future_filtered = apply_filters(
        future_df,
        start_date,
        end_date,
        selected_days,
        selected_holiday,
        selected_payday
    )

    city_test_filtered = apply_city_filters(
        city_test_df,
        start_date,
        end_date,
        selected_days,
        selected_holiday,
        selected_payday,
        selected_cities
    )

    city_future_filtered = apply_city_filters(
        city_future_df,
        start_date,
        end_date,
        selected_days,
        selected_holiday,
        selected_payday,
        selected_cities
    )

    vertical_test_filtered = apply_vertical_filters(
        vertical_test_df,
        start_date,
        end_date,
        selected_days,
        selected_holiday,
        selected_payday,
        selected_verticals
    )

    vertical_future_filtered = apply_vertical_filters(
        vertical_future_df,
        start_date,
        end_date,
        selected_days,
        selected_holiday,
        selected_payday,
        selected_verticals
    )

    fail_test_filtered = apply_fail_rate_filters(
        fail_test_df,
        start_date,
        end_date,
        selected_days,
        selected_holiday,
        selected_payday,
        selected_cities,
        selected_verticals
    )

    fail_future_filtered = apply_fail_rate_filters(
        fail_future_df,
        start_date,
        end_date,
        selected_days,
        selected_holiday,
        selected_payday,
        selected_cities,
        selected_verticals
    )

    ns_test_filtered = apply_non_seamless_filters(
        ns_test_df,
        start_date,
        end_date,
        selected_days,
        selected_holiday,
        selected_payday,
        selected_cities
    )

    ns_future_filtered = apply_non_seamless_filters(
        ns_future_df,
        start_date,
        end_date,
        selected_days,
        selected_holiday,
        selected_payday,
        selected_cities
    )

    current_combined_rows = pd.concat([
        test_filtered[["date"]],
        future_filtered[["date"]]
    ], ignore_index=True)["date"].dropna().nunique()

    # =========================
    # TABS
    # =========================
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Forecast Órdenes por Día",
        "Forecast por Ciudad",
        "Forecast por Vertical",
        "Forecast con Fail Rate",
        "Forecast con Seamless"
    ])

    with tab1:
        # =========================
        # FILA 1
        # =========================
        k1, k2, k3 = st.columns([1, 2, 1])

        with k1:
            st.metric("Fechas visibles", current_combined_rows)

        with k2:
            total_ordenes = 0

            if len(test_filtered) and "actual" in test_filtered.columns:
                total_ordenes += test_filtered["actual"].fillna(0).sum()

            if len(future_filtered) and "Ensamble Automático" in future_filtered.columns:
                total_ordenes += future_filtered["Ensamble Automático"].fillna(0).sum()

            st.metric("Total órdenes", f"{int(total_ordenes):,}")

        with k3:
            if len(test_filtered):
                mape_ensamble = np.nanmean(test_filtered["APE__Ensamble Automático"])
                st.metric("Forecast Error %", f"{mape_ensamble:.2f}%")
            else:
                st.metric("Forecast Error %", "-")

        st.write("")

        # =========================
        # FILA 2
        # =========================
        k4, k5 = st.columns(2)

        with k4:
            if len(test_filtered) and "actual" in test_filtered.columns:
                total_actual = test_filtered["actual"].fillna(0).sum()
                st.metric("Total órdenes actual", f"{int(total_actual):,}")
            else:
                st.metric("Total órdenes actual", "-")

        with k5:
            if len(future_filtered) and "Ensamble Automático" in future_filtered.columns:
                total_forecast = future_filtered["Ensamble Automático"].fillna(0).sum()
                st.metric("Total órdenes forecast", f"{int(total_forecast):,}")
            else:
                st.metric("Total órdenes forecast", "-")

        st.write("")

        st.markdown("### Comportamiento histórico + forecast")
        combined_chart = build_combined_chart(test_filtered, future_filtered)

        if combined_chart is not None:
            st.altair_chart(combined_chart, use_container_width=True)
            st.caption("Línea sólida = testing. Línea punteada = forecast.")
        else:
            st.info("No hay datos con los filtros seleccionados.")

        st.write("")
        st.markdown("### Detalle diario")

        # Datos históricos (testing)
        test_table = test_filtered.copy()
        test_table["Forecast"] = np.nan

        if "recommended_model" in test_table.columns:
            def get_test_forecast(row):
                model = row.get("recommended_model", np.nan)
                if pd.isna(model):
                    return np.nan
                return row.get(model, np.nan)

            test_table["Forecast"] = test_table.apply(get_test_forecast, axis=1)
        else:
            if "Ensamble Automático" in test_table.columns:
                test_table["Forecast"] = test_table["Ensamble Automático"]

        # Datos futuros
        future_table = future_filtered.copy()
        future_table["actual"] = np.nan

        if "recommended_prediction" in future_table.columns:
            future_table["Forecast"] = future_table["recommended_prediction"]
        else:
            future_table["Forecast"] = np.nan

        # Unir ambos
        daily_table = pd.concat([test_table, future_table], ignore_index=True, sort=False)

        # Asegurar columnas
        if "day_name" not in daily_table.columns:
            daily_table["day_name"] = daily_table["date"].dt.day_name()

        if "is_holiday" not in daily_table.columns:
            daily_table["is_holiday"] = 0

        if "is_payday" not in daily_table.columns:
            daily_table["is_payday"] = 0

        # Seleccionar y renombrar
        daily_table = daily_table[[
            "date",
            "day_name",
            "is_holiday",
            "is_payday",
            "actual",
            "Forecast"
        ]].copy()

        daily_table = daily_table.rename(columns={
            "date": "Fecha",
            "day_name": "Día Semana",
            "is_holiday": "Es holiday",
            "is_payday": "Es Payday",
            "actual": "Actual"
        })

        daily_table["Fecha"] = pd.to_datetime(daily_table["Fecha"]).dt.strftime("%Y-%m-%d")
        daily_table["Es holiday"] = daily_table["Es holiday"].fillna(0).astype(int)
        daily_table["Es Payday"] = daily_table["Es Payday"].fillna(0).astype(int)

        if "Actual" in daily_table.columns:
            daily_table["Actual"] = daily_table["Actual"].round(0)

        if "Forecast" in daily_table.columns:
            daily_table["Forecast"] = daily_table["Forecast"].round(0)

        st.dataframe(daily_table, use_container_width=True, hide_index=True)

    with tab2:
        # =========================
        # FILA 1
        # =========================
        c1, c2, c3 = st.columns([1, 2, 1])

        with c1:
            city_visible_dates = pd.concat([
                city_test_filtered[["date"]],
                city_future_filtered[["date"]]
            ], ignore_index=True)["date"].dropna().nunique()

            st.metric("Fechas visibles", city_visible_dates)

        with c2:
            total_city = 0

            if len(city_test_filtered):
                total_city += city_test_filtered["ordenes_ciudad_actual"].fillna(0).sum()

            if len(city_future_filtered):
                total_city += city_future_filtered["ordenes_ciudad_forecast"].fillna(0).sum()

            st.metric("Total órdenes ciudad", f"{int(total_city):,}")

        with c3:
            if len(city_test_filtered):
                city_error = np.nanmean(city_test_filtered["APE__forecast_ciudad"])
                st.metric("Forecast Error %", f"{city_error:.2f}%")
            else:
                st.metric("Forecast Error %", "-")

        st.write("")

        # =========================
        # FILA 2
        # =========================
        c4, c5 = st.columns(2)

        with c4:
            if len(city_test_filtered):
                total_city_actual = city_test_filtered["ordenes_ciudad_actual"].fillna(0).sum()
                st.metric("Total órdenes actual", f"{int(total_city_actual):,}")
            else:
                st.metric("Total órdenes actual", "-")

        with c5:
            if len(city_future_filtered):
                total_city_forecast = city_future_filtered["ordenes_ciudad_forecast"].fillna(0).sum()
                st.metric("Total órdenes forecast", f"{int(total_city_forecast):,}")
            else:
                st.metric("Total órdenes forecast", "-")

        st.write("")

        st.markdown("### Forecast por Ciudad")
        city_chart = build_city_chart(city_test_filtered, city_future_filtered)

        if city_chart is not None:
            st.altair_chart(city_chart, use_container_width=True)
            st.caption("Línea sólida = testing. Línea punteada = forecast.")
        else:
            st.info("No hay datos por ciudad con los filtros seleccionados.")

        st.write("")
        st.markdown("### Detalle por ciudad")

        city_test_table = city_test_filtered.copy()
        city_future_table = city_future_filtered.copy()

        city_future_table["ordenes_ciudad_actual"] = np.nan

        city_detail = pd.concat([city_test_table, city_future_table], ignore_index=True, sort=False)

        city_detail = city_detail[[
            "date",
            "city_name",
            "day_name",
            "is_holiday",
            "is_payday",
            "share_ciudad",
            "ordenes_ciudad_actual",
            "ordenes_ciudad_forecast"
        ]].copy()

        city_detail = city_detail.rename(columns={
            "date": "Fecha",
            "city_name": "Ciudad",
            "day_name": "Día Semana",
            "is_holiday": "Es holiday",
            "is_payday": "Es Payday",
            "share_ciudad": "Share ciudad",
            "ordenes_ciudad_actual": "Actual",
            "ordenes_ciudad_forecast": "Forecast"
        })

        city_detail["Fecha"] = pd.to_datetime(city_detail["Fecha"]).dt.strftime("%Y-%m-%d")
        city_detail["Es holiday"] = city_detail["Es holiday"].fillna(0).astype(int)
        city_detail["Es Payday"] = city_detail["Es Payday"].fillna(0).astype(int)

        if "Share ciudad" in city_detail.columns:
            city_detail["Share ciudad"] = city_detail["Share ciudad"].round(4)

        if "Actual" in city_detail.columns:
            city_detail["Actual"] = city_detail["Actual"].round(0)

        if "Forecast" in city_detail.columns:
            city_detail["Forecast"] = city_detail["Forecast"].round(0)

        st.dataframe(city_detail, use_container_width=True, hide_index=True)

    with tab3:
        # =========================
        # FILA 1
        # =========================
        v1, v2, v3 = st.columns([1, 2, 1])

        with v1:
            vertical_visible_dates = pd.concat([
                vertical_test_filtered[["date"]],
                vertical_future_filtered[["date"]]
            ], ignore_index=True)["date"].dropna().nunique()

            st.metric("Fechas visibles", vertical_visible_dates)

        with v2:
            total_vertical = 0

            if len(vertical_test_filtered):
                total_vertical += vertical_test_filtered["ordenes_vertical_actual"].fillna(0).sum()

            if len(vertical_future_filtered):
                total_vertical += vertical_future_filtered["ordenes_vertical_forecast"].fillna(0).sum()

            st.metric("Total órdenes vertical", f"{int(total_vertical):,}")

        with v3:
            if len(vertical_test_filtered):
                vertical_error = np.nanmean(vertical_test_filtered["APE__forecast_vertical"])
                st.metric("Forecast Error %", f"{vertical_error:.2f}%")
            else:
                st.metric("Forecast Error %", "-")

        st.write("")

        # =========================
        # FILA 2
        # =========================
        v4, v5 = st.columns(2)

        with v4:
            if len(vertical_test_filtered):
                total_vertical_actual = vertical_test_filtered["ordenes_vertical_actual"].fillna(0).sum()
                st.metric("Total órdenes actual", f"{int(total_vertical_actual):,}")
            else:
                st.metric("Total órdenes actual", "-")

        with v5:
            if len(vertical_future_filtered):
                total_vertical_forecast = vertical_future_filtered["ordenes_vertical_forecast"].fillna(0).sum()
                st.metric("Total órdenes forecast", f"{int(total_vertical_forecast):,}")
            else:
                st.metric("Total órdenes forecast", "-")

        st.write("")

        st.markdown("### Forecast por Vertical")
 
        vertical_chart = build_vertical_chart(vertical_test_filtered, vertical_future_filtered)

        if vertical_chart is not None:
            st.altair_chart(vertical_chart, use_container_width=True)
            st.caption("Línea sólida = testing. Línea punteada = forecast.")
        else:
            st.info("No hay datos por vertical con los filtros seleccionados.")

        st.write("")
        st.markdown("### Detalle por vertical")

        vertical_test_table = vertical_test_filtered.copy()
        vertical_future_table = vertical_future_filtered.copy()

        if "ordenes_vertical_actual" not in vertical_future_table.columns:
            vertical_future_table["ordenes_vertical_actual"] = np.nan

        vertical_detail = pd.concat(
            [vertical_test_table, vertical_future_table],
            ignore_index=True,
            sort=False
        )

        required_cols = [
            "date",
            "vertical",
            "day_name",
            "is_holiday",
            "is_payday",
            "share_vertical",
            "ordenes_vertical_actual",
            "ordenes_vertical_forecast"
        ]

        for col in required_cols:
            if col not in vertical_detail.columns:
                vertical_detail[col] = np.nan

        vertical_detail = vertical_detail[required_cols].copy()

        vertical_detail = vertical_detail.rename(columns={
            "date": "Fecha",
            "vertical": "Vertical",
            "day_name": "Día Semana",
            "is_holiday": "Es holiday",
            "is_payday": "Es Payday",
            "share_vertical": "Share vertical",
            "ordenes_vertical_actual": "Actual",
            "ordenes_vertical_forecast": "Forecast"
        })

        vertical_detail["Fecha"] = pd.to_datetime(vertical_detail["Fecha"], errors="coerce").dt.strftime("%Y-%m-%d")
        vertical_detail["Es holiday"] = vertical_detail["Es holiday"].fillna(0).astype(int)
        vertical_detail["Es Payday"] = vertical_detail["Es Payday"].fillna(0).astype(int)

        if "Share vertical" in vertical_detail.columns:
            vertical_detail["Share vertical"] = pd.to_numeric(vertical_detail["Share vertical"], errors="coerce").round(4)

        if "Actual" in vertical_detail.columns:
            vertical_detail["Actual"] = pd.to_numeric(vertical_detail["Actual"], errors="coerce").round(0)

        if "Forecast" in vertical_detail.columns:
            vertical_detail["Forecast"] = pd.to_numeric(vertical_detail["Forecast"], errors="coerce").round(0)

        st.dataframe(vertical_detail, use_container_width=True, hide_index=True)        
        
    with tab4:
        # =========================
        # FILA 1
        # =========================
        f1, f2, f3 = st.columns([1, 2, 1])

        with f1:
            fail_visible_dates = pd.concat([
                fail_test_filtered[["date"]],
                fail_future_filtered[["date"]]
            ], ignore_index=True)["date"].dropna().nunique()

            st.metric("Fechas visibles", fail_visible_dates)

        with f2:
            total_segment_orders = 0

            if len(fail_test_filtered):
                total_segment_orders += fail_test_filtered["total_orders_segment_actual"].fillna(0).sum()

            if len(fail_future_filtered):
                total_segment_orders += fail_future_filtered["total_orders_segment_forecast"].fillna(0).sum()

            st.metric("Total órdenes", f"{int(total_segment_orders):,}")

        with f3:
            total_cancelled = 0
            total_orders = 0

            if len(fail_test_filtered):
                total_cancelled += fail_test_filtered["cancelled_orders_actual_estimado"].fillna(0).sum()
                total_orders += fail_test_filtered["total_orders_segment_actual"].fillna(0).sum()

            if len(fail_future_filtered):
                total_cancelled += fail_future_filtered["cancelled_orders_forecast"].fillna(0).sum()
                total_orders += fail_future_filtered["total_orders_segment_forecast"].fillna(0).sum()

            fail_rate_pct = (total_cancelled / total_orders * 100) if total_orders > 0 else np.nan
            st.metric("Fail Rate %", f"{fail_rate_pct:.2f}%" if pd.notna(fail_rate_pct) else "-")

        st.write("")

        # =========================
        # FILA 2
        # =========================
        f4, f5 = st.columns(2)

        with f4:
            if len(fail_test_filtered):
                total_cancelled_actual = fail_test_filtered["cancelled_orders_actual_estimado"].fillna(0).sum()
                st.metric("Órdenes cancelled actual", f"{int(round(total_cancelled_actual)):,}")
            else:
                st.metric("Órdenes cancelled actual", "-")

        with f5:
            if len(fail_future_filtered):
                total_cancelled_forecast = fail_future_filtered["cancelled_orders_forecast"].fillna(0).sum()
                st.metric("Órdenes cancelled forecast", f"{int(round(total_cancelled_forecast)):,}")
            else:
                st.metric("Órdenes cancelled forecast", "-")

        st.write("")

        st.markdown("### Forecast de Fail Rate")

        fail_chart = build_fail_rate_chart(fail_test_filtered, fail_future_filtered)

        if fail_chart is not None:
            st.altair_chart(fail_chart, use_container_width=True)
            st.caption("Línea sólida = testing. Línea punteada = forecast.")
        else:
            st.info("No hay datos de fail rate con los filtros seleccionados.")

        st.write("")
        st.markdown("### Detalle fail rate")

        fail_test_table = fail_test_filtered.copy()
        fail_future_table = fail_future_filtered.copy()

        fail_future_table["total_orders_segment_actual"] = np.nan
        fail_future_table["cancelled_orders_actual_estimado"] = np.nan
        fail_future_table["fail_rate_actual_pct"] = np.nan

        fail_detail = pd.concat([fail_test_table, fail_future_table], ignore_index=True, sort=False)

        required_cols = [
            "date",
            "city_name",
            "vertical",
            "day_name",
            "is_holiday",
            "is_payday",
            "share_city_vertical",
            "total_orders_segment_actual",
            "total_orders_segment_forecast",
            "cancelled_orders_actual_estimado",
            "cancelled_orders_forecast",
            "fail_rate_actual_pct",
            "fail_rate_forecast_pct"
        ]

        for col in required_cols:
            if col not in fail_detail.columns:
                fail_detail[col] = np.nan

        fail_detail = fail_detail[required_cols].copy()

        fail_detail = fail_detail.rename(columns={
            "date": "Fecha",
            "city_name": "Ciudad",
            "vertical": "Vertical",
            "day_name": "Día Semana",
            "is_holiday": "Es holiday",
            "is_payday": "Es Payday",
            "share_city_vertical": "Share city-vertical",
            "total_orders_segment_actual": "Órdenes actual",
            "total_orders_segment_forecast": "Órdenes forecast",
            "cancelled_orders_actual_estimado": "Cancelled actual",
            "cancelled_orders_forecast": "Cancelled forecast",
            "fail_rate_actual_pct": "Fail Rate actual %",
            "fail_rate_forecast_pct": "Fail Rate forecast %"
        })

        fail_detail["Fecha"] = pd.to_datetime(fail_detail["Fecha"], errors="coerce").dt.strftime("%Y-%m-%d")
        fail_detail["Es holiday"] = fail_detail["Es holiday"].fillna(0).astype(int)
        fail_detail["Es Payday"] = fail_detail["Es Payday"].fillna(0).astype(int)

        for col in [
            "Share city-vertical",
            "Órdenes actual",
            "Órdenes forecast",
            "Cancelled actual",
            "Cancelled forecast",
            "Fail Rate actual %",
            "Fail Rate forecast %"
        ]:
            if col in fail_detail.columns:
                fail_detail[col] = pd.to_numeric(fail_detail[col], errors="coerce").round(4)

        st.dataframe(fail_detail, use_container_width=True, hide_index=True)

    with tab5:
        st.markdown("### Forecast con Non Seamless Orders")

        # =========================
        # FILA 1
        # =========================
        n1, n2, n3 = st.columns([1, 2, 1])

        with n1:
            ns_visible_dates = pd.concat([
                ns_test_filtered[["date"]],
                ns_future_filtered[["date"]]
            ], ignore_index=True)["date"].dropna().nunique()

            st.metric("Fechas visibles", ns_visible_dates)

        with n2:
            total_city_orders = 0

            if len(ns_test_filtered):
                total_city_orders += ns_test_filtered["total_orders_city_actual"].fillna(0).sum()

            if len(ns_future_filtered):
                total_city_orders += ns_future_filtered["total_orders_city_forecast"].fillna(0).sum()

            st.metric("Total órdenes", f"{int(total_city_orders):,}")

        with n3:
            seamless_orders = 0
            total_orders = 0

            if len(ns_test_filtered):
                seamless_orders += (
                    ns_test_filtered["total_orders_city_actual"].fillna(0).sum()
                    - ns_test_filtered["non_seamless_orders_actual_estimado"].fillna(0).sum()
                )
                total_orders += ns_test_filtered["total_orders_city_actual"].fillna(0).sum()

            if len(ns_future_filtered):
                seamless_orders += (
                    ns_future_filtered["total_orders_city_forecast"].fillna(0).sum()
                    - ns_future_filtered["non_seamless_orders_forecast"].fillna(0).sum()
                )
                total_orders += ns_future_filtered["total_orders_city_forecast"].fillna(0).sum()

            seamless_pct = (seamless_orders / total_orders * 100) if total_orders > 0 else np.nan
            st.metric("Seamless %", f"{seamless_pct:.2f}%" if pd.notna(seamless_pct) else "-")

        st.write("")

        # =========================
        # FILA 2
        # =========================
        n4, n5 = st.columns(2)

        with n4:
            if len(ns_test_filtered):
                total_non_seamless_actual = ns_test_filtered["non_seamless_orders_actual_estimado"].fillna(0).sum()
                st.metric("Órdenes non seamless actual", f"{int(round(total_non_seamless_actual)):,}")
            else:
                st.metric("Órdenes non seamless actual", "-")

        with n5:
            if len(ns_future_filtered):
                total_non_seamless_forecast = ns_future_filtered["non_seamless_orders_forecast"].fillna(0).sum()
                st.metric("Órdenes non seamless forecast", f"{int(round(total_non_seamless_forecast)):,}")
            else:
                st.metric("Órdenes non seamless forecast", "-")

        st.write("")

        ns_chart = build_non_seamless_chart(ns_test_filtered, ns_future_filtered)

        if ns_chart is not None:
            st.altair_chart(ns_chart, use_container_width=True)
            st.caption("Línea sólida = testing. Línea punteada = forecast.")
        else:
            st.info("No hay datos de non seamless con los filtros seleccionados.")

        st.write("")
        st.markdown("### Detalle non seamless")

        ns_test_table = ns_test_filtered.copy()
        ns_future_table = ns_future_filtered.copy()

        ns_future_table["total_orders_city_actual"] = np.nan
        ns_future_table["non_seamless_orders_actual_estimado"] = np.nan
        ns_future_table["seamless_pct_actual"] = np.nan

        ns_detail = pd.concat([ns_test_table, ns_future_table], ignore_index=True, sort=False)

        required_cols = [
            "date",
            "city_name",
            "day_name",
            "is_holiday",
            "is_payday",
            "share_ciudad",
            "total_orders_city_actual",
            "total_orders_city_forecast",
            "non_seamless_orders_actual_estimado",
            "non_seamless_orders_forecast",
            "seamless_pct_actual",
            "seamless_pct_forecast"
        ]

        for col in required_cols:
            if col not in ns_detail.columns:
                ns_detail[col] = np.nan

        ns_detail = ns_detail[required_cols].copy()

        ns_detail = ns_detail.rename(columns={
            "date": "Fecha",
            "city_name": "Ciudad",
            "day_name": "Día Semana",
            "is_holiday": "Es holiday",
            "is_payday": "Es Payday",
            "share_ciudad": "Share ciudad",
            "total_orders_city_actual": "Órdenes actual",
            "total_orders_city_forecast": "Órdenes forecast",
            "non_seamless_orders_actual_estimado": "Non seamless actual",
            "non_seamless_orders_forecast": "Non seamless forecast",
            "seamless_pct_actual": "Seamless actual %",
            "seamless_pct_forecast": "Seamless forecast %"
        })

        ns_detail["Fecha"] = pd.to_datetime(ns_detail["Fecha"], errors="coerce").dt.strftime("%Y-%m-%d")
        ns_detail["Es holiday"] = ns_detail["Es holiday"].fillna(0).astype(int)
        ns_detail["Es Payday"] = ns_detail["Es Payday"].fillna(0).astype(int)

        for col in [
            "Share ciudad",
            "Órdenes actual",
            "Órdenes forecast",
            "Non seamless actual",
            "Non seamless forecast",
            "Seamless actual %",
            "Seamless forecast %"
        ]:
            if col in ns_detail.columns:
                ns_detail[col] = pd.to_numeric(ns_detail[col], errors="coerce").round(4)

        st.dataframe(ns_detail, use_container_width=True, hide_index=True)

st.write("")
st.caption("Created by: nancy.valdes@pedidosya.com")
