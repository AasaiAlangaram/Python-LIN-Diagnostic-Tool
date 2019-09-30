# LIN-Driver-Implemented-using-Python
LIN Communication using R-Pi Serial 

## Project Overview

The Purpose of this project is to read diagnostic data & other information from ECU through [LIN](https://en.wikipedia.org/wiki/Local_Interconnect_Network) communication.
Our ECU supports LIN Communication.

## Requirements
-[LIN Transceiver](https://www.nxp.com/docs/en/data-sheet/TJA1020.pdf)\
-[74LS08](http://www.sycelectronica.com.ar/semiconductores/74LS08.pdf)\
-[Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)\
-1K Resistor\
-Jumpers

## Serial Communication in PI

This project used PI UART Protocol.To know more about serial communication in raspberry pi check this.\
[Serial Documentation](https://www.raspberrypi.org/documentation/configuration/uart.md)

## LIN Transceiver Pin Map Quick Reference

| Pin | Description |
| ----------- | ----------- |
| 1 | RxD |
| 2 | SLP_N |
| 3 | Wake_N |
| 4 | TxD |
| 5 | GND |
| 6 | LIN |
| 7 | Vbat |
| 8 | INH |

## Schematic

![Schematic](https://user-images.githubusercontent.com/43054456/65871741-004d5100-e3ba-11e9-9830-ea4d8eb5a286.JPG)

