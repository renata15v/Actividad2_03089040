print("\n⋆˚꩜｡")
print("Ejercicio 5 realizado por Renata\n")
print("Ejercicio 5: ¿Cuánto dura mi playlist?")

# Duración de cada canción en segundos 
cancion1 = 173
cancion2 = 158
cancion3 = 183
cancion4 = 178
cancion5 = 196

# Sumamos todo
total_segundos = cancion1 + cancion2 + cancion3 + cancion4 + cancion5

# // división entera: cuántos minutos completos caben 
minutos = total_segundos // 60 

# % residuo: los segundos que sobran
segundos = total_segundos % 60
print("\nResultados")
print(f"Total en segundos: {total_segundos}")
print(f"Tu playlist dura {minutos} minutos con {segundos} segundos")
print("\n⋆˚꩜｡")