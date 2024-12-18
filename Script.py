def cargar_stopwords():
    stopwords = [
        "a", "an", "and", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", 
        "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", 
        "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", 
        "has", "hasn't", "have", "haven't", "having", "he", "he’d", "he’ll", "he’s", "her", "here", "here’s", 
        "hereafter", "therein", "thereof", "there’s", "theirs", "them", "themselves", "to", "too", "under", "until", 
        "up", "very", "was", "wasn't", "we", "we’d", "we’ll", "we’re", "we’ve", "were", "weren’t", "what", "what’s", 
        "when", "when’s", "where", "where’s", "who", "who’s", "whom", "with", "won’t", "would", "wouldn't", "you", 
        "you’d", "you’ll", "you’re", "you’ve", "your", "yours"
    ]
    return set(word.lower() for word in stopwords)

def cargar_urls(archivo_urls):
    with open(archivo_urls, 'r') as f:
        urls = [linea.replace("\\|\\|", "||").strip() for linea in f]
    return urls

def arreglar_url(url):
    url = url.replace("||", "", 1)
    url = url.replace("||", ".")
    if not url.startswith("http://"):
        url = url.replace("http", "http://")
        url = url.replace(" ", "")
    return url.strip()

def remover_stopwords(archivo_entrada, archivo_salida, archivo_urls):
    stopwords = cargar_stopwords()
    urls = cargar_urls(archivo_urls)
    
    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w') as salida:
        for linea in entrada:
            clave, documento = linea.split(None, 1)
            palabra = clave.split()[0]

            if palabra.lower() not in stopwords:
                salida.write(linea)
    
    with open('urls.txt', 'w') as archivo_urls_limpias:
        for url in urls:
            url_arreglada = arreglar_url(url)
            archivo_urls_limpias.write(url_arreglada + '\n')

remover_stopwords('indice_invertido.txt', 'indice_invertido_sinstopwords.txt', 'urls.txt')
