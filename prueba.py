frase1 = "Excelente en su area, su muerte es una enorme pérdida y debería ser luto nacional"
frase1 = frase1.lower()

CPalabras_Positivas = 0
CPalabras_Neutras = 0
CPalabras_Negativas = 0


palabras_positivas = ["excelente","gran", "positivo"]
palabras_negativas = ["muerte", "luto"]
palabras_neutras = ["pérdida"]

palabras_clave = palabras_positivas + palabras_negativas + palabras_neutras


for palabra in frase1.split():
    palabra = palabra.strip(",.")
    if palabra in palabras_positivas:
        CPalabras_Positivas += 1
    elif palabra in palabras_negativas:
        CPalabras_Negativas += 1
    elif palabra in palabras_neutras:
        CPalabras_Neutras += 1

s = (CPalabras_Positivas, CPalabras_Neutras, CPalabras_Negativas)

print(s)

w = tuple([1 if palabra in frase1 else 0 for palabra in palabras_clave])

print(w)
