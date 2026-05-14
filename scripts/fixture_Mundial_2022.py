import csv

# Nombre del archivo
archivo_nombre = 'd:/C/Respaldo de Laura/UTN/organizacion empresarial/tp 2 oe/fixture_qatar_2022_resultados.csv'

try:
    with open(archivo_nombre, mode='r', encoding='utf-8') as archivo:
        # Creamos un lector de diccionarios para usar los nombres de las columnas
        lector_csv = csv.DictReader(archivo)
        
        # Imprimir encabezado con formato
        print(f"{'FECHA':<12} | {'GRUPO':<6} | {'EQUIPO 1':<15} | {'RES.':<7} | {'EQUIPO 2':<15}")
        print("-" * 65)
        
        for fila in lector_csv:
            # Extraemos los datos de cada fila
            fecha = fila['Fecha']
            grupo = fila['Grupo']
            equipo1 = fila['Equipo 1']
            resultado = fila['Resultado']
            equipo2 = fila['Equipo 2']
            
            # Imprimir la fila con alineación para que parezca una tabla
            print(f"{fecha:<12} | {grupo:<6} | {equipo1:<15} | {resultado:<7} | {equipo2:<15}")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_nombre}'.")
except Exception as e:
    print(f"Ocurrió un error: {e}")