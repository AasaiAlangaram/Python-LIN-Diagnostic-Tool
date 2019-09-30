import PyLinDriver
import time

MasterID = 0x3C
SlaveID = 0x7D

#Read output electric current 1 request frame
SendFrame =[0x01,0x03,0x22,0x02,0x47,0xff,0xff,0xff]

counter =0

while(1):
    x=[]
    time.sleep(0.02)
    PyLinDriver.SendMasterFrame(MasterID,SendFrame)
    time.sleep(0.02)
    x = PyLinDriver.SendHeaderFrame(SlaveID)
    print(x)

#check sum calculation
#The checksums are computed according to the following formula:

#Checksum = INV (data byte 1 ⊕ data byte 2 ⊕ ... ⊕ data byte 8)    
