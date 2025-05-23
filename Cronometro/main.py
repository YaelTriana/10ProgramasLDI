from machine import Pin, I2C, PWM
import ssd1306
import time

# Configuración OLED
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Botones
btn_up = Pin(14, Pin.IN, Pin.PULL_UP) #Botón azul
btn_down = Pin(15, Pin.IN, Pin.PULL_UP) #Botón verde
btn_start = Pin(16, Pin.IN, Pin.PULL_UP) #Botón amarillo

# Buzzer (activo)
buzzer = PWM(Pin(17))
buzzer.duty_u16(0)  # Silencio al inicio

# Variables
tiempo = 20  # segundos iniciales
corriendo = False

# Función para mostrar el tiempo en formato mm:ss
def mostrar_tiempo(segundos):
    oled.fill(0)
    minutos = segundos // 60
    segs = segundos % 60
    oled.text("Temporizador", 10, 0)
    oled.text("{:02}:{:02}".format(minutos, segs), 30, 24)
    oled.text("Start: Amarillo", 0, 48)
    oled.show()

# Función para reproducir alarma
def sonar_alarma():
    for _ in range(5):
        buzzer.freq(1000)
        buzzer.duty_u16(30000)
        time.sleep(0.3)
        buzzer.duty_u16(0)
        time.sleep(0.2)

# Bucle principal
while True:
    mostrar_tiempo(tiempo)

    if not btn_up.value():
        tiempo += 10
        time.sleep(0.3)
    elif not btn_down.value() and tiempo >= 10:
        tiempo -= 10
        time.sleep(0.3)
    elif not btn_start.value():
        corriendo = True
        while tiempo > 0 and corriendo:
            tiempo -= 1
            mostrar_tiempo(tiempo)
            time.sleep(1)
            if not btn_start.value():
                corriendo = False
                time.sleep(0.3)

        if tiempo == 0:
            mostrar_tiempo(tiempo)
            sonar_alarma()
            time.sleep(2)
            tiempo = 60  # Reiniciar temporizador