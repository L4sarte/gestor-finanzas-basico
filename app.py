import datetime, json

try:
    # Abre el archivo en modo lectura ('r')
    with open('datos.json', 'r', encoding='utf-8') as archivo:
        # Carga el contenido JSON en una variable (diccionario o lista)
        datos = json.load(archivo)
        gastos = datos['mis_gastos']
        dinero = datos['mi_dinero']
except:
    gastos = []
    dinero = 0
    

while True:
    opcion = int(input("1. Agregar gasto \n2. Ver todos los gastos \n3. Ver total gastado \n4. Agregar dinero \n5. Ver dinero disponible \n6. Salir \nSeleccione una opcion: "))
    if opcion == 1:
        descripcion = input("Proporcione una descripcion a este gasto: ")
        monto = float(input("Ingrese el monto del gasto: "))
        categoria = input("Ingrese la categoria del gasto: ")
        fecha_actual = datetime.datetime.now().strftime("%d-%m-%y")
        nuevo_gasto = {'descripcion': descripcion, 'monto': monto, 'categoria': categoria, 'fecha': fecha_actual}
        gastos.append(nuevo_gasto)
        dinero -= nuevo_gasto['monto']
        # 1. Creamos el "Paquete Maestro" (Diccionario)
        paquete_de_datos = {
            'mis_gastos': gastos,
            'mi_dinero': dinero
        }
        
        # 2. Abrimos el archivo en modo escritura ('w') y guardamos
        with open('datos.json', 'w', encoding='utf-8') as archivo:
            json.dump(paquete_de_datos, archivo, indent=4)
        
        print("¡Gasto cargado exitosamente!")
    elif opcion == 2:
        print(f"\n-- Todos los gastos --")
        for gasto in gastos:
            print(f"Descripcion: {gasto['descripcion']}, Monto: ${gasto['monto']}, Categoria: {gasto['categoria']}, Fecha: {gasto['fecha']}\n")
    elif opcion == 3:
        print("\n-- Total gastado --")
        gastado = 0
        for gasto in gastos:
            gastado += gasto['monto']
        print(f"$ {gastado}\n")
    elif opcion == 4:
        print("\n-- Agregar dinero --")
        agregar_dinero = float(input("Ingrese el monto a depositar: "))
        dinero += agregar_dinero
        # 1. Creamos el "Paquete Maestro" (Diccionario)
        paquete_de_datos = {
            'mis_gastos': gastos,
            'mi_dinero': dinero
        }
        
        # 2. Abrimos el archivo en modo escritura ('w') y guardamos
        with open('datos.json', 'w', encoding='utf-8') as archivo:
            json.dump(paquete_de_datos, archivo, indent=4)
        
        print("¡Dinero guardado exitosamente!")
    elif opcion == 5:
        print(f"\n-- Dinero disponible --")
        print(f"$ {dinero}\n")
    elif opcion == 6:
        print("Gracias por usar mi sistema")
        break
