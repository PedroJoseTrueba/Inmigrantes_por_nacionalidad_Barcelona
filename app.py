import streamlit as st
import pandas as pd
import plotly_express as px

# Cargar el archivo CSV con el separador ;
df = pd.read_csv(r"/Users/pedrotruebaplaza/Desktop/materia_Triple_Ten/inmigrantes_por_pais_Barcelona/2022_pad_imm_mdbas_sexe_edat-q_nacionalitat-g (2).csv", sep=';')

st.header('Población de Barcelona')



hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para la población de Barcelona')
            
    # crear un histograma
    fig1 = px.histogram(df, x="EDAT_Q", histfunc="count", title="Distribución de edades quinquenales en la población inmigrante", labels={"EDAT_Q": "Grupo etario"})
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)
    
    
disp_button = st.button('Construir gráfico de dispersión') # crear un botón    

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para la población de Barcelona')
            
    # crear un gráfico de dispersión
    fig2 = px.scatter(df, x='EDAT_Q', y='Valor', color='Nom_Districte', title='Número de personas inmigrantes por edad quinquenal y distrito', labels={'Valor': 'Número de personas inmigrantes', 'EDAT_Q': 'Edad quinquenal', 'Nom_Districte': 'Distrito'})
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
    


