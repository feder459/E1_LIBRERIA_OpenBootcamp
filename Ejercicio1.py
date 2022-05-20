
lista=[]
resp="si"

while(resp=="si"):
    resp=input("¿Desea ingresar el nombre de un país?(Ingrese si o no): ")
    if (resp=="si"):
        n=str(input("Ingrese el nombre del pais: "))
        lista.append(n)
#el método set() elimina los elementos repetidos
repetidos=set(lista)
ordenados=sorted(repetidos)
print(ordenados)