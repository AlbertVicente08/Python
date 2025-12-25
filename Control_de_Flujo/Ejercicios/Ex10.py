"""
El FizzBuzz (Clásico de Entrevista): Recorre los números del 1 al 15 con un for.
- Si el número es divisible por 3, imprime "Fizz".
- Si es divisible por 5, imprime "Buzz".
- Si es por ambos, "FizzBuzz".
- Si no, imprime el número.
"""



for i in range(1,16):
    if i % 3 == 0  and i % 5 == 0:
        print("FizzBuzz")        
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)