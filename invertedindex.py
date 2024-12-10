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


def procesar_consultas(archivo_consultas, indice_invertido, urls):
    # Abrimos el archivo de consultas
    with open(archivo_consultas, 'r', encoding='utf-8') as f:
        consultas = f.readlines()

    # Procesar cada consulta
    for i, consulta in enumerate(consultas):
        consulta = consulta.strip()  # Limpiar posibles saltos de línea
        print(f"Procesando consulta: {consulta}")  # Para depuración

        # Limpiar y dividir la consulta en términos
        terminos = consulta.split()

        # Obtener los resultados de la intersección
        resultados = interseccionar_listas(terminos, indice_invertido)
        print(f"Resultados (índices de documentos): {resultados}")  # Para depuración

        # Si hay resultados, convertimos los índices en URLs
        if resultados:
            resultados_urls = [urls[doc_id] for doc_id in resultados]
            print(f"Documentos que contienen todos los términos (URLs): {resultados_urls}")  # Para depuración
        else:
            resultados_urls = []

        # Guardar los resultados en un archivo
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
        
indice = []
leer_texto('C:/Users/diegh/Universidad2doSemestre/certamen3LP/Certamen-3-Lenguaje-de-programaci-n/indice_invertido_sinstopwords.txt', indice)

urls = []
leer_texto('C:/Users/diegh/Universidad2doSemestre/certamen3LP/Certamen-3-Lenguaje-de-programaci-n/urls.txt', urls)

# Crear el índice invertido
indice_invertido = crear_indice_invertido(indice)


# Procesar las consultas y guardar los resultados
procesar_consultas('C:/Users/diegh/Universidad2doSemestre/certamen3LP/Certamen-3-Lenguaje-de-programaci-n/consultas.txt', indice_invertido, urls)


