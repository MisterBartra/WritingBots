import webbrowser
import time

# Obtener entrada del usuario para los números desde y hasta
desde = int(input("Desde match_id:"))
hasta = int(input("Hasta match_id:"))

# Ajustar el valor de match_id según la relación entre desde y hasta
if desde < hasta:
    i = 1
else:
    i = -1

match_id = desde

# Encontrar match en el rango especificado
while match_id != hasta:
    url = 'https://osu.ppy.sh/mp/' + str(match_id)
    webbrowser.open_new_tab(url)
    match_id += i
    print(match_id)
    time.sleep(1.5)

# Cerrar el programa al finalizar
exit()