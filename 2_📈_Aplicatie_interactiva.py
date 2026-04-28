import streamlit as st

st.title("📚 1. Teorie: Cum funcționează o aplicație interactivă")

st.markdown("""
## Ce este Streamlit?

**Streamlit** este o bibliotecă Python care ne permite să construim aplicații web rapid.

Nu trebuie să scriem HTML, CSS sau JavaScript. Putem crea interfețe folosind comenzi Python.

---

## Modelul aplicației

O aplicație interactivă are de obicei 3 pași:

### 1. INPUT
Utilizatorul introduce sau alege valori.

Exemplu:
```python
a = st.slider("Alege valoarea lui a", -5.0, 5.0, 1.0)
```

### 2. PROCESARE
Programul folosește valorile primite și calculează ceva.

Exemplu:
```python
y = a * x**2 + b * x + c
```

### 3. OUTPUT
Programul afișează rezultatul.

Exemplu:
```python
st.pyplot(fig)
```

---

## Întrebare pentru clasă

**Ce aplicații folosiți care reacționează la ce introduce utilizatorul?**

Răspunsuri posibile:
- Google Forms
- aplicații meteo
- calculatoare online
- jocuri
- aplicații de notițe
""")

st.success("Ideea-cheie: aplicația primește date, le prelucrează și afișează un rezultat.")
