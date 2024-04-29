def ConverterCelsius(temp):
    fahrenheit = (temp *9 /5)+32
    return fahrenheit

def main():
    celsius = input("Informe a temperatura em Celsius para conversao: ")
    resultado = ConverterCelsius(float(celsius))
    print(f"O resultado da conversao e: {resultado}")

main()