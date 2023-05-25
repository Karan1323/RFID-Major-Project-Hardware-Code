from machine import Pin, SPI
from xpt2046 import Touch
from ili9341 import Display, color565
from xglcd_font import XglcdFont
from touch_keyboard import TouchKeyboard
from time import sleep

from config import con_initial

spi1,spi2,display,unispace=con_initial


class Yes_or_no(object):
    """Checks if password is pwned."""

    def __init__(self,spi1,spi2, dc=4, cs1=16, rst=17, cs2=5, rotation=90):
        """Initialize PwnLookup."""
        # Set up display
        self.option=None
        self.exit=False
#         self.display = Display(spi1, dc=Pin(dc), cs=Pin(cs1), rst=Pin(rst),
#                                width=320, height=240, rotation=rotation)
# 
#         # Load font
#         self.unispace = XglcdFont('Unispace12x24.c', 12, 24)
        # Set up touchscreen
        print('inside init func of yes_or_no')
        self.xpt = Touch(spi2, cs=Pin(cs2), int_pin=Pin(27), int_handler=self.touchscreen_press)
        #display.clear()
        display.draw_text(5, 15, ' Do you want to register to', unispace, color565(255, 255, 255))
        display.draw_text(5, 45, ' the service? ', unispace, color565(255, 255, 255))


        display.draw_text(60, 120, ' Yes ', unispace, color565(255, 255, 255),background=color565(0, 122, 55))

        display.draw_text(160, 120, ' No  ', unispace, color565(255, 255, 255),background=color565(255, 0, 0))

        
       

    def touchscreen_press(self, x, y):
        """Process touchscreen press events."""
        x,y=y,x
        try:
            print('triggered')
            
            if (x>=70 and x<=130) and (y>=110 and y<=160) :
            
#                 display.clear()
#                 display.draw_text(60, 120, ' enter email ', unispace, color565(255, 255, 255),background=color565(0, 122, 55))
                self.option='y'
                self.exit=True
                
            
            elif (x>=150 and x<=210) and (y>=110 and y<=160) :
            
                #self.display.clear()
                self.option='n'
                print('No clicked')
                self.exit=True
                
                
            else:
                self.option='o'
                print('outside pixel clicked')
                self.exit=True
                
            
        except Exception as e:
            print('yes or no error occured',e)
            self.exit=True
            
# Yes_or_no(spi1,spi2)            
            
            
            
            
