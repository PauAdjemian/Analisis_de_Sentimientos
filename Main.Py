def verificar_palabras(frase, palabras):
    return [palabra for palabra in palabras if palabra in frase]

def palabras_clave(frase, palabras):
    vector=[]
    for palabra in palabras:
        if(palabra in frase):
            vector.append(1)
        else:
            vector.append(0)
    return vector

lista = ["gato","mono", "bueno", "con"]
frase = "El gato con botas es bueno con la espada"
palabras_en_frase = verificar_palabras(frase, lista)
print(palabras_en_frase)
vector = palabras_clave(frase, lista)
print(vector)

