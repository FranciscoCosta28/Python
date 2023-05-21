from helloworld import somar

def verificar_soma():
    resultado = somar(2, 3)
    print(resultado)
    if resultado == 5:
        print("Ok")
    else:
        print("Not ok")

verificar_soma()
