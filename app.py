import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Lecție WOW Streamlit", page_icon="💻", layout="wide")

st.title("💻 Lecție WOW: Aplicație interactivă cu Streamlit")
st.caption("Clasa a X-a | Informatică")

tab1, tab2, tab3, tab4 = st.tabs([
    "📚 Teorie",
    "📈 Aplicație interactivă",
    "🛠️ Exerciții",
    "🧠 Quiz final"
])

with tab1:
    st.header("📚 Teorie")
    st.markdown("""
    ## Modelul unei aplicații interactive

    O aplicație interactivă are 3 pași:

    ### INPUT → PROCESARE → OUTPUT

    - **Input:** utilizatorul introduce valori
    - **Procesare:** programul face calcule
    - **Output:** aplicația afișează rezultatul

    În lecția noastră folosim Python și Streamlit.
    """)

    st.code("""
a = st.slider("Alege valoarea lui a", -5.0, 5.0, 1.0)
y = a * x**2 + b * x + c
st.pyplot(fig)
""", language="python")

with tab2:
    st.header("📈 Aplicație interactivă")

    st.markdown("Funcția folosită este: **f(x) = ax² + bx + c**")

    col1, col2, col3 = st.columns(3)

    with col1:
        a = st.slider("Coeficientul a", -5.0, 5.0, 1.0, 0.5)

    with col2:
        b = st.slider("Coeficientul b", -10.0, 10.0, 0.0, 0.5)

    with col3:
        c = st.slider("Coeficientul c", -10.0, 10.0, 0.0, 0.5)

    if a == 0:
        st.error("Pentru funcția de gradul al II-lea, a trebuie să fie diferit de 0.")
    else:
        x = np.linspace(-10, 10, 400)
        y = a * x**2 + b * x + c

        delta = b**2 - 4*a*c
        xv = -b / (2*a)
        yv = a * xv**2 + b * xv + c

        fig, ax = plt.subplots()
        ax.plot(x, y, label="f(x)")
        ax.scatter([xv], [yv], label="Vârful parabolei")
        ax.axhline(0, linewidth=1)
        ax.axvline(0, linewidth=1)
        ax.grid(True)
        ax.legend()

        st.pyplot(fig)

        st.success(f"Funcția este: f(x) = {a}x² + {b}x + {c}")
        st.metric("Delta", f"{delta:.2f}")
        st.metric("Vârful parabolei", f"V({xv:.2f}, {yv:.2f})")

        if a > 0:
            st.info("Parabola este deschisă în sus.")
        else:
            st.warning("Parabola este deschisă în jos.")

with tab3:
    st.header("🛠️ Exerciții")

    st.markdown("""
    ## Nivel ușor
    1. Schimbă titlul aplicației.
    2. Schimbă textul de introducere.
    3. Modifică intervalul sliderului.

    ## Nivel mediu
    1. Afișează valoarea lui Delta.
    2. Adaugă mesaj pentru `a > 0`.
    3. Adaugă mesaj pentru `a < 0`.

    ## Nivel avansat
    Creează un meniu pentru:
    - funcție liniară
    - funcție de gradul al II-lea
    """)

with tab4:
    st.header("🧠 Quiz final")

    scor = 0

    q1 = st.radio(
        "1. Ce face st.slider()?",
        ["Afișează o poză", "Permite utilizatorului să aleagă o valoare", "Închide aplicația"],
        index=None
    )

    q2 = st.radio(
        "2. Ce reprezintă a, b și c în program?",
        ["Variabile", "Fișiere", "Pagini web"],
        index=None
    )

    q3 = st.radio(
        "3. Ce face linia y = a * x**2 + b * x + c?",
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
