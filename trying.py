from ili9341 import Display, color565
from xglcd_font import XglcdFont
import time
from machine import I2C, Pin, SPI, SoftSPI , SoftI2C
from mfrc522 import MFRC522
from config import con_initial,wifi_Conn,api_url
import urequests
import json
# from email_verify_disp import mail_verify
import email_verify_disp as e
spi1,spi2,display,unispace=con_initial


def spi_config():
    sck = Pin(22, Pin.OUT)
    mosi = Pin(33, Pin.OUT)
    miso = Pin(25, Pin.OUT)
    sda = Pin(15, Pin.OUT)
    rst = Pin(21, Pin.OUT)
    spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
    spi.init()
    return (spi,sda,rst)
    
new_uid="abc"
c=1


def convert_to_hex(num):
    res=""
    for i in range(len(num)-1):
        res+=hex(num[i]).replace("0x","")
    return res


    

if __name__=='__main__':
    s=time.time()
    
    
    wifi_Conn()
    
    spi,sda,rst=spi_config()
    

    
    while True:
        
        display.draw_text(5, 15, ' Scan Your Card... ', unispace, color565(255, 255, 255))
    
        display.draw_image('card1.raw', 110,69, 209, 150)

        display.draw_image('card2.raw', 110,69, 209, 150)

        display.draw_image('card3.raw', 110,69, 209, 150)

        display.draw_image('card4.raw', 110,69, 209, 150)
        
        rdr = MFRC522(spi, sda, rst)
        (stat, tag_type) = rdr.request(rdr.REQIDL)
        if stat == rdr.OK:
            (stat, raw_uid) = rdr.anticoll()
            if stat == rdr.OK:
                uid= convert_to_hex(raw_uid)
                if True:
                #if new_uid!=uid:
                    display.clear()
                    display.draw_text(5, 15, ' Verifying the Card.. ', unispace, color565(255, 255, 255))

                    new_uid=uid
                    print(uid)
                    print(raw_uid)
                    c=uid
                    resp=urequests.post(api_url,json={"uid":uid})
    
                    print(resp.status_code)
                    print(resp.text)
                    json_data=json.loads(resp.text)
                    print(json_data) #To be worked on Dictionary
                    if json_data["username"] in ['',None]:
                        print('no user exists')
                        display.clear()
                        display.draw_text(5, 15, '    Card not registered!  ', unispace, color565(255, 0, 0))
                        display.draw_image('exc.raw', 100,69, 115, 114)
                        time.sleep(5)
                        display.clear()
                        e.mail_verify(uid)
                        #break
                    else:
                        print(json_data["username"])
                        display.clear()
                        display.draw_text(5, 15, f'Welcome {json_data["username"]}', unispace, color565(255, 255, 255))
                        time.sleep(5)
                        display.clear()
                        
                        #break
                        
    
                    
                    

#     print('entering')
#     e.mail_verify()

    display.clear()  
    display.draw_text(5, 15, ' Scan Your Card... ', unispace, color565(255, 255, 255))
    print(f'Finished in {time.time()-s}')
