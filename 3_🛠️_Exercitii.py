import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📈 2. Aplicație interactivă: Funcția de gradul al II-lea")

st.markdown("""
Vom folosi funcția:

### f(x) = ax² + bx + c

Din punct de vedere informatic:
- **a, b, c** sunt variabile
- valorile lor sunt alese de utilizator
- programul calculează graficul automat
""")

st.divider()

st.subheader("🟢 Pasul 1: INPUT - alegem valorile")

col1, col2, col3 = st.columns(3)

with col1:
    a = st.slider("Coeficientul a", -5.0, 5.0, 1.0, 0.5)

with col2:
    b = st.slider("Coeficientul b", -10.0, 10.0, 0.0, 0.5)

with col3:
    c = st.slider("Coeficientul c", -10.0, 10.0, 0.0, 0.5)

st.code("""
a = st.slider("Coeficientul a", -5.0, 5.0, 1.0, 0.5)
b = st.slider("Coeficientul b", -10.0, 10.0, 0.0, 0.5)
c = st.slider("Coeficientul c", -10.0, 10.0, 0.0, 0.5)
""", language="python")

st.divider()

if a == 0:
    st.error("Pentru funcția de gradul al II-lea, coeficientul a trebuie să fie diferit de 0.")
else:
    st.subheader("🟡 Pasul 2: PROCESARE - programul calculează")

    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c

    delta = b**2 - 4*a*c
    xv = -b / (2*a)
    yv = a * xv**2 + b * xv + c

    st.code("""
x = np.linspace(-10, 10, 400)
y = a * x**2 + b * x + c
delta = b**2 - 4*a*c
""", language="python")

    st.info("Programul calculează multe puncte ale funcției, apoi le unește într-un grafic.")

    st.divider()

    st.subheader("🔵 Pasul 3: OUTPUT - afișăm rezultatul")

    left, right = st.columns([2, 1])

    with left:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(x, y, label="f(x)")
        ax.scatter([xv], [yv], label="Vârful parabolei")
        ax.axhline(0, linewidth=1)
        ax.axvline(0, linewidth=1)
        ax.grid(True)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Graficul funcției de gradul al II-lea")
        ax.legend()
        st.pyplot(fig)

    with right:
        st.metric("a", a)
        st.metric("b", b)
        st.metric("c", c)
        st.metric("Delta", f"{delta:.2f}")
        st.metric("Vârful V", f"({xv:.2f}, {yv:.2f})")

    st.success(f"Funcția este: f(x) = {a}x² + {b}x + {c}")

    if a > 0:
        st.info("Pentru că a > 0, parabola este deschisă în sus.")
    else:
        st.warning("Pentru că a < 0, parabola este deschisă în jos.")

    if delta > 0:
        st.success("Delta > 0: funcția are două rădăcini reale.")
    elif delta == 0:
        st.success("Delta = 0: funcția are o rădăcină reală dublă.")
    else:
        st.warning("Delta < 0: funcția nu are rădăcini reale.")

    st.divider()

    st.subheader("🧑‍🏫 Întrebări pentru elevi")

    st.markdown("""
    1. Ce se întâmplă când modificăm valoarea lui **a**?
    2. Ce se întâmplă când **a** este negativ?
    3. Care este partea de input din aplicație?
    4. Care este partea de procesare?
    5. Care este output-ul?
    """)
