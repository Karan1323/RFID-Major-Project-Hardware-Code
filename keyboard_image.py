"""Search online for pwned passwords."""
from machine import Pin, SPI
from xpt2046 import Touch
from ili9341 import Display, color565
from xglcd_font import XglcdFont
from touch_keyboard import TouchKeyboard
from time import sleep


class PwnLookup(object):
    """Checks if password is pwned."""

    def __init__(self, spi1, spi2, dc=4, cs1=16, rst=17, cs2=5, rotation=90):
        """Initialize PwnLookup."""
        # Set up display
        self.display = Display(spi1, dc=Pin(dc), cs=Pin(cs1), rst=Pin(rst),
                               width=320, height=240, rotation=rotation)

        # Load font
        self.unispace = XglcdFont('Unispace12x24.c', 12, 24)

        # Set up Keyboard
        self.keyboard = TouchKeyboard(self.display, self.unispace)

        # Set up touchscreen
        self.xpt = Touch(spi2, cs=Pin(cs2), int_pin=Pin(33),
                         int_handler=self.touchscreen_press)

    def lookup(self, pwd):

        sha1pwd = sha1(pwd.encode('utf-8')).digest()
        sha1pwd = hexlify(sha1pwd).upper().decode('utf-8')
        head, tail = sha1pwd[:5], sha1pwd[5:]

       

    def touchscreen_press(self, x, y):
        """Process touchscreen press events."""
        if self.keyboard.handle_keypress(x, y, debug=False) is True:
            self.keyboard.locked = True
            pwd = self.keyboard.kb_text

            self.keyboard.show_message("Searching...", color565(0, 0, 255))
            try:
                hits = self.lookup(pwd)

                if hits:
                    # Password found
                    msg = "PASSWORD HITS: {0}".format(hits)
                    self.keyboard.show_message(msg, color565(255, 0, 0))
                else:
                    # Password not found
                    msg = "PASSWORD NOT FOUND"
                    self.keyboard.show_message(msg, color565(0, 255, 0))
            except Exception as e:
                if hasattr(e, 'message'):
                    self.keyboard.show_message(e.message[:22],
                                               color565(255, 255, 255))
                else:
                    self.keyboard.show_message(str(e)[:22],
                                               color565(255, 255, 255))

            self.keyboard.waiting = True
            self.keyboard.locked = False


def main():
    """Start PwnLookup."""
    spi1 = SPI(1, baudrate=51200000,
               sck=Pin(14), mosi=Pin(13), miso=Pin(12))
    spi2 = SPI(2, baudrate=1000000,
               sck=Pin(18), mosi=Pin(23), miso=Pin(19))

    PwnLookup(spi1, spi2)

    while True:
        sleep(.1)


main()