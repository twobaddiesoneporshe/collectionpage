import streamlit as st

st.title("Rina's Collection Page 🩷")
st.write("mostly stan skz and xdiz!! ⋆. 𐙚 ˚❀⋆.ೃ࿔*:･")
st.write("Rafa Fitrina, Kelas X-C")

st.write("SKZ Maxident Era 💗") 
st.image("IMG_0350.jpeg") 

st.write("Glitch Mode 💿")
st.image("IMG_0353.jpeg")

st.write("Today’s mail 💌💗")
st.image("IMG_0354.jpeg")

st.write("Seungmin Rockstar Era🤘🏻") 
st.image("IMG_0365.jpeg") 

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")

