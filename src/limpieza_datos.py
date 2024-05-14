import pandas as pd


# Leer el primer archivo CSV desde la URL
compra_venta = pd.read_csv('Datasets/est-mercat-immobiliari-compravenda-preu-total - est-mercat-immobiliari-compravenda-preu-total.csv')


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

print(compra_venta.info())

