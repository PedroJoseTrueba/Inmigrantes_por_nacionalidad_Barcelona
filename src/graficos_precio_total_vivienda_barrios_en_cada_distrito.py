import pandas as pd
import plotly.express as px
from src.limpieza_datos import compra_venta

def crear_grafico_precio_total_por_barrio(dataframe, distrito, tipo_datos, titulo):
    # Filtrar los datos para obtener solo los barrios del distrito especificado
    distrito_data = dataframe[dataframe['Nom_Districte'] == distrito]

    # Filtrar los datos para excluir los barrios que no tienen datos para el tipo de dato específico
    distrito_data = distrito_data.dropna(subset=[tipo_datos])

    # Calcular el precio total por barrio en el distrito especificado
    precio_total_por_barrio = distrito_data.groupby('Nom_Barri')[tipo_datos].mean().reset_index()

    # Crear el gráfico interactivo con Plotly Express
    if tipo_datos.endswith('_Milers'):
        y_label = 'Precio en miles de euros'
    elif tipo_datos.endswith('_Euros_m2'):
        y_label = 'Precio por m2 en euros'
    else:
        y_label = 'Eje Y'
        
    fig = px.bar(precio_total_por_barrio, x='Nom_Barri', y=tipo_datos, 
                 labels={tipo_datos: y_label,
                         'Nom_Barri': 'Barrio'},
                 title=titulo,
                 color='Nom_Barri',  # Usar 'Nom_Barri' como variable de color para que cada barra tenga un color diferente
                 color_discrete_sequence=px.colors.qualitative.Bold)  # Usar una paleta de colores diferente
    
    return fig

# Lista de distritos y tipos de datos
distritos = ['Ciutat Vella', 'Eixample', 'Sants-Montjuïc', 'Les Corts', 'Sarrià-Sant Gervasi', 
             'Gràcia', 'Horta-Guinardó', 'Nou Barris', 'Sant Andreu', 'Sant Martí']

tipos_datos = {'Total_Milers': 'Precio Total por Barrio en el distrito',
               'Nou_Milers': 'Precio de Viviendas Nuevas por Barrio en el distrito',
               'Usat_Milers': 'Precio de Viviendas Usadas por Barrio en el distrito',
               'Total_Euros_m2': 'Precio Total por Metro Cuadrado por Barrio en el distrito',
               'Nou_Euros_m2': 'Precio de Viviendas Nuevas por Metro Cuadrado por Barrio en el distrito',
               'Usat_Euros_m2': 'Precio de Viviendas Usadas por Metro Cuadrado por Barrio en el distrito'}

# Generar los gráficos para cada distrito y tipo de datos
figuras_por_distrito = {}
for distrito in distritos:
    for tipo_dato, titulo in tipos_datos.items():
        titulo = f"{titulo} {distrito}"  # Agregar el nombre del distrito al final del título
        figuras_por_distrito[titulo] = crear_grafico_precio_total_por_barrio(compra_venta, distrito, tipo_dato, titulo)