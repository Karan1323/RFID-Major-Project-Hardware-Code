from ili9341 import Display, color565
from machine import  Pin, SPI, SoftSPI
import time
from xglcd_font import XglcdFont

unispace = XglcdFont('Unispace12x24.c', 12, 24)
spi1 = SPI(1, baudrate=51200000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
spi2 = SPI(2, baudrate=1000000,sck=Pin(18), mosi=Pin(23), miso=Pin(19))
display = Display(spi1, dc=Pin(4), cs=Pin(16), rst=Pin(17),width=320, height=240, rotation=90)
    
display.draw_text(5, 15, '  REGISTRATION CANCELLED!', unispace, color565(255, 0, 0))


display.draw_image('canc.raw', 90,65, 130, 130)





    


