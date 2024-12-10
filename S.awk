#!/bin/awk -f

BEGIN {
    FS = "\\|\\|"  # Separador de campos
    buffer = ""    # Buffer para acumular líneas
}

{
    # Acumular las líneas, respetando los saltos de línea
    buffer = buffer $0

    # Si encontramos una línea vacía (indica un bloque finalizado), procesamos el buffer
    if (NF == 0) {
        processBlock(buffer)
        buffer = ""  # Limpiar el buffer para el siguiente bloque
    }
}

# Procesar el último bloque (si no hay línea vacía final)
END {
    if (buffer != "") {
        processBlock(buffer)
    }
}

# Función para procesar un bloque de texto acumulado
function processBlock(block) {
    # Dividir el bloque en campos según el separador '||'
    split(block, fields, FS)

    # Concatenar todos los campos hasta el penúltimo como URL
    url = fields[1]
    for (i = 2; i < length(fields); i++) {
        url = url FS fields[i]
    }

    # El último campo será el contenido
    contenido = fields[length(fields)]

    # Imprimir URL y contenido
    print contenido
}
