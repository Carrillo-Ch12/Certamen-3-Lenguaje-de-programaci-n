def cargar_stopwords():
    # Lista de stopwords generada previamente
    stopwords = [
        "a", "an", "and", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he’d", "he’ll", "he’s", "her", "here", "here’s", "hereafter", "therein", "thereof", "there’s", "theirs", "them", "themselves", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we’d", "we’ll", "we’re", "we’ve", "were", "weren’t", "what", "what’s", "what’ll", "what’s", "what’s", "when", "when’s", "when", "where", "where’s", "where", "who", "who’s", "who’s", "whom", "whom", "with", "won’t", "would", "wouldn't", "you", "you’d", "you’ll", "you’re", "you’ve", "your", "yours"
    ]
    return set(word.lower() for word in stopwords)  # Convertir todas las stopwords a minúsculas

def remover_stopwords(archivo_entrada, archivo_salida):
    stopwords = cargar_stopwords()
    
    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w') as salida:
        for linea in entrada:
            palabras = linea.split()
            palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stopwords]
            
            # Imprimir stopwords removidas (opcional)
            stopwords_removidas = set(palabras) - set(palabras_filtradas)
            if stopwords_removidas:  # Solo imprimir si se han removido stopwords
                print(f"Stopwords removidas: {stopwords_removidas}")
            
            # Escribir línea filtrada
            salida.write(' '.join(palabras_filtradas) + '\n')

# Uso
remover_stopwords('contenido.txt', 'indice_invertido_sinstopwords.txt')
