import math

def PrimeNumber(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):
         if num % i == 0:
            return False
    
    return True

def main():
    numero = input("Informe o numero a ser verficado: ")
    resultado = PrimeNumber(int(numero))

    if resultado:
        print("E numero primo")
    else:
        print("Nao e primo")

main()