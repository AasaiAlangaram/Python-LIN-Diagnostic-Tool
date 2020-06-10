[![GitHub license](https://img.shields.io/github/license/dipakkr/A-to-Z-Resources-for-Students.svg?style=plastic)](https://github.com/AasaiAlangaram/Python-LIN-Diagnostic-Tool/blob/master/LICENSE)
# LIN-Driver-Implemented-using-Python
LIN Communication using R-Pi Serial 

## Thanks Note

I'm thankful to my mentor for guiding me through out this project.

## Project Overview

The Purpose of this project is to read diagnostic data & other information from ECU through [LIN](https://en.wikipedia.org/wiki/Local_Interconnect_Network) communication.
Our ECU supports LIN Communication.One can use this project to build their own LIN Analyzer.For GUI Implementation PyQt Framework is used.

## SourceCode Overview

[1.PyLINTask.py](https://github.com/AasaiAlangaram/Python-LIN-Diagnostic-Tool/blob/master/PyLINTask.py)\
[2.PyLinDriver](https://github.com/AasaiAlangaram/Python-LIN-Diagnostic-Tool/blob/master/PyLinDriver.py)

## Requirements
-[LIN Transceiver](https://www.nxp.com/docs/en/data-sheet/TJA1020.pdf)\
-[74LS08](http://www.sycelectronica.com.ar/semiconductores/74LS08.pdf)\
-[Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)\
-1K Resistor\
-Jumpers & Wires

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

This is how the following project was implemented.If you have any doubt in implementing this :mailbox: :arrow_down: @aasaialangaram450@gmail.com


##  For Bug Reports & Help :beetle:

Use the GitHub issue.


