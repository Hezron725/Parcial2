import streamlit as st

# --- Presentación Personal ---
st.title("Portafolio de APIs - Hezron Barillas")
st.image("https://cdn-icons-png.flaticon.com/512/1077/1077114.png", width=120)

st.markdown("""
### 👋 Hola, soy **Hezron Arfaxad Barillas Herrera**
- 📍 País: **El Salvador**
- 💻 Me dedico a: **Pruebas y desarrollo de aplicaciones iniciales**
- 🎓 Carrera: **Ingeniería en Sistemas Informáticos**
- 🌱 Me interesa aprender sobre **inteligencia artificial, APIs y desarrollo web**

---
""")

# --- Proyectos ---
st.header("📂 Proyectos de Consumo de API")

st.markdown("""
Aquí podrás acceder a las APIs que he creado para este proyecto:
""")

st.markdown("""
- ☁️ [Api de Situacion Climatica](https://github.com/Hezron725/Situaci-n-climatica)            
- 🧀 [API de Quesos del Mundo](https://github.com/Hezron725/Apis-de-Quesos)
- 🐈 [API de Gatos del Mundo](https://github.com/Hezron725/Razas-de-Gatitos)
""")

st.info("Cada API muestra listas de datos generadas desde Streamlit con estructura modular.")
