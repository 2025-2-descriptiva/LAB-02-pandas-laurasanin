"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    # Leer el archivo TSV
    df = pd.read_csv("files/input/tbl1.tsv", sep="\t")

    # Agrupar por 'c0' y concatenar los valores de 'c4' separados por ','
    resultado = (
        df.groupby("c0")["c4"]
        .apply(lambda x: ",".join(sorted(x)))  # Ordena y une los valores
        .reset_index() # Reinicia el índice para obtener un DataFrame limpio
    )

    return resultado

print(pregunta_11())
