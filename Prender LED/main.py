import machine
import time
from machine import Pin, I2C
import ssd1306  # Asegúrate de que el archivo ssd1306.py esté cargado

time.sleep(0.1)  # Espera a que el USB esté listo

print("Hello, Pi Pico!")

# Inicialización de los LEDs
led_junior_1 = Pin(5, Pin.OUT)
led_junior_2 = Pin(9, Pin.OUT)
led_junior_3 = Pin(13, Pin.OUT)

# Configuración de la pantalla OLED (I2C)
i2c = I2C(0, scl=Pin(1), sda=Pin(0))  # Usa los pines GP1 (SCL) y GP0 (SDA)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # Tamaño típico: 128x64

def mostrar_estado(led_num, estado):
    oled.fill(0)  # Limpia la pantalla
    mensaje = f"LED {led_num}: {estado}"
    oled.text("Control de LEDs", 0, 0)
    oled.text(mensaje, 0, 20)
    oled.show()

while True:
    # LED 1
    led_junior_1.on()
    print("verde encendido")
    mostrar_estado(1, "encendido")
    time.sleep(5)
    led_junior_1.off()
    print("verde apagado")
    mostrar_estado(1, "apagado")
    time.sleep(0.5)

    # LED 2
    led_junior_2.on()
    print("verde encendido")
    mostrar_estado(2, "encendido")
    time.sleep(5)
    led_junior_2.off()
    print("verde apagado")
    mostrar_estado(2, "apagado")
    time.sleep(0.5)

    # LED 3
    led_junior_3.on()
    print("verde encendido")
    mostrar_estado(3, "encendido")
    time.sleep(5)
    led_junior_3.off()
    print("verde apagado")
    mostrar_estado(3, "apagado")
    time.sleep(0.5)
