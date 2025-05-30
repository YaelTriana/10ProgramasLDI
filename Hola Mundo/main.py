
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf, sys
import utime

pix_res_x = 128
pix_res_y = 64

def init_i2c(scl_pin, sda_pin):
    # Initialize I2C device
    i2c_dev = I2C(1, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=200000)
    i2c_addr = [hex(ii) for ii in i2c_dev.scan()]
    
    if not i2c_addr:
        print('No I2C Display Found')
        sys.exit()
    else:
        print("I2C Address      : {}".format(i2c_addr[0]))
        print("I2C Configuration: {}".format(i2c_dev))
    
    return i2c_dev

def display_logo(oled):
    # Display the Raspberry Pi logo on the OLED
    buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)
    
    oled.fill(0)
    oled.blit(fb, 96, 0)
    oled.show()

def display_text(oled):
    # Display text on the OLED
    oled.text("Raspberry Pi", 5, 5)
    oled.text("Pico", 5, 15)
    oled.text("Hola Mundo", 5, 25)
    oled.show()


def main():
    i2c_dev = init_i2c(scl_pin=27, sda_pin=26)
    oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)
    display_logo(oled)
    display_text(oled)
    display_anima(oled)

if __name__ == '__main__':
    main()
