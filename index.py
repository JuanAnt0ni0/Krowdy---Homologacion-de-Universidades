import pandas as pd
from fuzzywuzzy import fuzz, process
import json

# Lectura de los archivos csv y json
instituciones = pd.read_csv('input/instituciones_educativas.csv', encoding='utf-8')
universidades = pd.read_json('input/universidades.json', encoding='utf-8')

# Definición de la función de homologación
def homologar(univ):
    match = process.extractOne(univ, universidades['Nombre '], scorer=fuzz.token_sort_ratio)
    return match[0] if match[1] >= 90 else univ

# Aplicación de la función de homologación a la columna 'value' de instituciones
instituciones['universidad homologada'] = instituciones['value'].apply(homologar)

# Generación del archivo universidades_homologadas.csv
instituciones[['candidateId', 'value', 'universidad homologada']].to_csv('output/universidades_homologadas.csv', index=False, encoding='utf-8')

# Generación del archivo sinonimo_universidades.json
sinonimos = []
for nombre in universidades['Nombre ']:
    lista_sinonimos = process.extract(nombre, universidades['Nombre '], scorer=fuzz.token_sort_ratio)
    lista_sinonimos = [s[0] for s in lista_sinonimos if s[0] != nombre and s[1] >= 90]
    if len(lista_sinonimos) > 0:
        sinonimos.append({'nombre_universidad': nombre, 'sinonimos': lista_sinonimos})

with open('output/sinonimo_universidades.json', 'w', encoding='utf-8') as f:
    json.dump(sinonimos, f)