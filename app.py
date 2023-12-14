# # IMPORT LIB
# import _thread
# from machine import Pin
# from machine import Timer
# # IMPORT LIB
#
#
#
# class BoardLight:
#     def __init__(self,pin):
#         self.BL = Pin(pin, Pin.OUT)
#         self.FlashCounter = 0
#         self.LightStatue = 0
#     def BoardLight_ON(self):
#         self.BL.on()
#         self.LightStatue = 1
#     def BoardLight_OFF(self):
#         self.BL.off()
#         self.LightStatue = 0
#     def BoarfLight_Flash(self):
#         if self.FlashCounter == 0 and self.LightStatue == 1:
#             self.BL.off()
#             self.LightStatue = 0
#         elif self.FlashCounter == 0 and self.LightStatue == 0:
#             self.BL.on()
#             self.LightStatue = 1
#     def SetFlashFreq(self,val):
#         self.FlashCounter = val
#
#
# # GLOBAL VARIETY
# BL = BoardLight(2)
#
#
#
# # GLOBAL VARIETY
#
# def MAIN():
# # BOARDa LIGHT
#     BL = BoardLight(2)
#     BL.BoardLight_OFF() #初始关灯
#     BL.SetFlashFreq(500)
# # BOARDa LIGHT
# # SYS_TIMER
#     TIMER = Timer(1)
#     TIMER.init(period=1, mode=Timer.PERIODIC, callback=Counter)
# # SYS_TIMER
# while True:
#     BL.BoardLight_ON()
# def Counter():
#     BL.FlashCounter = BL.FlashCounter+1
#
# MAIN()
import time

while 1:
    time.sleep(1)
    print(2)