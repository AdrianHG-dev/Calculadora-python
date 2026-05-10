print("\nBienvenido al portal de pago")


while True:
    user = input("\nIngrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    
    if user == "ejemplo@gmail.com" and password == "hola123":
        print("\nBienvenido Adrian!")
        break
        
    else:
        print("\nAcceso denegado, intente de nuevo.")
        
    
while True:
    print('Escriba la operacion que desea realizar (Transferencia, Pago de servicios o "Salir" para terminar.): ')
    operacion = input().strip().capitalize()

    if operacion == "Salir":
        break

    if operacion == "Transferencia":
        transferencia = int(input("Ingrese el numero de cuenta del destinatario: "))
        monto = int(input("Ingrese el monto que desea transferir (USD): "))

        if not (10 <= monto <= 10000):
            print("Error. Solo se permiten transferencias de 10USD a 10,000USD")
            break
    
        print(f"Transferencia exitosa a #{transferencia} por un monto de {monto}USD. Gracias por preferirnos!")
    
    elif operacion == "Pago de servicios":
        agua = "50"
        luz = "150"
        tipo_servicio = (input("Ingrese el tipo de servicio (agua o luz): ")).strip().capitalize

        if tipo_servicio == "Agua":
            print(f"El total a pagar de su cuenta de agua es de {agua}USD.")
            print("Desea realizar el pago?")
            confirmacion = input("Si/No").strip().capitalize()
            if confirmacion == "Si":
                print("Pago completado con exito!")

            else:
                print("Pago cancelado.")
                break

        elif tipo_servicio == "Luz":
            print(f"El total a pagar de su cuenta de luz es de {luz}USD.")
            print("Desea realizar el pago?")
            confirmacion = input("Si/No").strip().capitalize()
            if confirmacion == "Si":
                print("Pago realizado con exito!")

            else:
                print("Pago cancelado.")
                break
        




        




          



    