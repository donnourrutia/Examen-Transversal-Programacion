import random
import csv
import math


trabajadores=["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisico Diaz","Elena Fernandez"]


def generar_sueldos():
    sueldos =[]
    for _ in range (len(trabajadores)):
        sueldos.append(random.randint(300000,2500000))
        return sueldos
    
def clasificar_sueldos(sueldos):
    sueldos_menores =[]
    sueldos_medios = []
    sueldos_mayores = []
    total_sueldos = 0
    for empleado, sueldo in zip(trabajadores, sueldos):
        total_sueldos += sueldo
        if sueldo < 800000:
            sueldos_menores.append ((empleado, sueldo))
        elif sueldo <= 2000000:
            sueldos_medios.append ((empleado,sueldo))
        else:
            sueldos_mayores.append ((empleado, sueldo))
    print("\n Clasificacion de sueldos")

    print(f"Sueldos menor a $800.000 (Total: ${sum(sueldo for _, sueldo in sueldos_menores):,.2f}):")
    for empleado, sueldo in sueldos_menores:
        print(f"- {empleado}: ${sueldo:,.2f}")

    print(f"Sueldos entre $800.000 y $2.000.000 (Total: {len(sueldos_medios)}):")
    for empleado, sueldo in sueldos_medios:
        print(f"- {empleado}: ${sueldo:,.2f}")

    print(f"Sueldos superiores a $2.000.000 (Total: {len(sueldos_mayores)}):")
    for empleado, sueldo in sueldos_mayores:
        print(f"- {empleado} : ${sueldo:,.2f}")


def Mostrar_estadisticas(sueldos):
    try:
        sueldo_maximo =max(sueldos)
        sueldo_minimo =min(sueldos)
        promedio =sum(sueldos) /len(sueldos)
        media_geometrica = math.sqrt(sueldo_maximo + sueldo_minimo)
        
        print("\nEstadisticas de sueldos:")
        print(f"Sueldo mas alto: ${sueldo_maximo:,.2f}")
        print(f"Sueldo mas bajo: ${sueldo_minimo:,.2f}")
        print(f"Promedio: ${promedio:,.2f}")
        print(f"Media geometrica: ${media_geometrica:,.2f}")
    except Exception as errorEstadistico:
        print(f"Error al calcular las estadisitcas: {errorEstadistico}")

def reporte_de_sueldos(sueldos):
    print("Reporte de Sueldos: \n")
    print("{:<25} {:<12} {:<12} {:<12} {:<12}".format("Nombre Empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"))
    for empleado, sueldo in zip(trabajadores,sueldos):
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo  * 0.12
        sueldo_liquido= sueldo - descuento_salud - descuento_afp
        print(empleado,descuento_salud,descuento_afp,sueldo_liquido)

def exportar_a_csv(sueldos, filename='reporte_sueldos.csv'):
    with open (filename, mode='w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre Empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
        for empleado, sueldo in zip(trabajadores, sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo  * 0.12
            sueldo_liquido= sueldo - descuento_afp - descuento_salud
            writer.writerow([empleado, sueldo, descuento_salud, descuento_afp, sueldo_liquido])
    print(f"Reporte exportado a {filename}")

def menu_principal():
    print("")
    print("1. Generar sueldos alatorios")
    print("2. Clasificar Sueldos")
    print("3. Mostrar Estadisticas")
    print("4. Reporte de Sueldos")
    print("5. Exportar reporte a csv")
    print("6. Salir del Programa")

sueldos = []


while True:
    menu_principal ()
    opcion = int(input("Eliga una opcion del 1-6\n"))
    if opcion == 1:
        sueldos = generar_sueldos()
        print("Sueldos Generado. ")
    elif opcion == 2:
        if sueldos: 
            clasificar_sueldos(sueldos)
        else:
            print("Primero debe generar los sueldos para poder Clasificarlos")
    elif opcion == 3:
        if sueldos:
            Mostrar_estadisticas(sueldos)
        else:
            print("Primero debe generar los sueldos para poder Clasificarlos")
    elif opcion == 4:
        if sueldos:
            reporte_de_sueldos(sueldos)
        else:
            print("Primero debe generar los sueldos para poder Clasificarlos")
    elif opcion == 5:
        if sueldos:
            exportar_a_csv(sueldos)
        else:
            print("Primero debe generar los sueldos para poder Clasificarlos")
    elif opcion == 6:
        print ("Saliendo Del Programa")
        break
    else:
        print("Opcion no valida. Intente nuevamente;)")
