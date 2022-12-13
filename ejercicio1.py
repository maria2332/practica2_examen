"""
Nota:
• Los signos de libra por sí solos no cuentan, por ejemplo: la cadena "#" devolvería una matriz vacía.
• Si una palabra está precedida por más de un hashtag, solo cuenta el último hashtag
(por ejemplo, "##alot" devolvería ["alot"])
• Los hashtags no pueden estar en medio de una palabra (por ejemplo, "hashtag en #línea" devuelve una matriz vacía)
• Los hashtags deben preceder a los caracteres alfabéticos (por ejemplo, "#120398" o "#?" no son válidos)
Entrada: cadena de palabras, donde algunas palabras pueden contener un hashtag.
Salida: matriz de cadenas que tenían el prefijo del hashtag, pero que no contienen el hashtag.
"""

from ast import main 

def checkio(text):
    lista = []
    for i in range(len(text)):
        if text[i] == "#":
            palabra = text[i+1:]
            if palabra[0].isalpha():
                lista.append(palabra)
    return lista

print(checkio("Hello #6hola3r4"))

if __name__ == "__main__":
    main()
