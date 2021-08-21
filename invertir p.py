mensaje = input("ingrese una frase: \n")

texto = mensaje.split()
texto.reverse()

resultado = "  ".join(texto)
print(resultado)

