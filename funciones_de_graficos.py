from limpieza_datos import compra_venta
import plotly.express as px
import graficos_de_precio_por_distrito 
import graficos_de_precio_por_barrio

def graficos_por_distrito():
    figuras_distrito = {}
    figuras_distrito['Precio de total de vivienda por Distrito'] = graficos_de_precio_por_distrito.crear_grafico_precio_total_por_distrito(compra_venta)
    figuras_distrito['Precio de vivienda nueva por Distrito'] = graficos_de_precio_por_distrito.crear_grafico_nou_por_distrito(compra_venta)
    figuras_distrito['Precio de vivienda usada por Distrito'] = graficos_de_precio_por_distrito.crear_grafico_usat_por_distrito(compra_venta)
    figuras_distrito['Precio del m2 por Distrito'] = graficos_de_precio_por_distrito.crear_grafico_precio_por_m2_por_distrito(compra_venta)
    figuras_distrito['Precio del m2  de vivienda nueva por Distrito'] = graficos_de_precio_por_distrito.crear_grafico_precio_por_m2_por_distrito_nuevo(compra_venta)
    figuras_distrito['Precio del m2  de vivienda usada por Distrito'] = graficos_de_precio_por_distrito.crear_grafico_precio_por_m2_por_distrito_usado(compra_venta)
    return figuras_distrito

def graficos_por_barrio():
    figuras_barrio = {}
    figuras_barrio['Precio Total por Barrio'] = graficos_de_precio_por_barrio.crear_grafico_precio_total_por_barrio(compra_venta)
    figuras_barrio['Precio de Viviendas Nuevas por Barrio'] = graficos_de_precio_por_barrio.crear_grafico_nou_milers_por_barrio(compra_venta)
    figuras_barrio['Precio de Viviendas Usadas por Barrio'] = graficos_de_precio_por_barrio.crear_grafico_usat_milers_por_barrio(compra_venta)
    figuras_barrio['Precio Total por Metro Cuadrado por Barrio'] = graficos_de_precio_por_barrio.crear_grafico_total_euros_m2_por_barrio(compra_venta)
    figuras_barrio['Precio de Viviendas Nuevas por Metro Cuadrado por Barrio'] = graficos_de_precio_por_barrio.crear_grafico_nou_euros_m2_por_barrio(compra_venta)
    figuras_barrio['Precio de Viviendas Usadas por Metro Cuadrado por Barrio'] = graficos_de_precio_por_barrio.crear_grafico_usat_euros_m2_por_barrio(compra_venta)
    return figuras_barrio
