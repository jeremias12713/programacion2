radio=0
area=0
altura=0
opc=0
volumen=0

print('Sacar el area de un circulo (1)')
print('Sacar el volumen de un cilindro (2)')
opc=int(input())

if(opc==1):
    print('Ingrese el radio de su circulo')
    radio=int(input())
    area=((radio**2)*(3.1416))
    print('El area de su circulo es:' , area , 'cm3')
else:
    if(opc==2):
        print('Ingrese el radio del cilindro')
        radio=int(input())
        print('Ingrese la altura del cilindro')
        altura=int(input())
        area=((radio**2)*(3.1416))
        volumen=(area*volumen)
        print('El volumen de su cilindro es: ' , volumen , 'cm3')
    


