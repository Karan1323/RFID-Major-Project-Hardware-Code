from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from test_mail import PwnLookup
import time
from yes_no import Yes_or_no
from config import con_initial

spi1,spi2,display,unispace=con_initial

# unispace = XglcdFont('Unispace12x24.c', 12, 24)
# spi1 = SPI(1, baudrate=51200000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
# spi2 = SPI(2, baudrate=1000000,sck=Pin(18), mosi=Pin(23), miso=Pin(19))
# display = Display(spi1, dc=Pin(4), cs=Pin(16), rst=Pin(17),width=320, height=240, rotation=90)

def to_exit_Touch(p):
    while not p.exit:
        continue
    print('out of loop ')
    del p
    print('Done')
    
def to_exit_Touch_yn(p):
    while not p.exit:
        continue
    print('out of loop ')
        

def runnn():
  
    yn=Yes_or_no()
    to_exit_Touch_yn(yn)
    if yn.option=='y':
        print('inside yes block')
        del yn
        
        display.clear()
        display.draw_text(5, 15, ' Enter Your E-Mail ID: ', unispace, color565(255, 255, 255))

#         display.draw_hline(5, 55, 310, color565(255, 255, 255))
#         display.draw_hline(5, 100, 310, color565(255, 255, 255))
#         display.draw_vline(5, 55, 45, color565(255, 255, 255))
#         display.draw_vline(315, 55, 45, color565(255, 255, 255))
        time.sleep(5)
        display.clear()
        p=PwnLookup()
        to_exit_Touch(p)
        
    else:
        del yn
        display.clear()
        display.draw_text(5, 15, ' Registration Incomplete ', unispace, color565(255, 255, 255))
        
    display.clear()  
    display.draw_text(5, 15, ' Scan Your Card... ', unispace, color565(255, 255, 255))
        
      
#     else:
#         del yn
#         display.clear()
#         display.draw_text(5, 15, ' choose correct option ', unispace, color565(255, 255, 255)) 
    
#runnn()






