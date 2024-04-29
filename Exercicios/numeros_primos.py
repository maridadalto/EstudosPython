import math

def NumPrimos(numeros):
    listaNumeros = []
    for num in numeros:
        if num > 1:
            primo = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    primo = False
                    break
            if primo:
                listaNumeros.append(num)
    return listaNumeros

def main():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    primos = NumPrimos(numeros)
    print(primos)
         
main()
