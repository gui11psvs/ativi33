#mostre-me as seguinte listas, derivadas de: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  Intervalo de 1 a 9  Intervalo de 8 a 13  Números pares  Números ímpares  Todos os múltiplos de 2, 3 e 4 Lista reversa  Razão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9 em float!

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Intervalo de 1 a 9
intervalo_1_9 = lista[1:10]

# Intervalo de 8 a 13
intervalo_8_13 = lista[8:14]

# Números pares
numeros_pares = [num for num in lista if num % 2 == 0]

# Números ímpares
numeros_impares = [num for num in lista if num % 2 != 0]

# Todos os múltiplos de 2, 3 e 4
multiplos_2_3_4 = [num for num in lista if num % 2 == 0 and num % 3 == 0 and num % 4 == 0]

# Lista reversa
lista_reversa = lista[::-1]

# Razão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9
soma_10_15 = sum(lista[10:16])
soma_3_9 = sum(lista[3:10])
razao = soma_10_15 / soma_3_9

# Exibindo os resultados
print("Intervalo de 1 a 9:", intervalo_1_9)
print("Intervalo de 8 a 13:", intervalo_8_13)
print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)
print("Múltiplos de 2, 3 e 4:", multiplos_2_3_4)
print("Lista reversa:", lista_reversa)
print("Razão entre a soma do intervalo de 10 a 15 e o intervalo de 3 a 9:", float(razao))
