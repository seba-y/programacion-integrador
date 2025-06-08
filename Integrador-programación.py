separador = "-"*50

# Busqueda lineal
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

numbers2 = [2,4,9,5,1]
animals = ["gato","perro","tigre","leon","tortuga","oso"]
objetivo = 5
objetivo2 = "oso"

def lineal_busqueda(target: object, arr: list) -> bool:
    conincidencia = False
    indice = 0
    for o in arr:
        if target is o:
            conincidencia = True
            break
        indice +=1
    if conincidencia:
        print(f"Coincidencia encontrada en el indice: {indice}")
    else:
        print("No hay ninguna concidencia")
    
    


#Busqueda Binaria
def binaria_busqueda(target: object, lista: list, comienzo: int, final: int) -> bool:
    print(f'Buscando {target} entre {lista[comienzo]} y {lista[final]}')
    if comienzo > final:
        return -1

    medio = (comienzo + final) // 2

    if lista[medio] == target:
        print(f"el elemento se encuentra en el índice: {medio}")
    elif lista[medio] < target:
        return binaria_busqueda(target, lista, medio + 1, final)
    else:
        return binaria_busqueda(target, lista, comienzo, medio - 1)



#Ordenamiento Burbuja

def burbuja_ord(lista: list) -> list:
    lista_fake = lista[:]
    n = len(lista_fake)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_fake[j] > lista_fake[j + 1]:
                lista_fake[j], lista_fake[j + 1] = lista_fake[j + 1], lista_fake[j]
                print(f"paso {i+1}: {lista_fake}")
    return lista_fake
    


#ordenamiento por insercion

def insercion_ord(lista: list) -> list:
    lista_fake = lista[:]
    for i in range(1, len(lista_fake)):
        valor_actual = lista_fake[i]
        actual = i - 1

        while actual >= 0 and lista_fake[actual] > valor_actual:
            lista_fake[actual + 1] = lista_fake[actual]
            actual -= 1
            
        lista_fake[actual + 1] = valor_actual
        print(f"paso{i}: {lista_fake}")    
    return lista_fake


# Ordenamiento por mezcla


def mezlca_ord(lista: list) -> list:
    lista_fake = lista

    
    if len(lista_fake) <= 1:
        return lista_fake[:]
    
    medio = len(lista_fake) // 2
    izquierda = mezlca_ord(lista_fake[:medio])
    derecha = mezlca_ord(lista_fake[medio:])
    

    mezclado = mezcla(izquierda,derecha)
    print(mezclado)
    
    return mezclado



def mezcla(izquierda: list, derecha: list) -> list:
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i]<derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


print(f"{separador}\nBUSQUEDA BINARIA \n")
binaria_busqueda(objetivo, numbers, 0, len(numbers)-1)
print(f"{separador}\nBUSQUEDA LINEAL \n")
lineal_busqueda(objetivo2, numbers+animals)

print(f"\n{separador}\n")

print("BURBUJA")
print(f"Lista Final -> {burbuja_ord(numbers2)}")
print(separador)
print("INSERCION")
print(f"Lista Final -> {insercion_ord(numbers2)}")
print(separador)
print("MEZCLA")
print(f"Lista final -> {mezlca_ord(numbers2)}")
print(separador)