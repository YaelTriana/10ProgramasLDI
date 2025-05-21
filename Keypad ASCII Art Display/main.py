# Descripción: Este programa utiliza el OLED Display para mostrar emojis
#              correspondientes a las teclas presionadas en el keypad.

from machine import Pin, I2C
import ssd1306
import time

# Configuración del keypad 4x4
filas = [Pin(pin, Pin.OUT) for pin in [28, 27, 26, 22]]  # Filas: GP22, GP26, GP27, GP28
columnas = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in [21, 20, 19, 18]]  # Columnas: GP18 a GP21

# Mapeo de teclas (orden matricial)
teclas = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# Mapeo de ASCII art para cada tecla
ascii_art = {
    '1': [':)',     # Cara sonriente
          ''],
    '2': ['8-)',    # Cara con lentes
          ''],
    '3': [':-?',    # Cara pensativa
          ''],
    'A': ['/\\',    # Letra A
          '--'],
    '4': ['<3',     # Corazón
          ''],
    '5': ['\\o/',   # Celebración
          ''],
    '6': ['/\\',    # Cohete
          '||'],
    'B': ['|3',     # Letra B
          '|3'],
    '7': [' *',     # Estrella
          '***'],
    '8': ['♪♫',     # Notas musicales
          ''],
    '9': [' ★',     # Estrella grande
          '***'],
    'C': ['(C)',    # Copyright
          ''],
    '*': [' *',     # Estrella
          '* *'],
    '0': ['(0)',    # Círculo
          ''],
    '#': ['###',    # Hash/numeral
          '###'],
    'D': ['|)',     # Letra D
          '|)']
}

# Configuración OLED (I2C)
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def limpiar_oled():
    oled.fill(0)
    oled.show()

def dibujar_tecla_con_ascii(tecla):
    limpiar_oled()
    
    # Mostrar la tecla presionada
    oled.text("Tecla: " + tecla, 30, 5)
    
    # Obtener el ASCII art correspondiente
    art = ascii_art.get(tecla, ['?', '?'])  # ASCII por defecto si no se encuentra
    
    # Mostrar el ASCII art (2 líneas máximo)
    oled.text(art[0], 45, 25)  # Primera línea del ASCII
    if len(art) > 1 and art[1]:  # Segunda línea si existe
        oled.text(art[1], 45, 35)
    
    # Mostrar descripción
    descripciones = {
        '1': 'Sonrisa',
        '2': 'Cool',
        '3': 'Pensando',
        'A': 'Letra A',
        '4': 'Amor',
        '5': 'Fiesta',
        '6': 'Cohete',
        'B': 'Letra B',
        '7': 'Estrella',
        '8': 'Musica',
        '9': 'Brillo',
        'C': 'Copyright',
        '*': 'Chispas',
        '0': 'Cero',
        '#': 'Numeral',
        'D': 'Letra D'
    }
    
    descripcion = descripciones.get(tecla, 'Desconocido')
    oled.text(descripcion, 5, 55)
    
    oled.show()

def leer_keypad():
    for i in range(4):
        filas[i].value(1)  # Activar fila
        for j in range(4):
            if columnas[j].value() == 1:  # Detectar columna
                filas[i].value(0)  # Desactivar fila antes de retornar
                return teclas[i][j]
        filas[i].value(0)  # Desactivar fila
    return None

# Mensaje inicial
limpiar_oled()
oled.text("Presiona una", 15, 10)
oled.text("tecla para", 20, 25)
oled.text("ver ASCII!", 15, 40)
oled.show()

# Bucle principal
while True:
    tecla = leer_keypad()
    if tecla is not None:
        dibujar_tecla_con_ascii(tecla)
        time.sleep(0.3)  # Anti-rebote