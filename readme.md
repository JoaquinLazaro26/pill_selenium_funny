# 🤖 Pill Selenium: Bot Automático para 2048

¡Bienvenido al repositorio **pill_selenium_funny**! 🚀

Este proyecto es una pequeña píldora educativa para aprender a utilizar **Python** y **Selenium**. El objetivo es crear un bot sencillo que "juegue" automáticamente al famoso juego [2048](https://play2048.co/) enviando comandos de teclado y detectando cuándo termina la partida.

## 📋 Requisitos Previos

Antes de empezar, asegúrate de tener instalado lo siguiente en tu ordenador:

1.  **Python 3.x**: [Descargar Python](https://www.python.org/downloads/)
2.  **Google Chrome**: El navegador donde se ejecutará el bot.
3.  **Git**: Para clonar este repositorio.

## 🛠️ Instalación y Configuración (Paso a Paso)

Sigue estos pasos para poner en marcha tu bot:

### 1. Clonar el repositorio
Descarga el código en tu máquina local usando la terminal:

```bash
git clone https://github.com/JoaquinLazaro26/pill_selenium_funny.git
cd pill_selenium_funny
```

### 2. Crear un entorno virtual (Opcional pero recomendado)
Para mantener las librerías ordenadas, crea un entorno virtual:

*   **En Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
*   **En Mac/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### 3. Instalar las dependencias
Este bot necesita dos librerías principales: `selenium` (para controlar el navegador) y `webdriver-manager` (para gestionar el driver de Chrome automáticamente).

Ejecuta:
```bash
pip install selenium webdriver-manager
```

---

## 🎮 Cómo usar el Bot

Una vez instalado todo, ¡es hora de jugar!

1.  Ejecuta el script principal (asegúrate de que el archivo se llame `main.py` o el nombre que le hayas dado):

    ```bash
    python main.py
    ```

2.  **Configuración de Velocidad**:
    El programa te preguntará en la terminal a qué velocidad quieres que juegue:
    *   Escribe `1` para el modo **RÁPIDO Y FURIOSO** 🚀.
    *   Escribe `2` para el modo **TURISTA OBSERVADOR** 🐢.

3.  **El Navegador**:
    *   Se abrirá una ventana de Chrome automáticamente.
    *   Si aparece publicidad, **ciérrala manualmente**.
    *   Vuelve a la terminal y presiona **ENTER** cuando estés listo.

4.  **Disfruta**:
    El bot empezará a mover las fichas (Arriba, Derecha, Abajo, Izquierda) en bucle.
    *   El programa detectará automáticamente si aparece el mensaje de **"Game Over"** y se detendrá.
    *   Puedes detenerlo manualmente presionando `Ctrl + C` en la terminal.

---

## 🧠 ¿Cómo funciona el código?

Aquí tienes una breve explicación de lo que hace el script para esta "Pill":

*   **Driver Manager**: Usamos `ChromeDriverManager` para no tener que descargar manualmente el `chromedriver.exe`. El script lo hace por ti.
*   **Interacción**: Usamos `send_keys` para simular que una persona está presionando las flechas del teclado.
*   **Lógica de Bucle**: El bot entra en un `while True` enviando movimientos constantes.
*   **Detección de Game Over**:
    Usamos una estrategia de **Manejo de Excepciones**. El bot busca el texto "Game Over" en el HTML:
    ```python
    driver.find_element(By.XPATH, "//div[text()='Game Over']")
    ```
    Si lo encuentra, rompe el bucle y termina. Si no lo encuentra (`NoSuchElementException`), sigue jugando.

---

## 📂 Estructura del Proyecto

```text
pill_selenium_funny/
│
├── main.py            # El código fuente del bot
├── README.md          # Este archivo de instrucciones
└── .gitignore         # (Opcional) Para ignorar archivos del sistema
```

---

## 📝 Autor

Creado por **JoaquinLazaro26** como parte de una píldora formativa sobre automatización web.

¡Diviértete viendo cómo la IA (o bueno, un script básico) intenta ganar al 2048! 👾