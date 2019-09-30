import PyLinDriver
import time

MasterID = 0x00 #ECU Master ID
SlaveID = 0x00 #Slave ID

#Send Frame with Request msg
SendFrame =[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]

counter =0

while(1):
    x=[]
    time.sleep(0.02)
    PyLinDriver.SendMasterFrame(MasterID,SendFrame)
    time.sleep(0.02)
    x = PyLinDriver.SendHeaderFrame(SlaveID)
    print(x)


