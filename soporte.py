# definimos la funcion

def soporte_automatico(opcion):
    if opcion == "problemas de internet": return internet
    elif opcion == "problemas con productos": return productos
    elif opcion == "hablar con un agente": return agente
    else:
        return lambda: "Opcion no valida."
    
def internet():
    return "Reinicie su router y vuelva a intentarlo."
def productos():
    return "Puede hacer la devolucion del producto en 5 dias."
def agente():
    return "El agente del sistema se estara comunicando con usted en un momento."    

# Mostramos el mensaje de bienvenida y el menu 
print("BIENVENIDO AL SISTEMA DE SOPORTE\n")
while True:
    print("\nMenu\n")
    print("problemas de internet") 
    print("problemas con productos")
    print("hablar con un agente")
    print("salir\n")        

    opcion = input("Diganos que desea realizar?\n").lower()
    
    if opcion == "salir":
        print("Gracias por confiar en nosotros. Un placer asistirle.")
        break
    soporte = soporte_automatico(opcion)
    print(soporte())            
    
