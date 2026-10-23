print("\n──── ୨୧ ────")
print("Ejercicio 8: Mi tiempo en pantalla realizado por Renata")
print("\n──── ୨୧ ──── TIEMPO DE PANTALLA ──── ୨୧ ────")
# Damos de alta la variable app y las horas que paso al día 
app = "Tiktok"
horas_diarias = 5 
print(f"\nPaso {horas_diarias} horas diarias en {app}")

# Calculamos las horas al año, esta formula dice: horas_anio = 5 * 365
horas_anio = horas_diarias * 365
print(f"Al año son {horas_anio} horas")

#Covertimos las horas a días completos (1 día tiene 24 horas)
#Esta formula dice: dias_anio = 1825 / 24, que da 76.0416666
dias_anio = horas_anio / 24 
#El :.1f muestra solo 1 decimal, así que se ve 76.0
print(f"¡Eso equivale a {dias_anio:.1f} días completos sin parar!")

#Calculamos cuántos meses son (un mes tiene aprox. 30 días)
#Esta formula dice: meses = 76.0 / 30 
meses = dias_anio / 30
print(f"\nO sea, casi {meses:.1f} meses de mi año se van en {app}\n")
print("──── ୨୧ ────")