import random as rd
import csv
sueldos=[]
sueldop=[]
sueldom=[]
sueldog=[]
suma=0
trabajadores =  ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
def Asignar(trabajadores):
    for i in range(10):
        randome=rd.randint[300000:2500000]
        sueldos.append(randome)


def Clasificar(sueldos):    
    for i in sueldos:
        if sueldos<800000:
            sueldop.append(sueldos)
        elif sueldos>800000 and sueldos<2000000:
            sueldom.append(sueldos)
        else:
            sueldog.append(sueldos)

def estadísticas(sueldos):
    for i in range(10):
        suma=suma+sueldos
    promedio=suma/10


  

def Reporte():
    print()
try:
    while True:
        print("------------------------------")
        print("(1)Asignar sueldos aleatorios")
        print("(2)Clasificar sueldos")
        print("(3)Ver estadísticas")
        print("(4)Reporte de sueldos")
        print("(5)Salir del programa")
        print("------------------------------")
        opcion1=int(input("ingrese la opcion"))
        if opcion1==1:
            Asignar    
        elif opcion1==2:
            if len(sueldos)==0:
                print("no ha asignado sueldo todavia")
            else:

                print("Sueldos menores a 800000")
                for i in sueldop:
                    print (sueldop)
                print("Sueldos mayores a 800000 y menores a 2000000")
                for i in sueldom:
                    print (sueldom)
                print("Sueldos mayores a 2000000")
                for i in sueldog:
                    print(sueldog)
        elif opcion1==3:
            Clasificar
            print()
        elif opcion1==4:
            2
        elif opcion1==5:
            break
        else:
            ("seleccione un numero valido")
except ValueError:
    print("error en el programa")