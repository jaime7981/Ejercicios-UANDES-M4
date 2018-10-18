def numero_menor(lista, n):
    k = len(lista)-n-1
    if len(lista) == n+1:
        print("numero menor es", lista[n])
    elif lista[n] < lista[n+k]:
        print("numero menor es", lista[n])
    elif lista[n] > lista[n+k]:
        numero_menor(lista, n+1)

lista = [5,8,6,9,2,12,45,3,63]
numero_menor(lista, 0)
