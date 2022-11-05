#!/bin/bash
sudo python3 /home/krishna/TinyFPGA-Programmer-Application/tinyfpga-programmer-gui.py --port /dev/ttyACM1  --appfpga top.bin --m4app $1 --mode m4-fpga --reset
