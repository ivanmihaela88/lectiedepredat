import streamlit as st

st.set_page_config(
    page_title="Lecție WOW - Streamlit",
    page_icon="💻",
    layout="wide"
)

st.sidebar.title("Navigare")
st.sidebar.markdown("""
### Alege pagina:

🏠 Lecție principală  
📚 Teorie  
📈 Aplicație interactivă  
🛠️ Exerciții  
🧠 Quiz final  

Folosește meniul automat din stânga sus pentru pagini.
""")

st.title("💻 Lecție WOW: Aplicație interactivă cu Streamlit")
st.caption("Clasa a X-a | Informatică")

st.markdown("""
## 🎯 Scopul lecției

Astăzi construim și analizăm o aplicație web interactivă realizată în Python cu Streamlit.

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
