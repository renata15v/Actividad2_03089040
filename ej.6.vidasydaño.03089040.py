print("\n°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･")
print("Ejercicio 6: vidas y daño")
print("°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･ BATALLA °❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･")
# Damos de alta las variables personaje y vida
personaje = "Suki"
vida = 100
print(f"\nMi personaje se llama {personaje} y empieza con {vida} de vida")
# Como vida vale 100, esta formula dice: vida = 100 - 20
vida = vida - 20
print(f"Me dio un golpe un zombi, ahora tengo vida: {vida}")
# Ahora vida vale 80, esta formula dice: vida = 80 - 35 
vida = vida - 35
print(f"Ah, ahora me tocó el golpe de bruja, tengo de vida: {vida}")
# Ahora vida vale 45, esta formula dice: vida = 45 - 15
vida = vida - 15 
print(f"Me tocó una flecha enemiga!!, tengo de vida: {vida}")
# Ahora vida vale 20, esta formula dice: vida = 30 + 20
vida = vida + 30 
print(f"Tomo una poción... mi vida: {vida}")

print(f"\n {personaje} terminó la batalla con {vida} HP\n")
print("°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･")