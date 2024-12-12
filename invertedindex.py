import nltk
nltk.download('punkt')
import re
from collections import defaultdict
from nltk.tokenize import word_tokenize

def leer_indice_invertido(path):
    indice = defaultdict(list)
    with open(path, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split()
            if len(partes) > 1:  
                palabra = partes[0]
                ids = list(map(int, partes[1:]))  
                indice[palabra].extend(ids)
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

def procesar_consultas(archivo_consultas, indice_invertido, urls):
    with open(archivo_consultas, 'r', encoding='utf-8') as f:
        consultas = f.readlines()

    for i, consulta in enumerate(consultas):
        consulta = consulta.strip()
        print(f"Procesando consulta: {consulta}")  
        terminos = consulta.split()
        resultados = interseccionar_listas(terminos, indice_invertido)
        print(f"Resultados (índices de documentos): {resultados}")  
        if resultados:
            resultados_urls = [urls[doc_id] for doc_id in resultados if 0 <= doc_id < len(urls)]
            print(f"Documentos que contienen todos los términos (URLs): {resultados_urls}")  
        else:
            resultados_urls = []
        archivo_resultados = f"resultados_consulta_{i+1}.txt"
        with open(archivo_resultados, 'w', encoding='utf-8') as out_file:
            out_file.write(f"Consulta: {consulta}\n")
            if resultados_urls:
                out_file.write(f"Documentos que contienen todos los términos (URLs):\n")
                for url in resultados_urls:
                    out_file.write(f"{url}\n")
            else:
                out_file.write("No se encontraron documentos que contengan todos los términos.\n")
        print(f"Resultados de la consulta {i+1} guardados en: {archivo_resultados}")       

indice_invertido = leer_indice_invertido('C:/Users/diegh/Universidad2doSemestre/certamen3LP/Certamen-3-Lenguaje-de-programaci-n/indice_invertido_sinstopwords.txt')

urls = []
with open('C:/Users/diegh/Universidad2doSemestre/certamen3LP/Certamen-3-Lenguaje-de-programaci-n/urls.txt', 'r', encoding='utf-8') as archivo:
    urls = [linea.strip() for linea in archivo]

procesar_consultas('C:/Users/diegh/Universidad2doSemestre/certamen3LP/Certamen-3-Lenguaje-de-programaci-n/consultas.txt', indice_invertido, urls)
