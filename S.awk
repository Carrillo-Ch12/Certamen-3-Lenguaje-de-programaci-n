#!/bin/awk -f

BEGIN {
    FS = "\\|\\|"  # Separador de campos
    buffer = ""    # Buffer para acumular líneas
    previous_url = ""  # URL previa para detectar cambios

    # Archivos de salida
    urls_file = "urls.txt"
    contenido_file = "contenido.txt"

    # Asegurarse de que los archivos están vacíos al inicio
    system("> " urls_file)
    system("> " contenido_file)
}

{
    # Dividir la línea en campos usando el separador '||'
    split($0, fields, FS)

    # Concatenar los campos hasta el penúltimo como la URL completa
    url = fields[1]
    for (i = 2; i <= length(fields) - 1; i++) {
        url = url FS fields[i]
    }

    # Si la URL cambia, procesamos el buffer acumulado
    if (previous_url != "" && url != previous_url) {
        processBlock(buffer)
        buffer = ""  # Limpiar el buffer
    }

    # Acumular la línea en el buffer
    buffer = buffer (buffer == "" ? "" : "\n") $0

    # Actualizar la URL previa
    previous_url = url
}

# Procesar el último bloque al finalizar el archivo
END {
    if (buffer != "") {
        processBlock(buffer)
    }
}

# Función para procesar un bloque de texto acumulado
function processBlock(block) {
    # Dividir el bloque en líneas
    split(block, lines, "\n")

    # Procesar cada línea para extraer la URL y su contenido
    for (i in lines) {
        split(lines[i], fields, FS)

        # Concatenar la URL completa
        url = fields[1]
        for (j = 2; j <= length(fields) - 1; j++) {
            url = url FS fields[j]
        }

        # Reemplazar los separadores escapados (\|\|) con los originales (||)
        gsub("\\|\\|", "||", url)

        # El último campo es el contenido
        contenido = fields[length(fields)]

        # Escribir la URL y el contenido en los archivos de salida
        print url >> urls_file
        print contenido >> contenido_file
    }

    # Cerrar los archivos después de escribir para asegurar que se guarden los datos
    close(urls_file)
    close(contenido_file)
}
