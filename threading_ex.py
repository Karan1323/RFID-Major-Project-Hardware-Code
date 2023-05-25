import _thread
import time
from ili9341 import Display, color565
from machine import  Pin, SPI, SoftSPI
import time
from xglcd_font import XglcdFont
import urequests

unispace = XglcdFont('Unispace12x24.c', 12, 24)
spi1 = SPI(1, baudrate=51200000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
spi2 = SPI(2, baudrate=1000000,sck=Pin(18), mosi=Pin(23), miso=Pin(19))
display = Display(spi1, dc=Pin(4), cs=Pin(16), rst=Pin(17),width=320, height=240, rotation=90)
resp=None

def requesting_uid_from_db():
    resp=urequests.post("https://us-east-1.aws.data.mongodb-api.com/app/application-0-qrwzu/endpoint/rfid_test?secret=rfid",json={"uid":"90909"})
    return resp
    
    
    
    
    
display.clear()
display.draw_text(5, 15, ' Verifying the Card.. ', unispace, color565(255, 255, 255))
_thread.start_new_thread(requesting_uid_from_db,())


for i in range(2):
    display.draw_image('v1.raw', 100,69, 90, 42)
    time.sleep(0.2)
    display.draw_image('v2.raw', 100,69, 90, 42)
    time.sleep(0.2)
    display.draw_image('v3.raw', 100,69, 90, 42)
    if i==2:
        exit()
    time.sleep(0.2)
#resp=urequests.post("https://us-east-1.aws.data.mongodb-api.com/app/application-0-qrwzu/endpoint/rfid_test?secret=rfid",json={"uid":uid})
time.sleep(10)
print(resp.status_code)
print(resp.text)
    
    
# _thread.start_new_thread(pre,())
# _thread.start_new_thread(dele,())    