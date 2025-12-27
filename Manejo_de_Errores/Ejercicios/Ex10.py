# Ex10.py
# Bucle de Insistencia: Crea un programa que pregunte al usuario "¿Cuántos años tienes?".
# Si el usuario ingresa texto o un error, el programa debe decir "Dato incorrecto"
# y volver a preguntar hasta que el usuario ingrese un número válido.
# (Pista: usa un while True y break en el try o en el else).


while True:
    try:
        user_input = input("Cuantos años tienes? ")
        edad = int(user_input)
    except ValueError:
        print("Dato incorrecto")
    else:
        break
