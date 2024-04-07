import pandas as pd

# URL del primer archivo CSV
url_csv_1 = 'https://opendata-ajuntament.barcelona.cat/data/es/dataset/est-mercat-immobiliari-compravenda-preu-total/resource/5a86c311-4363-4a20-a1e7-fbb867659a3f/download/est-mercat-immobiliari-compravenda-preu-total.csv'

# URL del segundo archivo CSV
url_csv_2 = 'https://opendata-ajuntament.barcelona.cat/data/es/dataset/est-mercat-immobiliari-lloguer-mitja-mensual/resource/8148fe53-6bb4-42ca-98df-93e6b723dca9/download/est-mercat-immobiliari-lloguer-mitja-mensual.csv'

# Leer el primer archivo CSV desde la URL
compra_venta = pd.read_csv(url_csv_1)

# Leer el segundo archivo CSV desde la URL
alquiler = pd.read_csv(url_csv_2)

print(compra_venta.sample(10))
#Convertir trimestre y año a datetime
#compra_venta['Any'] = pd.to_datetime(compra_venta['Any'])

#Eliminar  la columna Trimestre
compra_venta = compra_venta.drop(columns=['Trimestre'])

# Convertir la columna 'Codi_Districte' a tipo str
compra_venta['Codi_Districte'] = compra_venta['Codi_Districte'].astype(str)
# Convertir la columna 'Codi_Barri' a tipo str
compra_venta['Codi_Barri'] = compra_venta['Codi_Barri'].astype(str)


#Reemplazar valores ausentes en Valor por None
compra_venta['Valor'] = compra_venta['Valor'].replace('--', None)

# Crear nuevas columnas para cada tipo de precio
compra_venta['Total_Milers'] = compra_venta.loc[compra_venta['Preu_mitja_habitatge'] == 'Total. Milers d\'euros', 'Valor']
compra_venta['Nou_Milers'] = compra_venta.loc[compra_venta['Preu_mitja_habitatge'] == 'Nou. Milers d\'euros', 'Valor']
compra_venta['Usat_Milers'] = compra_venta.loc[compra_venta['Preu_mitja_habitatge'] == 'Usat. Milers d\'euros', 'Valor']
compra_venta['Total_Euros_m2'] = compra_venta.loc[compra_venta['Preu_mitja_habitatge'] == 'Total. Euros/m2 construït', 'Valor']
compra_venta['Nou_Euros_m2'] = compra_venta.loc[compra_venta['Preu_mitja_habitatge'] == 'Nou. Euros/m2 construït', 'Valor']
compra_venta['Usat_Euros_m2'] = compra_venta.loc[compra_venta['Preu_mitja_habitatge'] == 'Usat. Euros/m2 construït', 'Valor']

compra_venta.info()

print(compra_venta.sample(10))

# Convertir las columnas a tipo numérico
compra_venta[['Total_Milers', 'Nou_Milers', 'Usat_Milers', 'Total_Euros_m2', 'Nou_Euros_m2', 'Usat_Euros_m2']] = compra_venta[['Total_Milers', 'Nou_Milers', 'Usat_Milers', 'Total_Euros_m2', 'Nou_Euros_m2', 'Usat_Euros_m2']].apply(pd.to_numeric, errors='coerce')

# Agrupar las filas por barrio y distrito y calcular los promedios
compra_venta_agrupado = compra_venta.groupby(['Nom_Districte', 'Nom_Barri']).agg({
    'Total_Milers': 'mean',
    'Nou_Milers': 'mean',
    'Usat_Milers': 'mean',
    'Total_Euros_m2': 'mean',
    'Nou_Euros_m2': 'mean',
    'Usat_Euros_m2': 'mean'
}).reset_index()

# Mostrar el DataFrame resultante
print(compra_venta_agrupado)





#cambiar a 

# Eliminar la columna del trimestre
#df = compra_venta.drop(columns=['Trimestre'])

# Convertir la columna 'Any' a tipo datetime
#compra_venta['Any'] = pd.to_datetime(df['Any'])

# Eliminar filas con valores no numéricos en la columna 'Valor' y convertirlos a None
#compra_venta['Valor'] = pd.to_numeric(compra_venta['Valor'], errors='coerce')

# Agrupar por año y calcular el promedio del valor del precio de la vivienda
#df_promedio_por_año = compra_venta.groupby(compra_venta['Any'].dt.year)['Valor'].mean()

# Mostrar el resultado
#print(df_promedio_por_año)