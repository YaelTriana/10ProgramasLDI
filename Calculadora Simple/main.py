# Descripción: Calculadora simple que usa el keypad 4x4 para ingresar números
#              y operaciones, mostrando los resultados en el OLED

from machine import Pin, I2C
import ssd1306
import time

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

# Variables de la calculadora
numero_actual = ""
numero_anterior = ""
operacion = ""
resultado = 0
esperando_numero = True

def limpiar_oled():
    oled.fill(0)
    oled.show()

def mostrar_calculadora():
    limpiar_oled()
    
    # Mostrar operación completa en la parte superior
    if numero_anterior and operacion:
        operacion_text = numero_anterior + " " + operacion
        oled.text(operacion_text, 5, 5)
    
    # Mostrar número actual o resultado
    if numero_actual:
        # Limitar a 10 caracteres para que quepa en pantalla
        texto_numero = numero_actual[-10:]
        oled.text(texto_numero, 5, 20)
    else:
        oled.text("0", 5, 20)
    
    # Línea separadora
    for x in range(128):
        oled.pixel(x, 35, 1)
    
    # Instrucciones
    oled.text("A=+ B=- C=* D=/", 5, 45)
    oled.text("*=Borrar #=Igual", 5, 55)
    
    oled.show()

def leer_keypad():
    for i in range(4):
        filas[i].value(1)
        for j in range(4):
            if columnas[j].value() == 1:
                filas[i].value(0)
                return teclas[i][j]
        filas[i].value(0)
    return None

def realizar_calculo():
    global resultado, numero_anterior, numero_actual, operacion
    
    try:
        num1 = float(numero_anterior) if numero_anterior else 0
        num2 = float(numero_actual) if numero_actual else 0
        
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                return "Error: Div/0"
        
        # Convertir a entero si es un número entero
        if resultado == int(resultado):
            resultado = int(resultado)
        
        return str(resultado)
    except:
        return "Error"

def procesar_tecla(tecla):
    global numero_actual, numero_anterior, operacion, esperando_numero
    
    # Números 0-9
    if tecla in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if esperando_numero:
            numero_actual = tecla
            esperando_numero = False
        else:
            numero_actual += tecla
    
    # Operaciones: A=+, B=-, C=*, D=/
    elif tecla in ['A', 'B', 'C', 'D']:
        if numero_actual:
            if numero_anterior and operacion:
                # Realizar cálculo previo
                resultado_prev = realizar_calculo()
                if "Error" not in resultado_prev:
                    numero_anterior = resultado_prev
                    numero_actual = ""
                else:
                    numero_anterior = ""
                    numero_actual = resultado_prev
                    return
            else:
                numero_anterior = numero_actual
                numero_actual = ""
            
            # Asignar nueva operación
            if tecla == 'A':
                operacion = "+"
            elif tecla == 'B':
                operacion = "-"
            elif tecla == 'C':
                operacion = "*"
            elif tecla == 'D':
                operacion = "/"
            
            esperando_numero = True
    
    # Igual (#)
    elif tecla == '#':
        if numero_anterior and operacion and numero_actual:
            resultado_final = realizar_calculo()
            numero_actual = resultado_final
            numero_anterior = ""
            operacion = ""
            esperando_numero = True
    
    # Borrar (*)
    elif tecla == '*':
        numero_actual = ""
        numero_anterior = ""
        operacion = ""
        esperando_numero = True

# Pantalla inicial
limpiar_oled()
oled.text("CALCULADORA", 25, 15)
oled.text("A=+ B=- C=* D=/", 5, 35)
oled.text("Presiona numeros", 10, 50)
oled.show()
time.sleep(2)

# Bucle principal
while True:
    tecla = leer_keypad()
    if tecla is not None:
        procesar_tecla(tecla)
        mostrar_calculadora()
        time.sleep(0.3)  # Anti-rebote