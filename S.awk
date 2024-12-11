#!/bin/awk -f

BEGIN {
    FS = "\\|\\|" 
    OFS = " "
    buffer = ""
    URL = ""
    ID_documento = 0
    indice = "indice_invertido.txt"
    system("> urls.txt")
    system("> " indice)
}

{
    split($0, fields, FS)
    url = fields[1]
    for (i = 2; i <= length(fields) - 1; i++) {
        url = url FS fields[i]
    }
    if (URL != "" && url != URL) {
        procesarContenido(buffer, URL)
        buffer = "" 
    }
    buffer = buffer (buffer == "" ? "" : " ") fields[length(fields)]
    print url >> "urls.txt"
    URL = url
}

END {
    if (buffer != "") {
        procesarContenido(buffer, URL)
    }
    for (clave in indice_invertido) {
        split(clave, partes, SUBSEP) 
        palabra = partes[1]
        doc = partes[2]
        documentos[palabra] = documentos[palabra] (documentos[palabra] == "" ? "" : OFS) doc
    }
    for (palabra in documentos) {
        print palabra, documentos[palabra] >> indice
    }
}

function procesarContenido(texto, url) {
    ID_documento++ 
    gsub(/[[:punct:]]/, "", texto) 
    texto = tolower(texto)  
    split(texto, palabras, /[[:space:]]+/)
    for (i in palabras) {
        palabra = palabras[i]
        if (palabra != "") {
            clave = palabra SUBSEP ID_documento
            indice_invertido[clave] = 1
        }
    }
}
