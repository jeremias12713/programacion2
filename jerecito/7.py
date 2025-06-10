from datetime import date


anio = int(input("Introduce tu año de nacimiento (AAAA): "))
mes = int(input("Introduce tu mes de nacimiento (1-12): "))
dia = int(input("Introduce tu día de nacimiento (1-31): "))


fecha_nacimiento = date(anio, mes, dia)
hoy = date.today()


edad_en_dias = (hoy - fecha_nacimiento).days


anios = hoy.year - fecha_nacimiento.year
meses = hoy.month - fecha_nacimiento.month
dias = hoy.day - fecha_nacimiento.day

if dias < 0:

    meses -= 1
    
    if hoy.month == 1:
        mes_anterior = 12
        anio_anterior = hoy.year - 1
    else:
        mes_anterior = hoy.month - 1
        anio_anterior = hoy.year
    

    if mes_anterior in [1,3,5,7,8,10,12]:
        dias_en_mes_anterior = 31
    elif mes_anterior in [4,6,9,11]:
        dias_en_mes_anterior = 30
    else:
    
        if (anio_anterior % 4 == 0 and anio_anterior % 100 != 0) or (anio_anterior % 400 == 0):
            dias_en_mes_anterior = 29
        else:
            dias_en_mes_anterior = 28

    dias += dias_en_mes_anterior

if meses < 0:
    anios -= 1
    meses += 12


print("Tu edad total en días:", edad_en_dias, "días")
print("Tu edad es:", anios, "años,", meses, "meses y", dias, "días")
