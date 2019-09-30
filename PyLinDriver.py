#import serial
#import time
#import RPi.GPIO as GPIO
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(24,GPIO.OUT)
ser = serial.Serial("/dev/ttyS0",
                    baudrate=19231,
                    timeout=0.1,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS)

SyncBreak = 0x55

def SendHeader(ID):
    GPIO.output(24,0)
    time.sleep(0.000677)
    GPIO.output(24,1)
    time.sleep(0.000322)
    # serial expects a bytearray and not a string in python3.
    ser.write(chr(SyncBreak).encode()) #This is convert string into a byte array for serial transfer
    ser.write(chr(ID).encode())

def SendData(msg):
    print(msg)
    tmpBuffer= bytearray()
    for i in range(len(msg)):
        tmpBuffer.append(msg[i])

    Cks = CalcChecksum(tmpBuffer)
    tmpBuffer.append(Cks)
    ser.write(tmpBuffer)

def CalcChecksum(msg):
    data =0
    for i in range(len(msg)):
        data = data+msg[i]
        if data >255 :
            data = data -255

    data = ~data
    return ( data & 0xFF)


def SendMasterFrame(ID,msg):
    SendHeader(ID)   #Master ID
    SendData(msg)    #Request Frame

def SendHeaderFrame(ID):
    x=[]
    x1=[]
    ser.flushOutput()
    ser.flushInput()

    SendHeader(ID)
    time.sleep(0.010)
    a = ser.read(13)
    x = a.hex()

    print(x)
    ser.flushOutput()
    ser.flushInput()

    '''
    if x[0:2] =="55":
        x1 = x[4:22]

    elif x[0:2] =="7d":
        x1 = x[2:20]
    else:
        x1 = x[0:18]
    '''
    if x[6:8] =="7d":
        x1 = x[8:]

    return x1

def SendHeaderFrame_HexResp(ID):
    x=[]
    x1=[]
    ser.flushOutput()
    ser.flushInput()

    SendHeader(ID)
    time.sleep(0.010)
    a = ser.read(20)
    x = a.hex()

    print(x)
    ser.flushOutput()
    ser.flushInput()

    '''
    if x[0:2] =="55":
        x1 = x[4:22]

    elif x[0:2] =="7d":
        x1 = x[2:20]
    else:
        x1 = x[0:18]
    '''
    if x[6:8] =="7d":
        x1 = x[8:]
    else:
        return None

    print(x1)

    if x1=="":
        return None
    digit = []

    #print("Function is Called")

    for i in range(int(len(x1) / 2)):
        HighDigit = int(x1[(i * 2)], 16) * 16
        LowDigit = int(x1[(i * 2) + 1], 16)

        digit.append(HighDigit + LowDigit)

    #print(digit)

    return digit



