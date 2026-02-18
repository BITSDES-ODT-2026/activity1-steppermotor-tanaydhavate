from machine import Pin
import time

p1 = Pin(23, Pin.OUT)
p2 = Pin(22, Pin.OUT)
p3 = Pin(19, Pin.OUT)
p4 = Pin(18, Pin.OUT)
x=[[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]]

for i in range (0,1000,1):
    for i in x:
        p1.value(i[0])
        p2.value(i[1])
        p3.value(i[2])
        p4.value(i[3])
        time.sleep(0.003)
        
        
        p1.value(0)
        p2.value(0)
        p3.value(0)
        p4.value(0)

