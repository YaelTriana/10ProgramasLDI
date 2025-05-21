# Descripción: Juego de memoria que muestra una secuencia de teclas en el OLED
#              y el jugador debe repetir la secuencia usando el keypad

from machine import Pin, I2C
import ssd1306
import time
import random

# Configuración del keypad 4x4
filas = [Pin(pin, Pin.OUT) for pin in [28, 27, 26, 22]]
columnas = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in [21, 20, 19, 18]]

# Mapeo de teclas
teclas = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# Configuración OLED
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Variables del juego
secuencia = []
entrada_jugador = []
nivel = 1
puntuacion = 0
estado_juego = "inicio"  # inicio, mostrando, esperando, correcto, incorrecto, fin

# Teclas válidas para el juego (solo números)
teclas_juego = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def limpiar_oled():
    oled.fill(0)
    oled.show()

def mostrar_pantalla_inicio():
    limpiar_oled()
    oled.text("JUEGO MEMORIA", 20, 10)
    oled.text("Nivel: " + str(nivel), 45, 25)
    oled.text("Puntos: " + str(puntuacion), 35, 35)
    oled.text("Presiona # para", 15, 50)
    oled.text("comenzar", 35, 60)
    oled.show()

def mostrar_secuencia():
    global estado_juego
    estado_juego = "mostrando"
    
    for i, tecla in enumerate(secuencia):
        limpiar_oled()
        oled.text("Memoriza:", 30, 10)
        oled.text("Secuencia " + str(i+1) + "/" + str(len(secuencia)), 20, 25)
        
        # Mostrar la tecla con un marco
        oled.rect(50, 35, 30, 20, 1)
        oled.text(tecla, 60, 42)
        oled.show()
        time.sleep(1)
        
        # Pausa entre teclas
        limpiar_oled()
        oled.text("...", 60, 42)
        oled.show()
        time.sleep(0.5)
    
    # Mostrar instrucciones
    limpiar_oled()
    oled.text("Tu turno!", 40, 15)
    oled.text("Repite la", 40, 30)
    oled.text("secuencia:", 35, 40)
    oled.text("* = Reiniciar", 20, 55)
    oled.show()
    
    estado_juego = "esperando"

def mostrar_entrada_actual():
    limpiar_oled()
    oled.text("Entrada:", 40, 5)
    oled.text(str(len(entrada_jugador)) + "/" + str(len(secuencia)), 50, 15)
    
    # Mostrar las teclas ingresadas
    entrada_str = "".join(entrada_jugador[-8:])  # Mostrar últimas 8 teclas
    oled.text(entrada_str, 10, 30)
    
    # Mostrar progreso
    for i in range(len(secuencia)):
        x = 10 + i * 12
        if i < len(entrada_jugador):
            oled.rect(x, 45, 10, 8, 1)  # Completo
        else:
            oled.rect(x, 45, 10, 8, 1)  # Solo borde
    
    oled.text("*=Reset", 5, 58)
    oled.show()

def verificar_entrada():
    global estado_juego, puntuacion, nivel
    
    if len(entrada_jugador) == len(secuencia):
        if entrada_jugador == secuencia:
            # ¡Correcto!
            estado_juego = "correcto"
            puntuacion += nivel * 10
            nivel += 1
            
            limpiar_oled()
            oled.text("CORRECTO!", 30, 20)
            oled.text("Puntos: " + str(puntuacion), 30, 35)
            oled.text("Nivel: " + str(nivel), 40, 45)
            oled.show()
            time.sleep(2)
            
            # Preparar siguiente nivel
            generar_secuencia()
            estado_juego = "inicio"
        else:
            # Incorrecto
            estado_juego = "fin"
            mostrar_game_over()

def mostrar_game_over():
    limpiar_oled()
    oled.text("GAME OVER", 30, 15)
    oled.text("Nivel: " + str(nivel-1), 40, 30)
    oled.text("Puntos: " + str(puntuacion), 30, 40)
    oled.text("# = Nuevo Juego", 15, 55)
    oled.show()

def generar_secuencia():
    global secuencia
    secuencia = []
    for _ in range(nivel + 2):  # Secuencia crece con el nivel
        secuencia.append(random.choice(teclas_juego))

def reiniciar_juego():
    global secuencia, entrada_jugador, nivel, puntuacion, estado_juego
    secuencia = []
    entrada_jugador = []
    nivel = 1
    puntuacion = 0
    estado_juego = "inicio"
    generar_secuencia()

def leer_keypad():
    for i in range(4):
        filas[i].value(1)
        for j in range(4):
            if columnas[j].value() == 1:
                filas[i].value(0)
                return teclas[i][j]
        filas[i].value(0)
    return None

def procesar_tecla(tecla):
    global entrada_jugador, estado_juego
    
    if estado_juego == "inicio":
        if tecla == '#':
            mostrar_secuencia()
    
    elif estado_juego == "esperando":
        if tecla == '*':
            # Reiniciar entrada actual
            entrada_jugador = []
            mostrar_entrada_actual()
        elif tecla in teclas_juego:
            entrada_jugador.append(tecla)
            mostrar_entrada_actual()
            
            # Verificar si la entrada hasta ahora es correcta
            if entrada_jugador != secuencia[:len(entrada_jugador)]:
                estado_juego = "fin"
                mostrar_game_over()
            else:
                verificar_entrada()
    
    elif estado_juego == "fin":
        if tecla == '#':
            reiniciar_juego()
            mostrar_pantalla_inicio()

# Inicialización
reiniciar_juego()

# Pantalla de bienvenida
limpiar_oled()
oled.text("BIENVENIDO AL", 20, 15)
oled.text("JUEGO DE", 35, 30)
oled.text("MEMORIA", 40, 45)
oled.show()
time.sleep(3)

mostrar_pantalla_inicio()

# Bucle principal
while True:
    tecla = leer_keypad()
    if tecla is not None:
        procesar_tecla(tecla)
        time.sleep(0.3)  # Anti-rebote