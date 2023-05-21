from helloworld import somar

def verificar_soma():
    resultado = somar(2, 3)
    if resultado == 5:
        print("Ok")
    else:
        print("Not ok")

verificar_soma()
