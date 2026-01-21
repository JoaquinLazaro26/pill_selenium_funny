from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Necesario para pulsar teclas
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException # Para gestionar errores "no encontrado"
import time

# --- 1. CONFIGURACIÓN DEL CHÓFER (DRIVER) ---
# Preparamos las opciones. 'detach' es para que el navegador no se cierre solo al terminar.
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 

# Iniciamos el navegador (instala el driver automáticamente si falta)
# Necesitas tener Chrome instalado en tu sistema.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# --- 2. INTERACCIÓN INICIAL CON EL USUARIO ---
print("\n" + "🤖"*5 + " BIENVENIDO AL BOT DE 2048 " + "🤖"*5)
print("Este programa jugará automáticamente por ti.")

# Preguntamos al usuario qué velocidad prefiere
velocidad = input("¿A qué velocidad quieres que juegue? (1 = Rápido / 2 = Lento): ")

if velocidad == "1":
    tiempo_espera = 0.1 # Muy rápido
    print("🚀 Modo: RÁPIDO Y FURIOSO activado.")
else:
    tiempo_espera = 0.5 # Medio segundo entre movimientos
    print("🐢 Modo: TURISTA OBSERVADOR activado.")

# Vamos a la web
driver.get("https://play2048.co/")

print("\n" + "="*50)
print("👉 INSTRUCCIONES:")
print("1. Si sale publicidad, ciérrala.")
print("2. Asegúrate de que se ve el tablero.")
input("🟢 Cuando estés listo, PRESIONA ENTER AQUÍ para arrancar los motores...")
print("="*50 + "\n")

# Localizamos el "cuerpo" de la página web.
# Es como poner las manos sobre el teclado global de la web.
cuerpo_pagina = driver.find_element(By.TAG_NAME, "body")

print("👾 El bot ha tomado el control. Presiona Ctrl+C en la terminal para forzar la parada.")

# --- 3. BUCLE PRINCIPAL (EL CEREBRO DEL BOT) ---
ciclos = 0

while True:
    try:
        # --- A. ACCIÓN: Mover fichas ---
        # Enviamos las flechas del teclado al navegador
        cuerpo_pagina.send_keys(Keys.UP)
        cuerpo_pagina.send_keys(Keys.RIGHT)
        cuerpo_pagina.send_keys(Keys.DOWN)
        cuerpo_pagina.send_keys(Keys.LEFT)
        
        ciclos += 1
        # Imprimimos un puntito cada 10 ciclos para saber que está vivo sin llenar la pantalla
        if ciclos % 10 == 0:
            print(".", end="", flush=True) 

        # --- B. DECISIÓN: ¿Hemos perdido? ---
        try:
            # Intentamos buscar el texto exacto "Game Over".
            # Usamos XPATH porque nos permite buscar por TEXTO, no solo por clases raras.
            game_over_element = driver.find_element(By.XPATH, "//div[text()='Game Over']")
            
            # SI LLEGAMOS AQUÍ, es que Selenium ENCONTRÓ el elemento.
            print("\n\n" + "💀"*10)
            print(" ¡GAME OVER DETECTADO! ")
            print(f" El bot ha sobrevivido {ciclos} ciclos de movimientos.")
            print("💀"*10)
            break # <--- ¡IMPORTANTE! Esto rompe el bucle while y termina el juego.
           
        except NoSuchElementException:
            # Si Selenium NO encuentra el cartel "Game Over", salta aquí.
            # "pass" significa "no hagas nada, todo está bien, sigue jugando".
            pass
        
        # Respetamos la velocidad que eligió el usuario
        time.sleep(tiempo_espera)

    except Exception as e:
        # Si pasa algo muy raro (se cierra el navegador, se va internet...)
        print(f"\n❌ Error inesperado: {e}")
        driver.quit() # Cerramos el navegador, libera recursos
        driver.close() # Cerramos la ventana, no libera recursos
        break

print("\n🏁 Fin del programa.")