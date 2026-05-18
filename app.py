import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'PESO (kg)': [7.2, 8.5, 9.8, 6.5, 7.5, 10.1, 11.0, 11.1, 11.0, 11.2, 11.3, 11.4, 11.7, 12.0, 12.9, 12.9, 10.3, 9.7, 10.8, 11.0, 10.2, 6.5, 10.5, 6.3, 7.3, 7.5, 7.9, 8.2],
    'ALTURA (cm)': [50, 66, 73, 72, 81, 73, 66, 75, 70, 75, 69, 76, 69, 75, 64, 55, 76, 71, 64, 78, 70, 74, 72, 77, 51, 62, 60, 70],
    'VELOCIDAD (m/s)': [10.2, 10.3, 10.2, 16.4, 18.8, 19.7, 15.6, 21.2, 22.6, 19.9, 24.2, 21.0, 21.3, None, 22.2, 33.8, 27.4, 25.7, 24.9, 23.1, 31.7, 36.3, 38.3, 42.6, 55.4, None, 58.3, None],
    'COLOR': ['Blanco', 'Amarillo', 'Verde', 'Verde', 'Verde', 'Verde', 'Blanco', 'Amarillo', 'Verde', 'Blanco', 'Amarillo', 'Verde', 'Verde', 'Amarillo', 'Amarillo', 'Amarillo', 'Amarillo', 'Verde', 'Verde', 'Azul', 'Amarillo', 'Verde', 'Verde', 'Verde', 'Blanco', 'Verde', 'Amarillo', 'Verde']
}

df = pd.DataFrame(data)

st.title("Analizador Estadístico")

columna = st.sidebar.selectbox("Selecciona la columna a analizar", df.columns)

if st.button("Calcular"):
    
    df_limpio = df[columna].dropna()
    
    f_abs = df_limpio.value_counts().sort_index()
    f_rel = df_limpio.value_counts(normalize=True).sort_index()
    f_acu = f_abs.cumsum()
    
    st.header("1. Gráfica de Barras (Frecuencia Absoluta)")
    fig1, ax1 = plt.subplots()
    ax1.bar(f_abs.index.astype(str), f_abs.values, color="skyblue", edgecolor="black")
    ax1.set_ylabel("Conteo")
    st.pyplot(fig1)
    st.write("**Descripción:** Cuenta cuántas veces aparece cada dato en la columna.")
    
    st.header("2. Diagrama de Pastel (Frecuencia Relativa)")
    fig2, ax2 = plt.subplots()
    ax2.pie(f_rel.values, labels=f_rel.index.astype(str), autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')
    st.pyplot(fig2)
    st.write("**Descripción:** Muestra el porcentaje que representa cada dato respecto al total.")
    
    st.header("3. Frecuencia Acumulada")
    fig3, ax3 = plt.subplots()
    ax3.plot(f_acu.index.astype(str), f_acu.values, marker='o', color="green", linestyle="-")
    ax3.set_ylabel("Suma Acumulada")
    st.pyplot(fig3)
    st.write("**Descripción:** Suma progresiva de los conteos desde el menor valor al mayor.")
    
    st.header("4. Polígono de Frecuencias")
    fig4, ax4 = plt.subplots()
    ax4.plot(f_abs.index.astype(str), f_abs.values, marker='o', color="red", linestyle="-")
    ax4.set_ylabel("Conteo")
    st.pyplot(fig4)
    st.write("**Descripción:** Línea continua que une las frecuencias para ver la tendencia de los datos.")
    
    st.header("5. Medidas de Tendencia Central")
    
    if pd.api.types.is_numeric_dtype(df_limpio):
        media = df_limpio.mean()
        mediana = df_limpio.median()
        
        try:
            moda = df_limpio.mode()[0]
        except:
            moda = "No hay moda"
            
        st.success(f"**Media:** {media:.2f}")
        st.write("**Descripción:** Sumar todos los datos y dividir el resultado entre el total de elementos.")
        
        st.success(f"**Mediana:** {mediana:.2f}")
        st.write("**Descripción:** Ordenar los datos de menor a mayor y seleccionar el valor del centro.")
        
        st.success(f"**Moda:** {moda}")
        st.write("**Descripción:** Identificar el dato que más veces se repite en la lista.")
    else:
        try:
            moda = df_limpio.mode()[0]
        except:
            moda = "No hay moda"
        st.warning("La columna seleccionada es de texto. No se puede calcular Media ni Mediana.")
        st.success(f"**Moda:** {moda}")
        st.write("**Descripción:** Identificar el dato que más veces se repite en la lista.")