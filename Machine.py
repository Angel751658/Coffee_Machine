# Coffee Machine

# Inventario actual de la maquina (ingredientes y dinero)
beans = 200
cups = 10
water = 2500
milk = 1000
dinero = 0

# Capacidades máximas
MAX_WATER = 2500
MAX_MILK = 1000
MAX_BEANS = 200
MAX_CUPS = 10

# Registro de cafés vendidos
cafes_vendidos = {"espresso": 0, "latte": 0, "capuccino": 0}

# Función para hacer café
def make_coffee():
    global beans, cups, water, milk, dinero
    while True:
        # Menú de selección de café
        print(" \n\nCafes: \n"
        " 1. Expresso $4 \n"
        " 2. Latte $7 \n"
        " 3. Capuccino $6 \n"
        " 4. Salir")

        opcion_deCafe = input("Seleccione una opción: ")

        match opcion_deCafe:
            case "1":  # Preparar Espresso
                if water >= 250 and beans >= 16 and cups >= 1:
                    print("Aquí tiene su Expreso. ☕")
                    water -= 250
                    beans -= 16
                    cups -= 1
                    dinero += 4
                    cafes_vendidos["espresso"] += 1
                else:
                    print("No hay suficientes ingredientes para un expreso.")
                break

            case "2":  # Preparar Latte
                if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
                    print("Aquí tiene su Latte. ☕")
                    water -= 350
                    milk -= 75
                    beans -= 20
                    cups -= 1
                    dinero += 7
                    cafes_vendidos["latte"] += 1
                else:
                    print("No hay suficientes ingredientes para un latte.")
                break

            case "3":  # Preparar Capuccino
                if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
                    print("Aquí tiene su Capuccino. ☕")
                    water -= 200
                    milk -= 100
                    beans -= 12
                    cups -= 1
                    dinero += 6
                    cafes_vendidos["capuccino"] += 1
                else:
                    print("No hay suficientes ingredientes para un capuccino.")
                break

            case "4":  # Salir al menú principal
                return
            case _:  # Opción inválida
                print("Opción inválida")

# Función para llenar la máquina
def fill_machine():    
    global beans, cups, water, milk, dinero
    if water == 2500 and milk == 1000 and beans == 200 and cups == 10:
        print("\nMáquina llena.")
        return

    while True:
        # Menú de selección de café        
        print(" \n\nSelecciona un deposito: \n"
        " 1. Agua \n"
        " 2. Leche \n"
        " 3. Granos de Café \n"
        " 4. Vasos \n"
        " 5. Salir")

        deposito = input("Seleccione una opción: ")

        match deposito:
            case "1":   # Rellenar agua
                try:
                    agua_ingresada = int(input("Ingrese el agua: "))                
                    if agua_ingresada <= 0:
                        print("Error: Ingrese un número positivo.")
                        continue
                    if water + agua_ingresada > MAX_WATER:
                        print(f"Error: Esa cantidad excede la capacidad máxima de {MAX_WATER}ml.")
                    else:
                        water += agua_ingresada
                        print(f"El agua ha sido rellenada. Nivel actual: {water}ml.")
                except ValueError:
                    print("Error: Por favor, ingrese solo agua.")
                continue

            case "2":   # Rellenar leche
                try:
                    leche_ingresada = int(input("Ingrese la leche: "))
                    if leche_ingresada <= 0:
                        print("Error: Ingrese un número positivo.")
                        continue
                    if milk + leche_ingresada > MAX_MILK:
                        print(f"Error: Esa cantidad excede la capacidad máxima de {MAX_MILK}ml.")
                    else:
                        milk += leche_ingresada
                        print(f"La leche ha sido rellenada. Nivel actual: {milk}ml.")
                except ValueError:
                    print("Error: Por favor, ingrese solo leche.")
                continue

            case "3":   # Rellenar granos de café
                try:
                    beans_ingresados = int(input("Ingrese los granos: "))
                    if beans_ingresados <= 0:
                        print("Error: Ingrese un número positivo.")
                        continue
                    if beans + beans_ingresados > MAX_BEANS:
                        print(f"Error: Esa cantidad excede la capacidad máxima de {MAX_BEANS}g.")
                    else:
                        beans += beans_ingresados
                        print(f"Los granos han sido rellenados. Nivel actual: {beans}g.")
                except ValueError:
                    print("Error: Por favor, ingrese solo granos de café.")
                continue

            case "4":   # Rellenar vasos
                try:
                    cups_ingresados = int(input("Ingrese los vasos: "))
                    if cups_ingresados <= 0:
                        print("Error: Ingrese un número positivo.")
                        continue
                    if cups + cups_ingresados > MAX_CUPS:
                        print(f"Error: Esa cantidad excede la capacidad máxima de {MAX_CUPS} vasos.")
                    else:
                        cups += cups_ingresados
                        print(f"Los vasos han sido repuestos. Nivel actual: {cups} vasos.")
                except ValueError:
                    print("Error: Por favor, ingrese solo vasos.")            
                continue

            case "5":   # Salir al menú principal
                return
            case _: 
                print("Opción inválida")

# Función para retirar dinero
def withdraw_money():
    global dinero

    if dinero == 0:
        print("No hay dinero en la máquina.")
    else: 
        print(f"Ha retirado ${dinero}.")
        dinero = 0        

# Función para mostrar datos
def show_data():
    global beans, cups, water, milk, dinero, cafes_vendidos
    print("\nDatos de la máquina:")
    print(f"Agua: {water}ml")
    print(f"Leche: {milk}ml")
    print(f"Café: {beans}g")
    print(f"Dinero: ${dinero}")
    print("Cafés vendidos:")
    for i in cafes_vendidos:
        print(f"  {i}: {cafes_vendidos[i]}")

# Función para salir de la máquina
def exit_machine():
    print("Saliendo de la máquina...")

# Ciclo principal
while True:
    print("\n\tMENU: \n"
    "==================== \n"
    " 1. Hacer café \n"
    " 2. Llenar máquina \n"
    " 3. Retirar dinero \n"
    " 4. Mostrar datos \n"
    " 5. Salir")

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

