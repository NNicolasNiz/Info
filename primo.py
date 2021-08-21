
def es_primo(num):
    for x in range(2, num):
        if (num % x) == 0:
            return False
    return True


primo = es_primo(int(input("Ingrese el número para saber si es primo: ")))
if primo == True:
    print("El número es primo")
else:
    print("El número no es primo")



#para qeu no se imnpoirte en otro lado
#if __name__ == "__main__"
