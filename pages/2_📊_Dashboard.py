import streamlit as st

st.title("📊 Dashboard")
st.write("Here I will show visualizations and data analysis.")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



# Datos de ejemplo
users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

# Convertir a DataFrame
data = []
for u in users:
    user_id, name, age, categories, spendings = u
    total_spent = sum(spendings)
    data.append([user_id, name.strip(), age, categories, spendings, total_spent])

df = pd.DataFrame(data, columns=['User ID', 'Name', 'Age', 'Fav Categories', 'Total Spendings', 'Total Spent'])

# Mostrar tabla
st.subheader("Usuarios y sus gastos")
st.dataframe(df)

# Gráfico: gasto total por usuario
st.subheader("Gasto total por usuario")
plt.figure(figsize=(10,5))
plt.bar(df['Name'], df['Total Spent'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.ylabel("Total Gastado")
plt.xlabel("Usuario")
plt.title("Gasto Total por Usuario")
st.pyplot(plt)