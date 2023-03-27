import pywhatkit
from datetime import datetime
'''
Este pequeño script lee el contenido de un texto y luego usando pywhatkit(libreria que usa selenium para hacer web scrapping)
abre la pagina de whatsapp web 1 minuto despues de la hora actual, busca el numero o group id dado y envia un mensaje, finalmente cierra la pagina completando el flujo
'''
def mensaje():
    '''
    abre el file contenido.txt y guarda todas las lineas del archivo
    '''
    with open("contenido.txt") as f:
        lines = f.readlines()
    text = ''
    for i in range(0,len(lines)):
        text += lines[i]
    return text

def enviarTexto(texto,destinatario):
    '''
    texto,destinatario = string
    esta función obtiene la hora actual y un minuto despues envia el mensaje recibido al destinatario indicado
    '''
    currentDateAndTime = datetime.now()
    hour = int(currentDateAndTime.strftime("%H"))
    minutes = int(currentDateAndTime.strftime("%M")) + 1
    if(destinatario[0]== "+"):
        pywhatkit.sendwhatmsg(destinatario,texto,hour,minutes + 1,10,True,15) 
    else:
        pywhatkit.sendwhatmsg_to_group(destinatario, texto , hour,minutes + 1,10,True,15)
    return None

if __name__== '__main__':
    groupId = ""
    numero = ""
    enviarTexto(mensaje(),groupId)
