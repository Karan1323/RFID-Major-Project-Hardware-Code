from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from test_mail import PwnLookup
import time
from yes_no import Yes_or_no
from config import con_initial,wifi_Conn

spi1,spi2,display,unispace=con_initial


def to_exit_Touch(p):
    while not p.exit:
        continue
    print('deleting touch object  ')
    del p
    print('Done')
    
def to_exit_Touch_yn(p):
    while not p.exit:
        continue
    print('touch option selected in y or no ')
        

def mail_verify(uid):
    
    while True:
        yn=Yes_or_no(spi1,spi2)
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
            time.sleep(2)
            display.clear()
            p=PwnLookup(uid)
            to_exit_Touch(p)
            break
            
        elif yn.option=='n':
            del yn
            display.clear()
            display.draw_text(5, 15, '  REGISTRATION CANCELLED!', unispace, color565(255, 0, 0))
            display.draw_image('canc.raw', 90,65, 130, 130)
            time.sleep(2)
            display.clear()
            break
            
          
        else:
            del yn
            display.draw_text(50, 200, 'Choose correct option! ', unispace, color565(255, 0, 0))
            display.draw_image('warn.raw', 5,190, 40, 40)

            #time.sleep(5)
#             continue
    
# wifi_Conn()
# mail_verify()






