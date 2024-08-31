# Lista de comentarios
comments = [
    """Ser Sabio para ayudar a los demás es el mejor regalo que Dios nos ha dado en esta vida, y tú lo estas sabiendo utilizar muy bien buen video y muy detallado, y excelente tu enseñanza sigue así y que se te siga dotando de muuuucha mas sabiduría para seguirnos enseñando de todo lo necesario, sigue así que lo estás haciendo muy bien, felicitaciones desde Sabaneta de Barinas, Venezuela.""",
    """Muy buen video, yo tengo conocimientos de js avanzados oero despues del curso jamas los n he practicado y parecen mas engorrosos que los que tu enseñas. Hoy estoy retomando todos esos conocimientos que he olvidado y me siven mas los tuyos que los del curso de la facultad. Saludos desde argentina, maestro.""",
    "Que bueno los explicas bien nose realmente nada de programacion pero con tus videos aprendo mas..!", 
    "Muy buen video seria genial si hubiera uno igual para cada lenguaje de programacion.", 
    """Hola Programador X, me presento, soy XC. Me encató el video, la verdad es bastante bueno (muy buans técnicas de edición por cierto), verás soy un pequeño youtuber y un aficionado al Hardware y la programación... Bueno llendo al grano, me suscríbo a tu canal y dejo mi grandisio like (ya activé la campanita), gracias por la ayuda (y un poco de refresco de memoria) un abrazo grande y un saludo! :D""",
    "La verdad ví muchos vídeo y se me hace difícil aprender ya que soy nuevo en esto, pero con tus vídeos de me hace mal fácil y entiendo mucho tu forma de explicar, sos muy bueno gracias",
    "Me encanta como Xavi en cada vídeo se esmera en ser muy creativo! Gracias Xavi, buen vídeo!", 
    "Que buenos videos Programador X, puntuales, dinamicos y faciles de entender",
    """Hola programador X recien descubro tu canal , despues de ver el video veo que javascript esta orientado a personas que tienen logica matematica buena, pero a los que no somos tan buenos en logica matematica habra algún area de TI o de programacion en que nos podamos especializar? , espero que me leas. Saludos""",
    "Muy buen. no tenia idea de JS y lo aprendí en poco tiempo con este video. Muy bueno de verdad gracias por tu tiempo y dedicación haciendo este contenido",
    "muy buena edición, vamos por esa placa de 100k",
    "Me gustaría que hicieras más videos así de prácticas, ayuda mucho",
    "Muchas gracias por tus videos, me ayudan mucho a seguir Aprendiendo",
    "excelente video, me sirvió mucho para estas clases de informática, muchas gracias y sigue así",
    "Hola Xavier, me gustó mucho el video. Hace unos minutos ví el de el plan de estudio que seguiste para aprender programación. Apenas estoy empezando y, me pregunto dónde o cómo puedo aplicar mis conocimientos después de cada sesión de estudio. Espero puedas resoponder. Gracias"
]

palabras_clave= ["bueno", "buen", "gracias", "video", "programador", "mucho", "ayuda", "no", "dificil", "nada"]
palabras_positivas = {"bueno", "buen", "gracias"}
palabras_neutrales = {"video", "programador", "mucho", "ayuda"}
palabras_negativas = {"no", "dificil", "nada"}
#print(palabras_clave)

import unicodedata

def eliminar_tildes(texto):
    """Elimina tildes de una cadena utilizando unicodedata.

    Args:
        texto: La cadena de entrada.

    Returns:
        La cadena sin tildes.
    """

    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

def hacer_w(frase):
    vector = [0,0,0,0,0,0,0,0,0,0]#vector de 10 espacios para las 10 palabras clave
    #Aca normalizamos (sacamos tildes y comas para luego parsear a palabras separadas en una lista y que no nos tome subcadenas)
    frase = eliminar_tildes(frase) 
    frase = frase.replace(","," ") 
    palabras_frase = frase.lower().split() 

    for i in range (len(vector)):
        if palabras_clave[i] in palabras_frase:
            vector[i] = 1
    print(palabras_clave)
    return vector

#print(hacer_w("excelente video, me sirvió mucho para estas clases de informática, muchas gracias y sigue así"))

def hacer_s(frase):
    vector = [0,0,0] #vector de 3 espacios para las 10 palabras clave positivas, neutrales y negativas
    #Aca normalizamos (sacamos tildes y comas para luego parsear a palabras separadas en una lista y que no nos tome subcadenas)
    frase = eliminar_tildes(frase) 
    frase = frase.replace(","," ") 
    palabras_frase = frase.lower().split()
    for i in range (len(palabras_frase)):
        if palabras_frase[i] in palabras_positivas:
            vector[0]+=1
        if palabras_frase[i] in palabras_neutrales:
            vector[1]+=1
        if palabras_frase[i] in palabras_negativas:
            vector[2]+=1
    return vector #El vector contiene en primer lugar positivas, segundo lugar neutras y tercero negativas
#print(hacer_s("excelente video, me sirvió mucho para estas clases de informática, muchas gracias y sigue así"))

def calidad_prom(frase):
    vector = hacer_w(frase)
    palabras_clave_frase = 0
    for coordenada in vector:
        palabras_clave_frase+= coordenada #En este bucle sumamos las DISTINTAS palabras clave que aparecieron en la frase
    return palabras_clave_frase/10 #Porque las palabras clave son 10 en total
#print("calidad promedio: "+str(calidad_prom("excelente video, me sirvió mucho para estas clases de informática, muchas gracias y sigue así")))

def sentimiento_prom(frase):
    vector = hacer_s(frase)
    ponderacion = [1,0,-1] #ponderación para cada tipo de palabras_clave en el vector
    resultante=0
    for i in range (3):
        resultante+= vector[i] * ponderacion[i]
    return resultante

#print("sentimiento promedio: "+str(sentimiento_prom("excelente video, me sirvió mucho para estas clases de informática, muchas gracias y sigue así")))

print("ALGORITMO CON TODAS LAS FRASES\n")

def repetir_todo(frases): #funcion para ejecutar todas las operaciones en todas las frases e imprimirlo
    cont=1
    for frase in frases:
        print(f"Frase {cont}: "+frase)
        print("W: "+str(hacer_w(frase)))
        print("S: "+str(hacer_s(frase)))
        print("Calidad promedio: "+str(calidad_prom(frase)))
        print("Sentimiento promedio: "+str(sentimiento_prom(frase))+"\n")
        cont+=1

repetir_todo(comments)