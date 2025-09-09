def factorial_x(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_x(n-1)

def suma_n_naturales(n):
    if n == 0:
        return "Finalizado"
    else:
        return n + suma_n_naturales(n-1)

def fibonacci(n):
    pass

def aparaciones_letras(lista, letra, index=0, counter=0):
    if index == (len(lista)-1):
        return counter
    else:
        if letra.lower() == lista[index].lower():
            counter+=1
        return aparaciones_letras(lista,letra,index+1,counter)

def string_reversed(list, index, new_list = []):
    if (index*-1) == (len(list)-1):
        new_list.append(list[0])
        return "".join(new_list)
    else:
        new_list.append(list[index-1])
        return string_reversed(list, index-1)

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)

key = True
while key:
    try:
        calc_ops = input("----------------Bienvenido al menú----------------\n1. Factorial de un número\n2. Suma de los primero números naturales\n3. N númeor fibonacci\n4. Cantidad de apariciones de una letra\n5. Cadena invertida\n6. Calcular potencia de un número n")

        match calc_ops:
            case "1":
                fact = int(input("Coloque el número: "))
                print(f"El factorial de {fact} es {factorial_x(fact)}")
            case "2":
                natural = int(input("Coloque el número: "))
                print(f"La suma de todos los números de {natural} es {suma_n_naturales(natural)}")
            case "3":
                pass
            case "4":
                string_to_evaluate = input("Coloque la string a evaluar: ")
                letter_to_e = input("Coloque una letra a evaluar: ")
                print(f"El número de veces que la letra {letter_to_e} aparece en el texto es de: {aparaciones_letras(list(string_to_evaluate),letter_to_e)}")
            case "5":
                cadena_a_invertir = input("Coloque su cadena: ")
                print(string_reversed(list(cadena_a_invertir), 0))

                #print(string_reversed(cadena_a_invertir_x, 0))
            case "6":
                base = int(input("Coloque la base: "))
                exponent = int(input("Coloque el exponente: "))
                print(f"\nLa potencia de {base} elevado a la {exponent} es {potencia(base, exponent)}\n\n")
            case "7":
                key = False
    except Exception as e:
        print(f"Hubo un error inesperado: {e}")