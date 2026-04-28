import streamlit as st

st.title("🧠 4. Quiz final")

scor = 0

q1 = st.radio(
    "1. Ce face `st.slider()`?",
    ["Afișează o poză", "Permite utilizatorului să aleagă o valoare", "Închide aplicația"],
    index=None
)

q2 = st.radio(
    "2. Ce reprezintă a, b și c în program?",
    ["Variabile", "Fișiere", "Pagini web"],
    index=None
)

q3 = st.radio(
    "3. Ce face linia `y = a * x**2 + b * x + c`?",
    ["Calculează valorile funcției", "Șterge graficul", "Deschide browserul"],
    index=None
)

q4 = st.radio(
    "4. Ce bibliotecă folosim pentru grafic?",
    ["matplotlib", "random", "time"],
    index=None
)

q5 = st.radio(
    "5. Care este ordinea corectă?",
    ["Output → Input → Procesare", "Input → Procesare → Output", "Procesare → Output → Input"],
    index=None
)

if st.button("✅ Verifică răspunsurile"):
    if q1 == "Permite utilizatorului să aleagă o valoare":
        scor += 1
    if q2 == "Variabile":
        scor += 1
    if q3 == "Calculează valorile funcției":
        scor += 1
    if q4 == "matplotlib":
        scor += 1
    if q5 == "Input → Procesare → Output":
        scor += 1

    st.subheader(f"Scor: {scor}/5")

    if scor == 5:
        st.success("Excelent! Ai înțeles foarte bine lecția.")
    elif scor >= 3:
        st.info("Bine! Mai repetă puțin partea de cod.")
    else:
        st.warning("Mai parcurge încă o dată lecția.")
st.sidebar.title("Navigare")

st.sidebar.page_link("app.py", label="🏠 Lecție")
st.sidebar.page_link("pages/1_📚_Teorie.py", label="📚 Teorie")
st.sidebar.page_link("pages/2_📈_Aplicatie_interactiva.py", label="📈 Aplicație")
st.sidebar.page_link("pages/3_🛠️_Exercitii.py", label="🛠️ Exerciții")
st.sidebar.page_link("pages/4_🧠_Quiz.py", label="🧠 Quiz")
