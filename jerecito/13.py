matriz = []
valor = 1
for i in range(4):
    fila = []
    for j in range(4):
        fila.append(valor)
        valor += 1
    matriz.append(fila)


suma_dp = 0
mult_dp = 1
suma_cd = 0
mult_cd = 1


for i in range(4):
    suma_dp += matriz[i][i]
    mult_dp *= matriz[i][i]

    suma_cd += matriz[i][3 - i]
    mult_cd *= matriz[i][3 - i]


print("Matriz 4x4:")
for fila in matriz:
    print(fila)


print("\nResultados:")
print(f"Suma diagonal principal: {suma_dp}")
print(f"Multiplicación diagonal principal: {mult_dp}")
print(f"Suma contradiagonal: {suma_cd}")
print(f"Multiplicación contradiagonal: {mult_cd}")
