print("\nEjercicio 3: ¿Cuánto escucho a mi artista favorito?")
print("\nMI ARTISTA FAVORITO\n")

artista = "the marías"
canciones_por_dia = 15
duracion_promedio = 3.5    # minutos por canción 

minutos_dia = canciones_por_dia * duracion_promedio      # minutos al día
minutos_anio = minutos_dia * 365                         # minutos al año
horas_anio = minutos_anio / 60                           # 1 hora = 60 minutos
dias_anio = horas_anio / 24                              # 1 día = 24 horas

print(f"Escuchas a {artista} {minutos_dia} minutos al día")
print(f"Al año son {minutos_anio} minutos")
print(f"Eso equivale a {horas_anio:1f} horas")
print(f"¡O sea {dias_anio:1f} días completos escuchando a {artista}!\n")