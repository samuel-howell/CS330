from Robot import Robot
import time

robot = Robot('COM10')

# robot.reset() 
# robot.start()
# robot.safe()
# robot.drive(0,50,0,0)
# time.sleep(2)
# robot.drive(0,0,0,0)
# time.sleep(1)
# robot.leds(15,55,255)
# time.sleep(4)
# robot.leds(0,0,0)
# time.sleep(1)
# robot.digitLEDsASCII(49,50,51,52)
# time.sleep(1)
# robot.driveDirect(0,60,0,60)
# time.sleep(3)
# robot.digitLEDsASCII(32,32,32,32)
# robot.drive(0,0,0,0)
# robot.clearBuffer()
# robot.closeConnection()


robot.reset() 
time.sleep(3)

robot.start()
time.sleep(3)

robot.safe()
print("ready to run")
robot.driveDirect(1,3,1,0)
time.sleep(4.8)
robot.drive(0,0,0,0)
robot.driveDirect(10,0,246,0)
time.sleep(.45)
robot.drive(0,0,0,0)

robot.driveDirect(1,3,1,0)
time.sleep(4.8)
robot.drive(0,0,0,0)
robot.driveDirect(10,0,246,0)
time.sleep(.45)
robot.drive(0,0,0,0)

robot.driveDirect(1,3,1,0)
time.sleep(4.9)
robot.drive(0,0,0,0)
robot.driveDirect(10,0,246,0)
time.sleep(.43)
robot.drive(0,0,0,0)

robot.driveDirect(1,3,1,0)
time.sleep(4.8)
robot.drive(0,0,0,0)
robot.driveDirect(10,0,246,0)
time.sleep(.43)
robot.drive(0,0,0,0)

robot.clearBuffer()
robot.closeConnection()