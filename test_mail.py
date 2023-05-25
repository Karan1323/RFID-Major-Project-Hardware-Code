"""Search online for pwned passwords."""
from machine import Pin, SPI
from xpt2046 import Touch
from ili9341 import Display, color565
from xglcd_font import XglcdFont
from touch_keyboard import TouchKeyboard
from time import sleep
from Sending_Mail import send_mail
import network
import time
from config import con_initial,wifi_Conn

spi1,spi2,display,unispace=con_initial



class PwnLookup(object):
    """Checks if password is pwned."""

    def __init__(self, uid, dc=4, cs1=16, rst=17, cs2=5, rotation=90):
        """Initialize PwnLookup."""
        # Set up display
    
#         self.display = Display(spi1, dc=Pin(dc), cs=Pin(cs1), rst=Pin(rst),
#                                width=320, height=240, rotation=rotation)
# 
#         # Load font
#         self.unispace = XglcdFont('Unispace12x24.c', 12, 24)

        # Set up Keyboard
        self.uid=uid
        self.keyboard = TouchKeyboard(display, unispace)

        # Set up touchscreen
        self.xpt_2 = Touch(spi2, cs=Pin(cs2), int_pin=Pin(27), int_handler=self.touchscreen_press_2)
        
        self.exit=False 
       
    def key_handle(self,x,y):
        if self.keyboard.handle_keypress(x, y, debug=False) is True:
                
            pwd = self.keyboard.kb_text
            display.clear()
            display.draw_text(5, 15, ' Verifying The E-Mail ID.. ', unispace, color565(255, 255, 255))

            
            
            mssg=f'http://localhost:3000/register?uid={self.uid}'
            pwd=str(pwd)
            status=send_mail(pwd, mssg)
            if status:
                print('mail sent')
                display.clear()
                display.draw_text(5, 15, ' Sending Registration link ', unispace, color565(255, 255, 255))
                display.draw_text(5, 45, ' to : ', unispace, color565(255, 255, 255))
                display.draw_text(5,75 , f' {pwd}', unispace, color565(255, 172, 28))
                for i in range(2):
                    display.draw_image('v1.raw', 100,120, 90, 42)
                    time.sleep(0.2)
                    display.draw_image('v2.raw', 100,120, 90, 42)
                    time.sleep(0.2)
                    display.draw_image('v3.raw', 100,120, 90, 42)
                    if i==2:
                        exit()
                    time.sleep(0.2)
                
                display.clear()
                display.draw_text(5, 15, ' Link successfully sent to ', unispace, color565(5, 225, 66))
                display.draw_text(5, 45, ' your E-mail ID! ', unispace, color565(5, 225, 66))
                display.draw_image('mail.raw', 110,89, 100, 99)
                time.sleep(5)
                display.clear()

                self.keyboard.waiting = True
                self.keyboard.locked = False
                self.exit=True

            else:
                display.clear()
                display.draw_text(5, 15, '   Invalid E-mail ID! ', unispace, color565(255, 0, 0))
                display.draw_image('exc.raw', 100,69, 115, 114)
                self.keyboard.waiting = True
                self.keyboard.locked = False
                self.exit=True
                time.sleep(2.5)
                display.clear()
                display.draw_text(5, 15, '  Registration Incomplete! ', unispace, color565(255, 0, 0))
                time.sleep(2.5)
                display.clear()
                
                
                

                
    def touchscreen_press_2(self, x, y):
        """Process touchscreen press events."""
        try:
            self.key_handle(x,y)
            
            
        except Exception as exc:
            print('pixel mapping error',exc)
#             if 'tuple index out of range'in exc:
#                 self.key_handle(x,y)
#             self.exit=True

# wifi_Conn()
# PwnLookup()

  
    

