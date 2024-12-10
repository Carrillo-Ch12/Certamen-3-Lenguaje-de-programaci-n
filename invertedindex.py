import nltk
nltk.download('punkt')
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

def interseccionar_listas(terminos, indice, i=0):
    if i == len(terminos):  
        return set(range(len(indice))) 

    termino = terminos[i]
    if termino in indice:  
        documentos_termino = set(indice[termino])
        return documentos_termino & interseccionar_listas(terminos, indice, i + 1) 
    else:
        return set() 

indice = []
leer_texto('C:/Users/diegh/Universidad2doSemestre/certamen3LP/Certamen-3-Lenguaje-de-programaci-n/indice_invertido_sinstopwords.txt', indice)

urls = []
leer_texto('C:/Users/diegh/Universidad2doSemestre/certamen3LP/Certamen-3-Lenguaje-de-programaci-n/urls.txt', urls)

indice_invertido = crear_indice_invertido(indice)

consulta = input("Introduce los términos de búsqueda separados por espacio: ")
terminos = consulta.split()

resultados = interseccionar_listas(terminos, indice_invertido)


resultados_urls = [urls[doc_id] for doc_id in resultados]

print(f"Documentos que contienen todos los términos (URLs): {resultados_urls}")


