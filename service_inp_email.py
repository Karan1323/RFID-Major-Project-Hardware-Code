from machine import Pin, SPI
from xpt2046 import Touch
from ili9341 import Display, color565
from xglcd_font import XglcdFont
from touch_keyboard import TouchKeyboard
import time
from test_mail import PwnLookup

spi1 = SPI(1, baudrate=51200000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
spi2 = SPI(2, baudrate=1000000,sck=Pin(18), mosi=Pin(23), miso=Pin(19))
display = Display(spi1, dc=Pin(4), cs=Pin(16), rst=Pin(17),width=320, height=240, rotation=90)
unispace = XglcdFont('Unispace12x24.c', 12, 24)

xpt=None

def touchscreen_press(x, y):
    """Process touchscreen press events."""
    x,y=y,x
    if (x>=80 and x<=120) and (y>=120 and y<=150) :
    
        display.clear()
        display.draw_text(5, 15, ' Enter Your E-Mail ID: ', unispace, color565(255, 255, 255))

        display.draw_hline(5, 55, 310, color565(255, 255, 255))
        display.draw_hline(5, 100, 310, color565(255, 255, 255))
        display.draw_vline(5, 55, 45, color565(255, 255, 255))
        display.draw_vline(315, 55, 45, color565(255, 255, 255))
        time.sleep(5)
#         xpt.int_handler=None
#         xpt.int_pin=None
        p=PwnLookup(spi1,spi2)
        while p.exit==False:
            time.sleep(25)
        del p
        print('deleted p')

    
    elif (x>=160 and x<=200) and (y>=120 and y<=150) :
    
        display.clear()
        display.draw_text(5, 45, ' Dont want ', unispace, color565(255, 255, 255))
        time.sleep(2)
        display.clear()
        return None
    

    
def ask_service():      

    xpt=Touch(spi2, cs=Pin(5), int_pin=Pin(12), int_handler= touchscreen_press)
    display.draw_text(5, 15, ' Do you want to register to', unispace, color565(255, 255, 255))
    display.draw_text(5, 45, ' the service? ', unispace, color565(255, 255, 255))


    display.draw_text(60, 120, ' Yes ', unispace, color565(255, 255, 255),background=color565(0, 122, 55))

    display.draw_text(160, 120, ' No  ', unispace, color565(255, 255, 255),background=color565(255, 0, 0))
    while xpt.int_pin!=None and xpt.int_handler!=None:
        continue
    print('Finished Execution')
        

ask_service()
#print('Finished Execution')



