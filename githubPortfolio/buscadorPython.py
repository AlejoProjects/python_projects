#Este script elimina una palabra dada dentro de todo el texto.

def borradorEspacios(sentence,posI,posF):
    '''
    sentence= string
    posI,posF = int
    Esta función borra los espacios extras que se encuentran en el texto

    '''
    if(sentence[posI - 1] == " "):
        trimmed = sentence[0:posI -2] + sentence[posI + 2:len(sentence)]
    elif(sentence[posF - 1] == " "):
        trimmed = sentence[0:posF -2] + sentence[posF + 2:len(sentence)]
    else:
        trimmed = sentence[0:posI] + sentence[(i + j) + 1:len(sentence)]
    return(trimmed)

def recortador(sentence,word):
    """
    sentence,word = String
    esta función remueve la palabra word de un texto dado 
    """
    i = j = 0
    valor = sentence
    existe = True
    while existe == True:
            existe = False#valor bool por defecto para que se ejecute el ciclo hasta que cambie el valor de verdad
            i = 0
            #loop ejecutado según el largo del texto
            for x in sentence[0:len(sentence)-1]:
                #condición para identificar si la primera de la palabra coincide con la palabra actual del texto
                if(word[0] == sentence[i]):
                    j = 0#primera letra de la palabra
                    #mientras que cada letra de la palabra sea la misma del texto el ciclo continuara
                    while (word[j] == sentence[i + j]):
                        #si se llega al final de la palabra quiere decir que se ha encontrado la palabra en el texto
                        if(j == len(word)-1):
                            #crea una nueva string que elimina la palabra del texto
                            valor = sentence[0:i] + sentence[(i + j)+1 :len(sentence)]
                            #elimina los espacios extras resultantes de la eliminación
                            sentence = borradorEspacios(valor)
                            #como el valor de verdad se cambia el primer ciclo se rompera
                            existe = True
                            i = 0
                            #se rompe el segundo ciclo
                            break
                        
                        j+=1               
                i+= 1
    print(sentence)
def borradorEspacios(sentence):
    k = 0
    for w in sentence:
        if(k == len(sentence)):break
        if(" " == sentence[k]):
            if(" " == sentence[k + 1]):
                sentence = sentence[0:k]+sentence[k+1:len(sentence)]       
        k+=1
    return(sentence)
texto = "Cadaprueba vez que pienso prueba en ti, pruebamis ojos rompen en llanto;y muy triste me pregunto, ¿por qué te quiero tanto?"
recortador(texto,"prueba")
