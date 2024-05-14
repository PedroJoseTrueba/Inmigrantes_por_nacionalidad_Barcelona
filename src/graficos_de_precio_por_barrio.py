from src.limpieza_datos import compra_venta
import pandas as pd
import plotly.express as px

def crear_grafico_precio_total_por_barrio(compra_venta):
    # Calcular el precio total por barrio
    precio_total_por_barrio = compra_venta.groupby('Nom_Barri')['Total_Milers'].mean().reset_index()
    
    # Filtrar los barrios sin datos
    precio_total_por_barrio = precio_total_por_barrio[precio_total_por_barrio['Total_Milers'].notnull()]
    
    # Crear el gráfico interactivo con Plotly Express
    fig = px.bar(precio_total_por_barrio, x='Nom_Barri', y='Total_Milers', 
                 labels={'Total_Milers': 'Precio Total (Miles de euros)', 'Nom_Barri': 'Barrio'},
                 )
    
    return fig

def crear_grafico_nou_milers_por_barrio(compra_venta):
    # Calcular el precio de viviendas nuevas por barrio
    nou_milers_por_barrio = compra_venta.groupby('Nom_Barri')['Nou_Milers'].mean().reset_index()
    
    # Filtrar los barrios sin datos
    nou_milers_por_barrio = nou_milers_por_barrio[nou_milers_por_barrio['Nou_Milers'].notnull()]
    
    # Crear el gráfico interactivo con Plotly Express
    fig = px.bar(nou_milers_por_barrio, x='Nom_Barri', y='Nou_Milers', 
                 labels={'Nou_Milers': 'Nou Milers (Miles de euros)', 'Nom_Barri': 'Barrio'},
                 )
    
    return fig

def crear_grafico_usat_milers_por_barrio(compra_venta):
    # Calcular el precio de viviendas usadas por barrio
    usat_milers_por_barrio = compra_venta.groupby('Nom_Barri')['Usat_Milers'].mean().reset_index()
    
    # Filtrar los barrios sin datos
    usat_milers_por_barrio = usat_milers_por_barrio[usat_milers_por_barrio['Usat_Milers'].notnull()]
    
    # Crear el gráfico interactivo con Plotly Express
    fig = px.bar(usat_milers_por_barrio, x='Nom_Barri', y='Usat_Milers', 
                 labels={'Usat_Milers': 'Usat Milers (Miles de euros)', 'Nom_Barri': 'Barrio'},
                 )
    
    return fig

def crear_grafico_total_euros_m2_por_barrio(compra_venta):
    # Calcular el precio total por metro cuadrado por barrio
    total_euros_m2_por_barrio = compra_venta.groupby('Nom_Barri')['Total_Euros_m2'].mean().reset_index()
    
    # Filtrar los barrios sin datos
    total_euros_m2_por_barrio = total_euros_m2_por_barrio[total_euros_m2_por_barrio['Total_Euros_m2'].notnull()]
    
    # Crear el gráfico interactivo con Plotly Express
    fig = px.bar(total_euros_m2_por_barrio, x='Nom_Barri', y='Total_Euros_m2', 
                 labels={'Total_Euros_m2': 'Precio Total (Euros por m²)', 'Nom_Barri': 'Barrio'},
                )
    
    return fig

def crear_grafico_nou_euros_m2_por_barrio(compra_venta):
    # Calcular el precio de viviendas nuevas por metro cuadrado por barrio
    nou_euros_m2_por_barrio = compra_venta.groupby('Nom_Barri')['Nou_Euros_m2'].mean().reset_index()
    
    # Filtrar los barrios sin datos
    nou_euros_m2_por_barrio = nou_euros_m2_por_barrio[nou_euros_m2_por_barrio['Nou_Euros_m2'].notnull()]
    
    # Crear el gráfico interactivo con Plotly Express
    fig = px.bar(nou_euros_m2_por_barrio, x='Nom_Barri', y='Nou_Euros_m2', 
                 labels={'Nou_Euros_m2': 'Precio de viviendas nuevas (Euros por m²)', 'Nom_Barri': 'Barrio'},
                 )
    
    return fig

def crear_grafico_usat_euros_m2_por_barrio(compra_venta):
    # Calcular el precio de viviendas usadas por metro cuadrado por barrio
    usat_euros_m2_por_barrio = compra_venta.groupby('Nom_Barri')['Usat_Euros_m2'].mean().reset_index()
    
    # Filtrar los barrios sin datos
    usat_euros_m2_por_barrio = usat_euros_m2_por_barrio[usat_euros_m2_por_barrio['Usat_Euros_m2'].notnull()]
    
    # Crear el gráfico interactivo con Plotly Express
    fig = px.bar(usat_euros_m2_por_barrio, x='Nom_Barri', y='Usat_Euros_m2', 
                 labels={'Usat_Euros_m2': 'Precio de viviendas usadas (Euros por m²)', 'Nom_Barri': 'Barrio'},
                 )
    
    return fig

# Invocar las funciones y mostrar los gráficos
grafico_1 = crear_grafico_precio_total_por_barrio(compra_venta)
grafico_2 = crear_grafico_nou_milers_por_barrio(compra_venta)
grafico_3 = crear_grafico_usat_milers_por_barrio(compra_venta)
grafico_4 = crear_grafico_total_euros_m2_por_barrio(compra_venta)
grafico_5 = crear_grafico_nou_euros_m2_por_barrio(compra_venta)
grafico_6 = crear_grafico_usat_euros_m2_por_barrio(compra_venta)





