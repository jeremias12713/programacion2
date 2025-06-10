import random

num1=0
use=0
cont=1
num1=random.randint(1,20)

while(cont==6) or (use!=num1):
    print('Ingrese un número del 1 al 20')
    use=int(input())
    if(use>=1 and use<=20):
        if(use==num1):
            print('ganaste')
            cont=cont+6
        else:
            if(use<num1):    
                print('tu numero es menor')
            else:
                (use>num1)
                print('tu numero es mayor')
                cont=cont+1
    else:
        print('tu numero es invalido')
        cont=cont+6
    


  
