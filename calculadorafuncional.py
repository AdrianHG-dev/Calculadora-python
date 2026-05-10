def iniciar_calculadora():
    print("=== Calculadora Interactiva ===")
    print("Escribe tu operación (ej. 2+2, 5x3, 10/2) o escribe 'salir' para terminar.")

    # El bucle 'while True' permite que el programa siga pidiendo operaciones 
    # infinitamente sin tener que reiniciarlo desde cero.
    while True:
        # 1. Recibir entrada y normalizarla (quitar espacios y poner en minúsculas)
        entrada = input("\nIngresa operación: ").strip().lower()

        # 2. Condición de salida para romper el bucle
        if entrada == 'salir':
            print("¡Calculadora apagada. Hasta pronto!")
            break

        # 3. Preparar la cadena de texto
        # Reemplazamos la 'x' por '*' para unificar el símbolo de multiplicación
        entrada = entrada.replace('x', '*')
        # Eliminamos cualquier espacio en blanco que el usuario haya puesto entre los números
        entrada = entrada.replace(' ', '') 

        # 4. Identificar el operador matemático
        operador = None
        
        # Buscamos el operador. Lo hacemos a partir del segundo carácter (entrada[1:]) 
        # para evitar problemas si el usuario ingresa un primer número negativo (ej: -5+2).
        for op in ['+', '-', '*', '/']:
            if op in entrada[1:]:
                operador = op
                break

        # Si el bucle termina y no encontró ningún operador, avisa y vuelve a empezar
        if not operador:
            print("Error: No se detectó una operación válida (+, -, *, /).")
            continue 

        # 5. Separar los números y realizar el cálculo
        try:
            # Separamos la cadena en dos partes usando el operador encontrado.
            # rsplit() divide desde la derecha hacia la izquierda.
            partes = entrada.rsplit(operador, 1) 
            
            # Convertimos los textos extraídos a números decimales (float)
            num1 = float(partes[0])
            num2 = float(partes[1])

            # 6. Lógica matemática según el operador
            if operador == '+':
                resultado = num1 + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                if num2 == 0:
                    print("Error: No se puede dividir por cero.")
                    continue # Salta el resto del código y pide otra operación
                resultado = num1 / num2

            # 7. Imprimir el resultado de forma limpia
            # Si el resultado es un número entero (ej. 4.0), lo mostramos sin decimales
            if resultado.is_integer():
                print(f"Resultado: {int(resultado)}")
            else:
                print(f"Resultado: {resultado}")

        # Manejo de errores en caso de que el usuario escriba letras o símbolos raros
        except ValueError:
            print("Error: Asegúrate de ingresar solo números válidos y un operador.")

# Punto de entrada del programa
if __name__ == "__main__":
    iniciar_calculadora()

    