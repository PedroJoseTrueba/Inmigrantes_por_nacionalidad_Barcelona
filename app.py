import streamlit as st
import pandas as pd
import plotly_express as px

# Cargar el archivo CSV con el separador ;
df = pd.read_csv("inmigrantes_nacionalidad_edad_barcelona.csv", sep=';') 

st.header('Población de Barcelona')

st.write("""Los datos proporcionan información detallada sobre el número de personas inmigrantes según su nacionalidad (española, 
         de la Unión Europea o de otros países), sexo y edad quinquenal en la ciudad de Barcelona. Estos datos están desglosados por 
         diferentes variables, como el año del movimiento, el distrito y el barrio, así como por áreas estadísticas básicas y secciones censales. 
         La información incluye el número total de personas inmigrantes y detalles específicos sobre la nacionalidad, edad quinquenal y sexo de cada individuo. 
         Estos datos son esenciales para comprender la composición demográfica y las tendencias migratorias en Barcelona, y proporcionan información valiosa 
         para la planificación y la toma de decisiones en políticas públicas y servicios comunitarios.""")



hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para la población de Barcelona')
            
    # crear un histograma
    fig1 = px.histogram(df, x="EDAT_Q", histfunc="count", title="Distribución de edades quinquenales en la población inmigrante", labels={"EDAT_Q": "Grupo etario"})
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)
    
    # Texto descriptivo
    st.write("""El histograma muestra la distribución de las edades quinquenales en la población inmigrante de la ciudad de Barcelona. Cada barra representa un grupo de edad quinquenal, desde menores de 5 años hasta mayores de 90 años, como se detalla a continuación:

    Los grupos de edad quinquenales se definen de la siguiente manera:\n
    Edades:\n
    0: Menores de 5 años\n
    1: 5-9 años\n
    2: 10-14 años\n
    3: 15-19 años\n
    4: 20-24 años\n
    5: 25-29 años\n
    6: 30-34 años\n
    7: 35-39 años\n
    8: 40-44 años\n
    9: 45-49 años\n
    10: 50-54 años\n
    11: 55-59 años\n
    12: 60-64 años\n
    13: 65-69 años\n
    14: 70-74 años\n
    15: 75-79 años\n
    16: 80-84 años\n
    17: 85-89 años\n
    18: 90-94 años\n
    La altura de cada barra indica la cantidad de personas inmigrantes dentro de ese grupo de edad. Este gráfico proporciona una visión general de cómo se distribuye la población inmigrante en diferentes grupos de edad en la ciudad.""")
    
    
disp_button = st.button('Construir gráfico de dispersión') # crear un botón    

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para la población de Barcelona')
            
    # crear un gráfico de dispersión
    fig2 = px.scatter(df, x='EDAT_Q', y='Valor', color='Nom_Districte', title='Número de personas inmigrantes por edad quinquenal y distrito', labels={'Valor': 'Número de personas inmigrantes', 'EDAT_Q': 'Edad quinquenal', 'Nom_Districte': 'Distrito'})
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
    
    #descripcion del grafico
    st.write("""
    El gráfico de dispersión muestra el número de personas inmigrantes por edad quinquenal y distrito en la ciudad de Barcelona. 
    Cada punto en el gráfico representa un grupo de edad quinquenal y su correspondiente número de personas inmigrantes. 
    El eje x representa la edad quinquenal, mientras que el eje y representa el número de personas inmigrantes. 
    Los puntos están coloreados según el distrito al que pertenecen.

    Los grupos de edad quinquenales se definen de la siguiente manera:\n
    Edades:\n
    0: Menores de 5 años\n
    1: 5-9 años\n
    2: 10-14 años\n
    3: 15-19 años\n
    4: 20-24 años\n
    5: 25-29 años\n
    6: 30-34 años\n
    7: 35-39 años\n
    8: 40-44 años\n
    9: 45-49 años\n
    10: 50-54 años\n
    11: 55-59 años\n
    12: 60-64 años\n
    13: 65-69 años\n
    14: 70-74 años\n
    15: 75-79 años\n
    16: 80-84 años\n
    17: 85-89 años\n
    18: 90-94 años\n""")
    


