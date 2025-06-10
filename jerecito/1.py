nacimiento=0

año=0

nombre=""

print("ingrese su nombre")
nombre=input()

print("Hola",nombre,"buen dia")

print("ingrese su año de nacimiento")
nacimiento=int(input())

print("ingrese el año actual")
año=int(input())

print("¿ya cumpliste años, si o no ?")
cumpli=input()

if(cumpli=="si"):
    edad=(año-nacimiento)
    print("su edad es",edad)
else:
    edad=(año-nacimiento-1)
    print("tu edad es",edad)
    
