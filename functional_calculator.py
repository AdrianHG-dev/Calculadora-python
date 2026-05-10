def iniciar_calculadora():
    print("===Bienvenido a la calculadora interativa===")
    print('Ingrese su operacion (2+2, 2-2, 2*2, 2/2) o "salir" para terminar.')

    while True:

        entrada = input("\nIngresa tu operación: ").strip().lower()
        if entrada == "salir":
            print("Hasta pronto!")
            break
        
        entrada = entrada.replace("x", "*")
        entrada = entrada.replace(" ", "")

        operador = None

        for op in ["+", "-", "*", "/"]:
            if op in entrada[1:]:
                operador = op
                break

        if not operador:
            print("Error: No se detectó una operación válida (+, -, *, /).")
            continue
        
        try:
            partes = entrada.rsplit(operador, 1)

            num1 = float(partes[0])
            num2 = float(partes[1])

            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                if num2 == 0:
                    print("Error: No se puede dividir por cero.")
                    continue
                resultado = num1 / num2


            if resultado.is_integer():
                print(f"resultado: {int(resultado)}")
            else:
                print(f"Resultado: {resultado}")
            
        except ValueError:
            print("Error: Asegúrate de ingresar solo números válidos y un operador.")

if __name__ == "__main__":
    iniciar_calculadora()




            





    
