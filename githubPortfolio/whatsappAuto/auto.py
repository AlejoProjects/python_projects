import pywhatkit
from datetime import datetime
'''
This small Script reads the content of a text and then using pywhatkit opens the whatssapp web one minute after the actual time, searches for the number or group id given and sends a message, finally it closes the page ending the process
Este pequeño script lee el contenido de un texto y luego usando pywhatkit(libreria que usa selenium para hacer web scrapping)
abre la pagina de whatsapp web 1 minuto despues de la hora actual, busca el numero o group id dado y envia un mensaje, finalmente cierra la pagina completando el flujo
'''
def mensaje():
    '''
    Open the file contenido.txt and saves all the lines corresponding to the file
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
    This function  gets the actual date and a minute after sends the received message to the destinatary
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
