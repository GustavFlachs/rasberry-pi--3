from machine import Pin
import dht
import time

d = dht.DHT11(Pin(0))
led1 = Pin(1, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(3, Pin.OUT)
led4 = Pin(4, Pin.OUT)




while True:
    try: 
        d.measure()
        temp = d.temperature()
        hum = d.humidity()
        print("teplota: %3.1f C" %temp)
        print("humidity: %3.1f %%" %hum)
        print("------------------------")
    except:
        print("fail")
    time.sleep(3)
    if temp >21.9:
        led1(True)
        led2(False)
        led3(False)
        led4(False)
    if temp >22.9:
        led1(True)
        led2(True)
        led3(False)
        led4(False)
    if temp >23.9:
        led1(True)
        led2(True)
        led3(True)
        led4(False)
    if temp >24.9:
        led1(True)
        led2(True)
        led3(True)
        led4(True)
