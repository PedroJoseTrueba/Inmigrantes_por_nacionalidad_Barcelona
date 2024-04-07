import pandas as pd
import plotly.express as px
from limpieza_datos import compra_venta



def crear_grafico_precio_total_por_distrito(compra_venta):
    # Calcular el precio total por distrito
    precio_total_por_distrito = compra_venta.groupby('Nom_Districte')['Total_Milers'].mean().reset_index()

    # Crear el gráfico interactivo con Plotly Express
    fig = px.bar(precio_total_por_distrito, x='Nom_Districte', y='Total_Milers', 
                 labels={'Total_Milers': 'Precio Total (Miles de euros)', 'Nom_Districte': 'Distrito'},
                 title='Precio Total de vivienda por Distrito')

    return fig

def crear_grafico_nou_por_distrito(compra_venta):
    # Calcular el precio Nou por distrito
    precio_nou_por_distrito = compra_venta.groupby('Nom_Districte')['Nou_Milers'].mean().reset_index()

    # Crear el gráfico interactivo con Plotly Express
    fig = px.bar(precio_nou_por_distrito, x='Nom_Districte', y='Nou_Milers', 
                 labels={'Nou_Milers': 'Precio Nou (Miles de euros)', 'Nom_Districte': 'Distrito'},
                 title='Precio de vienda nueva por Distrito', color_discrete_sequence=['green'])

    return fig

def crear_grafico_usat_por_distrito(compra_venta):
    # Calcular el precio Usat por distrito
    precio_usat_por_distrito = compra_venta.groupby('Nom_Districte')['Usat_Milers'].mean().reset_index()

    # Crear el gráfico interactivo con Plotly Express
    fig = px.bar(precio_usat_por_distrito, x='Nom_Districte', y='Usat_Milers', 
                 labels={'Usat_Milers': 'Precio Usat (Miles de euros)', 'Nom_Districte': 'Distrito'},
                 title='Precio de vivienda usada por Distrito', color_discrete_sequence=['pink'])

    return fig

def crear_grafico_precio_por_m2_por_distrito(compra_venta):
    # Calcular el precio por m2 por distrito
    precio_por_m2_por_distrito_total = compra_venta.groupby('Nom_Districte')[['Total_Euros_m2']].mean().reset_index()


    # Crear el gráfico interactivo con Plotly Express
    fig = px.bar(precio_por_m2_por_distrito_total, x='Nom_Districte', y=['Total_Euros_m2'], 
                 labels={'value': 'Precio (Euros por m2)','Nom_Districte': 'Distrito'},
                 title='Precio de m2 por Distrito', color_discrete_sequence=['red'])
    
    return fig


def crear_grafico_precio_por_m2_por_distrito_nuevo(compra_venta):
    # Calcular el precio por m2 por distrito
    precio_por_m2_por_distrito_nuevo = compra_venta.groupby('Nom_Districte')[['Nou_Euros_m2']].mean().reset_index()


    # Crear el gráfico interactivo con Plotly Express
    fig = px.bar(precio_por_m2_por_distrito_nuevo, x='Nom_Districte', y=['Nou_Euros_m2'], 
                 labels={'value': 'Precio (Euros por m2)', 'Nom_Districte': 'Distrito'},
                 title='Precio de m2 de vivienda nueva por Distrito', color_discrete_sequence=['yellow'])
    
    return fig

def crear_grafico_precio_por_m2_por_distrito_usado(compra_venta):
    # Calcular el precio por m2 por distrito
    precio_por_m2_por_distrito_usado = compra_venta.groupby('Nom_Districte')[['Usat_Euros_m2']].mean().reset_index()


    # Crear el gráfico interactivo con Plotly Express
    fig = px.bar(precio_por_m2_por_distrito_usado, x='Nom_Districte', y=['Usat_Euros_m2'], 
                 labels={'value': 'Precio (Euros por m2)', 'Nom_Districte': 'Distrito'},
                 title='Precio de m2 de vivienda usada por Distrito', color_discrete_sequence=['orange'])
    
    return fig






