import streamlit as st
import plotly.graph_objects as go
from src.limpieza_datos import compra_venta

def graficar_diagrama_caja_bigotes(df, columna, titulo):
    """
    Genera un gráfico de caja y bigotes para una columna específica del DataFrame.
    
    Parámetros:
        - df: DataFrame que contiene los datos.
        - columna: Nombre de la columna para la cual se generará el gráfico.
        
    Retorna:
        - fig: Objeto de figura Plotly.
    """
    # Filtrar filas donde la columna especificada no sea nula
    df_filtered = df.dropna(subset=[columna])

    # Determinar la etiqueta del eje y según el tipo de datos
    if columna.endswith('_Milers'):
        y_label = 'Precio en miles de euros'
    elif columna.endswith('_Euros_m2'):
        y_label = 'Precio por m2 en euros'
    else:
        y_label = 'Eje Y'

    # Crear el gráfico de caja y bigotes
    fig = go.Figure()
    for distrito, data in df_filtered.groupby('Nom_Districte'):
        fig.add_trace(go.Box(y=data[columna], name=distrito))

    # Configurar el diseño del gráfico
    fig.update_layout(
        title= titulo,
        xaxis_title="Distrito",
        yaxis_title=y_label
    )

    return fig

def graficar_diagramas_cajas_todos_distritos(df):
    """
    Genera gráficos de caja y bigotes para cada columna específica del DataFrame.
    
    Parámetros:
        - df: DataFrame que contiene los datos.
        
    Retorna:
        - figuras: Un diccionario que contiene objetos de figura Plotly para cada columna.
    """
    tipos_datos_titulo = {
        'Total_Milers': 'Variabilidad del Precio de todas las Viviendas por distrito',
        'Nou_Milers': 'Variabilidad del Precio de Viviendas Nuevas por distrito',
        'Usat_Milers': 'Variabilidad del Precio de Viviendas Usadas por distrito',
        'Total_Euros_m2': 'Variabilidad del Precio de todas las viviendas por Metro Cuadrado en cada distrito',
        'Nou_Euros_m2': 'Variabilidad del Precio de Viviendas Nuevas por Metro Cuadrado en cada distrito',
        'Usat_Euros_m2': 'Variabilidad del Precio de Viviendas Usadas por Metro Cuadrado en cada distrito'
    }
    
    figuras = {}
    
    distritos = ['Ciutat Vella', 'Eixample', 'Sants-Montjuïc', 'Les Corts', 'Sarrià-Sant Gervasi', 
                 'Gràcia', 'Horta-Guinardó', 'Nou Barris', 'Sant Andreu', 'Sant Martí']
    
    for distrito in distritos:
        for columna, titulo in tipos_datos_titulo.items():
            figuras[columna] = graficar_diagrama_caja_bigotes(df, columna, titulo)
    
    return figuras

# Ejemplo de uso
figuras_diagramas_cajas = graficar_diagramas_cajas_todos_distritos(compra_venta)