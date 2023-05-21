from helloworld import somar

def verificar_soma():
    resultado = somar(2, 3)
    if resultado == 5:
        print("A soma é igual a 5.")
    else:
        print("A soma não é igual a 5.")

verificar_soma()
