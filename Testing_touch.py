from machine import Pin, SPI
from xpt2046 import Touch
from ili9341 import Display, color565
from xglcd_font import XglcdFont
from touch_keyboard import TouchKeyboard
from time import sleep


unispace = XglcdFont('Unispace12x24.c', 12, 24)
spi1 = SPI(1, baudrate=51200000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
spi2 = SPI(2, baudrate=1000000,sck=Pin(18), mosi=Pin(23), miso=Pin(19))
display = Display(spi1, dc=Pin(4), cs=Pin(16), rst=Pin(17),width=320, height=240, rotation=90)


def touchscreen_press( x, y):
        """Process touchscreen press events."""
        x,y=y,x
        print('Triggered')
        display.clear()
        display.draw_text(60, 120, ' enter email ', unispace, color565(255, 255, 255),background=color565(0, 122, 55))

xpt = Touch(spi2, cs=Pin(5), int_pin=Pin(12), int_handler=touchscreen_press)
display.draw_text(60, 120, ' hello ', unispace, color565(255, 255, 255),background=color565(0, 122, 55))



