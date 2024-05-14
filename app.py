import streamlit as st
from funciones_de_graficos import graficos_por_distrito, graficos_por_barrio
from graficos_precio_total_vivienda_barrios_en_cada_distrito import crear_grafico_precio_total_por_barrio, figuras_por_distrito
from graficos_de_caja import graficar_diagramas_cajas_todos_distritos 
from limpieza_datos import compra_venta

def main():
    # Mensaje introductorio para la aplicación
    st.write("""
# Explorando los Precios de Vivienda en Barcelona en el Año 2023

¡Bienvenido a esta aplicación de visualización de datos sobre los precios de la vivienda en Barcelona en el año 2023!

En esta aplicación, podrás explorar los precios de la vivienda en diferentes distritos y barrios de Barcelona. Selecciona una opción del menú a continuación para acceder a diferentes conjuntos de gráficos y obtener insights sobre el mercado inmobiliario de la ciudad.

Los datos utilizados en esta aplicación fueron extraídos de Open Data BCN, una plataforma que proporciona información pública de manera transparente y confiable. Esto asegura que los datos que estás viendo sean de alta calidad y estén disponibles para su reutilización por parte de la comunidad.

El mapa interactivo que se muestra a continuación representa los 10 distritos de Barcelona, cada uno compuesto por varios barrios. En total, Barcelona cuenta con 73 barrios numerados en el mapa del 1 al 73. Cada número en el mapa corresponde a un barrio específico de la ciudad.

¡Explora los datos y descubre insights sobre el mercado inmobiliario de Barcelona!
""")

    
    # Agregar la imagen al inicio de la página y hacerla más grande
    st.image("mapa_Barcelona_barrios_y_distritos_con_fondo_celeste.svg", width=800)

    # Opciones con radio buttons
    opcion = st.radio("Selecciona una opción:", 
                      ["Graficar precio de vivienda por distrito",
                       "Graficar precio de vivienda por barrio",
                       "Mostrar gráficos de precios por barrio en cada distrito",
                       "Mostrar variabilidad de los precios por distrito"])

    # Acciones basadas en la opción seleccionada
    if opcion == "Graficar precio de vivienda por distrito":
        figuras_distrito = graficos_por_distrito()
        for nombre_grafico, figura in figuras_distrito.items():
            st.subheader(nombre_grafico)
            st.plotly_chart(figura)

    elif opcion == "Graficar precio de vivienda por barrio":
        figuras_barrio = graficos_por_barrio()
        for nombre_grafico, figura in figuras_barrio.items():
            st.subheader(nombre_grafico)
            st.plotly_chart(figura)
    
    elif opcion == "Mostrar gráficos de precios por barrio en cada distrito":
        for nombre_grafico, figura in figuras_por_distrito.items():
            st.subheader(nombre_grafico)
            st.plotly_chart(figura)
            
    elif opcion == "Mostrar variabilidad de los precios por distrito":
        figuras_cajas = graficar_diagramas_cajas_todos_distritos(compra_venta)
        for columna, figura in figuras_cajas.items():
            st.plotly_chart(figura)

if __name__ == "__main__":
    main()


