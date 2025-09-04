mensajes={}
def enviar_msj(contacto, texto):
    if contacto not in mensajes:
        mensajes[contacto]=[]
    mensajes[contacto].append(texto)
    print("Mensaje enviado a ",contacto," : ",texto)

def ver_mensajes(contacto):
    if contacto not in mensajes or not mensajes[contacto]:
        print("No tiene mensajes con ",contacto)
    else:
        print("Chat con ",contacto,":" )
        for i in mensajes[contacto]:
            print("-",i)
