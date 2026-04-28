import streamlit as st

st.set_page_config(
    page_title="Lecție WOW - Streamlit",
    page_icon="💻",
    layout="wide"
)

st.sidebar.title("Navigare")
st.sidebar.page_link("app.py", label="🏠 Lecție principală")
st.sidebar.page_link("pages/1_📚_Teorie.py", label="📚 Teorie")
st.sidebar.page_link("pages/2_📈_Aplicatie_interactiva.py", label="📈 Aplicație interactivă")
st.sidebar.page_link("pages/3_🛠️_Exercitii.py", label="🛠️ Exerciții")
st.sidebar.page_link("pages/4_🧠_Quiz.py", label="🧠 Quiz final")

st.title("💻 Lecție WOW: Aplicație interactivă cu Streamlit")
st.caption("Clasa a X-a | Informatică")

st.markdown("""
## 🎯 Scopul lecției

Astăzi construim și analizăm o aplicație web interactivă realizată în Python cu Streamlit.

Vom urmări ideea de bază din multe aplicații informatice:

### INPUT → PROCESARE → OUTPUT

- **Input:** utilizatorul alege valori
- **Procesare:** programul calculează
- **Output:** aplicația afișează rezultatul

---

## 🧠 Ce vom învăța

✅ ce este Streamlit  
✅ cum folosim variabile  
✅ cum citim valori de la utilizator  
✅ cum facem calcule în Python  
✅ cum afișăm grafice  
✅ cum testăm o aplicație interactivă  
""")
