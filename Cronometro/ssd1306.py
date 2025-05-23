# ssd1306.py (versión mínima)
import framebuf

class SSD1306_I2C:
    def __init__(self, width, height, i2c, addr=0x3c):
        self.width = width
        self.height = height
        self.i2c = i2c
        self.addr = addr
        self.buffer = bytearray(self.height * self.width // 8)
        self.framebuf = framebuf.FrameBuffer(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.init_display()

    def init_display(self):
        for cmd in (
            0xae, 0x20, 0x00, 0x40, 0xa1, 0xc8, 0xa6, 0xa4,
            0xd3, 0x00, 0xd5, 0xf0, 0xd9, 0x22, 0xda, 0x12,
            0xdb, 0x20, 0x8d, 0x14, 0xaf
        ):
            self.write_cmd(cmd)
        self.show()

    def write_cmd(self, cmd):
        self.i2c.writeto(self.addr, bytearray([0x80, cmd]))

    def show(self):
        for page in range(0, self.height // 8):
            self.write_cmd(0xb0 + page)
            self.write_cmd(0x00)
            self.write_cmd(0x10)
            start = self.width * page
            self.i2c.writeto(self.addr, bytearray([0x40]) + self.buffer[start:start + self.width])

    def fill(self, c):
        self.framebuf.fill(c)

    def text(self, s, x, y):
        self.framebuf.text(s, x, y)

    def pixel(self, x, y, c):
        self.framebuf.pixel(x, y, c)

    def line(self, x1, y1, x2, y2, c):
        self.framebuf.line(x1, y1, x2, y2, c)

    def fill_rect(self, x, y, w, h, c):
        self.framebuf.fill_rect(x, y, w, h, c)

    def circle(self, x, y, r, c):
        for i in range(360):
            _x = int(x + r * math.cos(i * 3.14 / 180))
            _y = int(y + r * math.sin(i * 3.14 / 180))
            self.pixel(_x, _y, c)
