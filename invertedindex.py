import nltk
nltk.download('punkt')
import json
import re
from collections import defaultdict
from nltk.tokenize import word_tokenize


def leer_texto(path, lista):
    with open(path, 'r') as archivo:
        lineas = archivo.readlines()

    lista.extend([linea.strip() for linea in lineas])


def limpiar_texto(texto):
    texto = re.sub(r'[^\w\s]', '', texto)
    texto = texto.lower()
    return texto

def tokenizar(texto):
    texto = limpiar_texto(texto)
    return word_tokenize(texto)

def crear_indice_invertido(documentos):
    indice = defaultdict(list) 
    for doc_id, doc in enumerate(documentos):
        tokens = tokenizar(doc)
        for token in tokens:
            if doc_id not in indice[token]:  
                indice[token].append(doc_id)
    return indice

def remplazar_urls(indice, urls):
    nuevo_indice = defaultdict(list)
    for clave, lista_indices in indice.items():
        for idx in lista_indices:
            if idx < len(urls):
                nuevo_indice[clave].append(urls[idx])
    
    return nuevo_indice

  

indice = []
leer_texto('C:/Users/diegh/Universidad2doSemestre/certamen3LP/Certamen-3-Lenguaje-de-programaci-n/indice_invertido_sinstopwords.txt', indice)

urls = []
leer_texto('C:/Users/diegh/Universidad2doSemestre/certamen3LP/Certamen-3-Lenguaje-de-programaci-n/urls.txt', urls)

indice_invertido = crear_indice_invertido(indice)


indice_invertido = remplazar_urls(indice_invertido, urls)

print(indice_invertido)






indice_json = json.dumps(indice_invertido)
with open('inverted_index.json', 'w') as f:
    f.write(indice_json)

