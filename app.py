from limpieza_datos import compra_venta
import streamlit as st
import pandas as pd
import graficos_de_precio_por_distrito 
    

def main():
    # Título de la aplicación
    st.title('Visualización de precios de vivienda por distrito')

    # Crear los gráficos
    fig_precio_total = graficos_de_precio_por_distrito.crear_grafico_precio_total_por_distrito(compra_venta)
    fig_nou = graficos_de_precio_por_distrito.crear_grafico_nou_por_distrito(compra_venta)
    fig_usat = graficos_de_precio_por_distrito.crear_grafico_usat_por_distrito(compra_venta)
    fig_precio_por_m2 = graficos_de_precio_por_distrito.crear_grafico_precio_por_m2_por_distrito(compra_venta)
    fig_precio_por_m2_nuevo = graficos_de_precio_por_distrito.crear_grafico_precio_por_m2_por_distrito_nuevo(compra_venta)
    fig_precio_por_m2_usado = graficos_de_precio_por_distrito.crear_grafico_precio_por_m2_por_distrito_usado(compra_venta)

    # Mostrar los gráficos en la aplicación
    st.plotly_chart(fig_precio_total)
    st.plotly_chart(fig_nou)
    st.plotly_chart(fig_usat)
    st.plotly_chart(fig_precio_por_m2)
    st.plotly_chart(fig_precio_por_m2_nuevo)
    st.plotly_chart(fig_precio_por_m2_usado)

if __name__ == "__main__":
    main()
