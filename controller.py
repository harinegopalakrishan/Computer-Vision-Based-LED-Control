#Import pyfirmata
import pyfirmata

#Choose the port your arduino is connected to
comport='COM9'

#Choose board
board=pyfirmata.Arduino(comport)

#Locate pins connected to the microcontroller
led_1=board.get_pin('d:8:o') #Digital pin 8 connected to led 1
led_2=board.get_pin('d:9:o') #Digital pin 9 connected to led 2
led_3=board.get_pin('d:10:o') #Digital pin 10 connected to led 3
led_4=board.get_pin('d:11:o') #Digital pin 11 connected to led 4
led_5=board.get_pin('d:7:o') #Digital pin 7 connected to led 5

def led(fingerUp):
    #If no finger is up then no LED will glow
    if fingerUp==[0,0,0,0,0]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)

    #If index finger is up LED 1 will glow
    elif fingerUp==[0,1,0,0,0]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)

    #If index finger and middle finger are up LED 1 and 2 will glow
    elif fingerUp==[0,1,1,0,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)   

    #If index, middle and ring finger are up then LED 1,2 and 3 will glow
    elif fingerUp==[0,1,1,1,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)

    #If index, middle, ring and little finger are up then LED 1,2,3 and 4 will glow
    elif fingerUp==[0,1,1,1,1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)

    #If all the five fingers are up, then all the LED will glow
    elif fingerUp==[1,1,1,1,1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
