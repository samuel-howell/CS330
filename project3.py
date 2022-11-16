from Robot import Robot
import time

robot = Robot('COM10')

# when serial not found, change interprester to microsoft store version of python

robot.reset() 
time.sleep(2)

robot.start()
time.sleep(2)

robot.safe()
print("ready to run")

robot.createSongOne()
robot.createSongTwo()


robot.playSongOne()
time.sleep(15) # wait 15 seconds before sending the second song play so the buffer isn't overwritten and the song doens't play
robot.playSongTwo()

print("operation finished")
robot.clearBuffer()
robot.closeConnection()