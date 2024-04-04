import requests
import pandas as pd

url = "https://opendata-ajuntament.barcelona.cat/data/api/action/datastore_search?resource_id=b8b7c184-6d9c-4ea0-8e67-631f452cc75c"
response = requests.get(url)
data = response.json()

# Obtener los registros de la respuesta
records = data['result']['records']

# Convertir los registros a un DataFrame de pandas
df = pd.DataFrame(records)


print(df.head())
