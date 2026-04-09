import streamlit as st
import hashlib

# =========================
# CONFIG
# =========================
ALLOWED_EMAIL = "peyaridergt@pedidosya.com"

# Password de prueba: Peya123!
PASSWORD_HASH = hashlib.sha256("Peya123!".encode()).hexdigest()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# =========================
# LOGIN
# =========================
def login():
    st.title("🔐 Login Dashboard")

    email = st.text_input("Correo")
    password = st.text_input("Password", type="password")

    if st.button("Ingresar"):
        if email.strip().lower() != ALLOWED_EMAIL:
            st.error("No tienes acceso a este dashboard.")
            return

        if hash_password(password) != PASSWORD_HASH:
            st.error("Password incorrecta.")
            return

        st.session_state["logged_in"] = True
        st.session_state["user"] = email
        st.rerun()


def logout():
    st.session_state["logged_in"] = False
    st.session_state["user"] = None
    st.rerun()


# =========================
# SESSION STATE
# =========================
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "user" not in st.session_state:
    st.session_state["user"] = None


# =========================
# APP FLOW
# =========================
if not st.session_state["logged_in"]:
    login()
    st.stop()


# =========================
# DASHBOARD
# =========================
st.success(f"Bienvenido/a {st.session_state['user']} 🎉")

col1, col2 = st.columns([4, 1])
with col2:
    if st.button("Cerrar sesión"):
        logout()

st.title("📊 Dashboard RT y Forecast")

# 🔽 AQUÍ VA TU DASHBOARD REAL
st.metric("Órdenes", "3,245")
st.metric("Ventas", "Q 125,000")
st.line_chart([10, 20, 15, 30, 25, 40])