import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Lecție Streamlit", page_icon="💻")

st.title("💻 Lecție: Aplicație interactivă cu Streamlit")
st.caption("Clasa a X-a")

# =====================
# TEORIE
# =====================

st.header("📚 1. Teorie")

st.markdown("""
## Cum funcționează o aplicație?

### INPUT → PROCESARE → OUTPUT

- **Input:** utilizatorul introduce valori  
- **Procesare:** programul calculează  
- **Output:** afișăm rezultatul  

Exemplu din aplicația noastră:
""")

st.code("""
a = st.slider("Alege valoarea lui a", -5.0, 5.0, 1.0)
y = a * x**2 + b * x + c
st.pyplot(fig)
""")

# =====================
# APLICAȚIE
# =====================

st.header("📈 2. Aplicație interactivă")

st.write("Modifică valorile și observă graficul:")

col1, col2, col3 = st.columns(3)

with col1:
    a = st.slider("a", -5.0, 5.0, 1.0)

with col2:
    b = st.slider("b", -10.0, 10.0, 0.0)

with col3:
    c = st.slider("c", -10.0, 10.0, 0.0)

if a == 0:
    st.error("a trebuie să fie diferit de 0")
else:
    x = np.linspace(-10, 10, 100)
    y = a*x**2 + b*x + c

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.grid()

    st.pyplot(fig)

    st.success(f"f(x) = {a}x² + {b}x + {c}")

    if a > 0:
        st.info("Parabola este deschisă în sus")
    else:
        st.warning("Parabola este deschisă în jos")

# =====================
# EXERCIȚII
# =====================

st.header("🛠️ 3. Exerciții")

st.markdown("""
### Nivel ușor:
- schimbă titlul aplicației
- modifică intervalul slider-ului

### Nivel mediu:
- afișează valoarea lui Delta
- adaugă un mesaj pentru a > 0

### Nivel avansat:
- creează o funcție liniară (f(x)=mx+n)
""")

# =====================
# QUIZ
# =====================

st.header("🧠 4. Quiz")

scor = 0

q1 = st.radio(
    "1. Ce face st.slider()?",
    ["Afișează o poză", "Permite alegerea unei valori", "Închide aplicația"],
    index=None
)

q2 = st.radio(
    "2. Ce sunt a, b și c?",
    ["Variabile", "Fișiere", "Pagini web"],
    index=None
)

q3 = st.radio(
    "3. Ce face formula?",
    ["Calculează funcția", "Șterge graficul", "Deschide browserul"],
    index=None
)

if st.button("Verifică"):
    if q1 == "Permite alegerea unei valori":
        scor += 1
    if q2 == "Variabile":
        scor += 1
    if q3 == "Calculează funcția":
        scor += 1

    st.write(f"Scor: {scor}/3")
