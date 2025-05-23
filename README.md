# 🚀 Colección de 10 Proyectos con Raspberry Pi Pico en Wokwi

Esta colección presenta 10 proyectos completos desarrollados para **Raspberry Pi Pico** usando **MicroPython** en el simulador **Wokwi**. Cada proyecto está diseñado para ser educativo, funcional y fácil de implementar.

## 📋 Índice de Proyectos


| #  | Proyecto                 | Componentes            | Dificultad    | Descripción                                   |
| -- | ------------------------ | ---------------------- | ------------- | --------------------------------------------- |
| 1  | Keypad ASCII Art Display | Keypad 4x4, OLED       | 🟢 Básico     | Muestra arte ASCII al presionar teclas        |
| 2  | Calculadora Simple       | Keypad 4x4, OLED       | 🟡 Intermedio | Calculadora con operaciones básicas           |
| 3  | Juego de Memoria         | Keypad 4x4, OLED       | 🟡 Intermedio | Memoriza y repite secuencias                  |
| 4  | Alarma                   | Buzzer, RTC (reloj)    | 🟡 Intermedio | Alarma programable con señal sonora           |
| 5  | Cronómetro               | Pantalla OLED, botones | 🟢 Básico     | Cronómetro con inicio, pausa y reset          |
| 6  | Hola Mundo               | Pantalla OLED          | 🟢 Básico     | Muestra texto "Hola Mundo" en pantalla        |
| 7  | Mini-piano               | Teclado, buzzer        | 🟢 Básico     | Mini piano con sonidos en buzzer              |
| 8  | Prender LED              | LED, botón             | 🟢 Básico     | Enciende y apaga LED con botón                |
| 9  | Temporizador Pantalla    | OLED, botones          | 🟡 Intermedio | Temporizador con cuenta regresiva en pantalla |

## 🔧 Configuración General

### Componentes Comunes
- **Raspberry Pi Pico** (simulado en Wokwi)
- **Display OLED SSD1306** (128x64, I2C)
- **Keypad Matricial 4x4**
- **Cables de conexión**

### Conexiones Base OLED (I2C)
```
OLED SSD1306 -> Raspberry Pi Pico
VCC -> 3.3V
GND -> GND
SDA -> GP0
SCL -> GP1
```

### Conexiones Base Keypad 4x4
```
Keypad -> Raspberry Pi Pico
Filas: GP22, GP26, GP27, GP28
Columnas: GP18, GP19, GP20, GP21
```

## 📂 Estructura de Proyectos

Cada proyecto incluye:
- 📄 **Código fuente** (.py)
- 🔌 **Diagrama de conexiones**
- 📚 **Documentación específica**
- 🎯 **Casos de uso**

## 🎯 Proyectos Detallados

### 1. Keypad ASCII Art Display
**Componentes:** Keypad 4x4, OLED SSD1306
**Función:** Muestra arte ASCII personalizado para cada tecla presionada
**Aprendizaje:** Manejo de keypad, displays OLED, arte ASCII

### 2. Calculadora Simple
**Componentes:** Keypad 4x4, OLED SSD1306
**Función:** Calculadora con operaciones básicas (+, -, *, /)
**Aprendizaje:** Lógica matemática, manejo de estados, interfaces de usuario

### 3. Juego de Memoria
**Componentes:** Keypad 4x4, OLED SSD1306
**Función:** Juego que genera secuencias para memorizar y repetir
**Aprendizaje:** Algoritmos de juego, gestión de puntuaciones, lógica secuencial



## 🛠️ Instrucciones de Uso

### Para Wokwi:
1. **Crear nuevo proyecto** en [wokwi.com](https://wokwi.com)
2. **Seleccionar** "Raspberry Pi Pico"
3. **Agregar componentes** según el proyecto
4. **Copiar el código** correspondiente
5. **Conectar componentes** según el diagrama
6. **Ejecutar simulación**

### Instalación Local:
```bash
# Instalar Thonny IDE
# Conectar Raspberry Pi Pico
# Instalar MicroPython firmware
# Copiar archivos .py al Pico
```

## 📚 Bibliotecas Utilizadas

```python
# Bibliotecas estándar de MicroPython
from machine import Pin, I2C, PWM, SPI
import ssd1306        # Display OLED
import time           # Manejo de tiempo
import random         # Números aleatorios
import onewire        # Protocolo OneWire
import ds18x20        # Sensor temperatura
import dht            # Sensor DHT22/DHT11
```

## 🎓 Objetivos de Aprendizaje

### Nivel Básico:
- ✅ Configuración de pines GPIO
- ✅ Lectura de sensores digitales
- ✅ Control de displays
- ✅ Manejo de interrupciones

### Nivel Intermedio:
- ✅ Comunicación I2C/SPI
- ✅ Máquinas de estado
- ✅ Interfaces de usuario
- ✅ Algoritmos de control

### Nivel Avanzado:
- ✅ Sistemas multi-componente
- ✅ Manejo de archivos
- ✅ Protocolos de comunicación
- ✅ Optimización de código

## 🔍 Troubleshooting

### Problemas Comunes:

**OLED no muestra nada:**
- Verificar conexiones I2C (SDA/SCL)
- Comprobar dirección I2C (0x3C o 0x3D)
- Revisar alimentación (3.3V)

**Keypad no responde:**
- Verificar conexiones de filas y columnas
- Comprobar configuración pull-down
- Revisar anti-rebote en código

**Sensor no lee valores:**
- Verificar alimentación del sensor
- Comprobar protocolo de comunicación
- Revisar timing en el código

## 📈 Extensiones Sugeridas

### Mejoras Posibles:
- 🌐 **Conectividad WiFi** para IoT
- 📱 **Interfaz web** para control remoto
- 🔋 **Optimización energética** para batería
- 📊 **Visualización de datos** avanzada
- 🔔 **Notificaciones** push
- 🗄️ **Base de datos** local

## 👥 Contribuciones

¡Las contribuciones son bienvenidas! Para contribuir:

1. Fork del repositorio
2. Crear rama para nueva característica
3. Commit de cambios
4. Push a la rama
5. Crear Pull Request


#

---

**¡Disfruta programando con Raspberry Pi Pico!**
