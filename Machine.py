# Coffee Machine
# Inventario (variables a usar)
beans = 200
cups = 10
water = 2500
milk = 1000
dinero = 0

cafes_vendidos = {"espresso": 0, "latte": 0, "capuccino": 0}

#
def make_coffee():
    global beans, cups, water, milk, dinero
    while True:
        print(" Menu: \n"
        " 1. Expresso $4 \n"
        " 2. Latte $7 \n"
        " 3. Capuccino $6 \n"
        " 4. Salir")

        opcion_deCafe = input("Seleccione una opción: ")

        match opcion_deCafe:
            case "1":            
                water -= 250 
                beans -= 16
                dinero += 4
                cafes_vendidos["espresso"] += 1
                if water < 0 or milk < 0 or beans < 0:
                    print("No hay suficientes ingredientes.")
                else:
                    print("Aquí tiene su Expreso. ☕")
                break
            case "2":            
                water -= 350
                milk -= 75
                beans -= 20
                dinero += 7
                cafes_vendidos["latte"] += 1
                if water < 0 or milk < 0 or beans < 0:
                    print("No hay suficientes ingredientes.")
                else:
                    print("Aquí tiene su Latte. ☕")
                break
            case "3":                
                water -= 200
                milk -= 100
                beans -= 12
                dinero += 6
                cafes_vendidos["capuccino"] += 1
                if water < 0 or milk < 0 or beans < 0:
                    print("No hay suficientes ingredientes.")
                else:
                    print("Aquí tiene su Capuccino. ☕")
                break
            case "4":
                return
            case _ :
                print("Opción inválida")

#
def fill_machine():    
    global beans, cups, water, milk, dinero
    if water == 2500 and milk == 1000 and beans == 200:
        print("Máquina llena.")
        return

    while True:
        print(" Selecciona un deposito: \n"
        " 1. Agua \n"
        " 2. Leche \n"
        " 3. Café \n"
        " 4. Salir")

        deposito = input("Seleccione una opción: ")

        match deposito:
            case "1":   
                agua_ingresada = input("Ingrese la cantidad de agua:")
                water += agua_ingresada
                print("El agua ha sido rellenada.")
                continue
            case "2":                  
                leche_ingresada = input("Ingrese la cantidad de leche:")
                milk += leche_ingresada      
                print("La leche ha sido rellenada.")
                continue
            case "3":                  
                beans_ingresados = input("Ingrese la cantidad de granos:")
                beans += beans_ingresados            
                print("Los granos han sido rellenada.")
                continue
            case "4":
                return
            case _ :
                print("Opción inválida")


def withdraw_money():
    global dinero

    if dinero == 0:
        print("No hay dinero en la máquina.")
        return
    
    print(f"Ha retirado ${dinero}.")
    

def show_data():
    global beans, cups, water, milk, dinero, cafes_vendidos
    print("Datos de la máquina:")
    print(f"Agua: {water}ml")
    print(f"Leche: {milk}ml")
    print(f"Café: {beans}g")
    print(f"Dinero: ${dinero}")
    print("Cafés vendidos:")
    for i in cafes_vendidos:
        print(f"  {i}: {cafes_vendidos[i]}")

def exit_machine():
    print("Saliendo de la máquina...")


while True:
    print(" Menu: \n"
    " 1. Hacer café \n"
    " 2. Llenar máquina \n"
    " 3. Retirar dinero \n"
    " 4. Mostrar datos \n"
    " 5. Salir ")

    opcion_elegida = input("Seleccione una opción: ")

    match opcion_elegida:
        case "1":
            make_coffee()
        case "2":
            fill_machine()
        case "3":
            withdraw_money()
        case "4":
            show_data()
        case "5":
            exit_machine()
            break
        case _:
            print("Opción no válida")








