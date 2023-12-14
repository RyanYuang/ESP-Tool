import serial
import serial.tools.list_ports
from Libs import varity


class Serial:
    def __init__(self):
        # self.Device = serial.Serial("COM21",115200)
        self.portList = list(serial.tools.list_ports.comports())
        self.NumOfPort = len(self.portList)
        self.LastNumOfPort = 0
        self.comports = []
        if len(self.portList)<=0:
            print("There is have no Serial Device")
        else:
            print("Detectd Serial Device")
            for comport in self.portList:
                print(list(comport)[0], list(comport)[1])
    def UpDatePortList(self):
        while True:
            self.portList = list(serial.tools.list_ports.comports())
            SerialPortList = []
            self.comports = []
            self.LastNumOfPort = self.NumOfPort
            for comport in self.portList:
                SerialPortList.append((comport)[0]+list(comport)[1])
                self.comports.append(list(comport)[0])
            varity.q.put(SerialPortList)