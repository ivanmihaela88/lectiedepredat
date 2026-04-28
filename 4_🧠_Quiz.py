import streamlit as st

st.title("🛠️ 3. Exerciții de programare")

st.markdown("""
Aceste exerciții sunt pentru ora de informatică. Elevii pot lucra individual sau pe grupe.
""")

st.divider()

st.header("🟢 Nivel ușor")

st.markdown("""
1. Schimbă titlul aplicației.
2. Schimbă textul de introducere.
3. Modifică intervalul sliderului pentru **a** de la `-5, 5` la `-10, 10`.

Rezolvare posibilă:
```python
a = st.slider("Coeficientul a", -10.0, 10.0, 1.0, 0.5)
```
""")

st.header("🟡 Nivel mediu")

st.markdown("""
1. Afișează valoarea lui Delta cu `st.metric()`.
2. Adaugă un mesaj pentru cazul `a > 0`.
3. Adaugă un mesaj pentru cazul `a < 0`.

Rezolvare posibilă:
```python
st.metric("Delta", delta)

if a > 0:
    st.success("Parabola este deschisă în sus.")
else:
    st.warning("Parabola este deschisă în jos.")
```
""")

st.header("🔴 Nivel avansat")

st.markdown("""
Creează un meniu din care utilizatorul să aleagă tipul funcției:

- funcție liniară: `f(x) = mx + n`
- funcție de gradul al II-lea: `f(x) = ax² + bx + c`

Indiciu:
```python
tip = st.selectbox("Alege tipul funcției", ["Liniară", "Gradul al II-lea"])
```
""")

st.divider()

st.info("Întrebare finală: Ce trebuie schimbat în cod ca aplicația să afișeze alt tip de grafic?")
