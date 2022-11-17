'''
Samuel Howell 
CS330
Project 5


Note: you need to install pkgs from the cmd line outside of the vs code application
'''

from Robot import Robot
import time



byteList = []
flag = False
robot = Robot('COM3')
direction = "n"

#! MAKE SURE THE CORD IS PLUGGED ALL THE WAY IN
def initRobot():
    robot.reset() 
    time.sleep(1)
    robot.start()
    time.sleep(1)
    robot.safe()
    time.sleep(1)
    print("ready to run")
    robot.clearBuffer()

 

initRobot()

# move forward until bump
while(flag == False):
    robot.driveDirect(0,150,0,150)

    robot.sendCommand(b'\x8E\x07') # bump detected
    readList = robot.read(1)
    

    bumpDetected =(int(readList[0], 2) & 1 == 1 or int(readList[0], 2) & 2 == 2)   #  use bitmasking to isolate and check each status bit to determine if left or right bump have been triggered
    
    if(bumpDetected):
        flag = True
        print("bump detected")
        robot.driveDirect(254,150,254,150) # drive backward to create some space for the turn
        time.sleep(.2)
        robot.driveDirect(0, 150, 255, 106)  #rotate 90 degrees in a west direction to get the wall to the right of the wall sensor. #! make sure robot is rotating enought to get a good inital read from the side
        time.sleep(1.5) 
        robot.driveDirect(0,0,0,0)
    


while(flag == True):
    #robot.driveDirect(0,50,0,50)
    #robot.sendCommand(b'\x8E\x07') # bump detected
    
    robot.queryLight()
    byteList.append(robot.readTwo())  #! make sure that you come in from the side more so than you think
    


    currentByte = int(str(byteList[len(byteList)-1]).lstrip('[').rstrip(']')) # this takes "[x]" and makes is "x" so it can be converted to an int.
    print("current: " + str(currentByte))
    
    error = 150 - currentByte # desired distance - actual distance
    ref = 40
    prop = robot.pController(error)

    print("prop: ", str(prop), "   error: " + str(error), "   distance: ", str(currentByte))
    

    # wait for serial comm to stop sending before you run program again
    # current byte is measurement from the wall. we want to keep it at around 40

    if (currentByte > 150):
        currentByte = 150
    if (currentByte == 0): # ifthe robot is too far away from the wall, set current byte to ref - 1 to send the robot right.
        currentByte == ref - 1
    if (currentByte < ref): # move closer to the wall, turning right #!can change 10 to 0 for even tighter turns if necessary depending on complexity of the obstacle
        robot.driveDirect(0, 50 - prop, 0, 50 + prop)
        print("R")
    if (currentByte > ref): # move away from the wall, turning left
        robot.driveDirect(0, 50 + prop, 0, 50 - prop)
        print("L")
    if (currentByte == ref): # go straight
        robot.driveDirect(0, 70, 0, 70)

    
    #check for a bump
    robot.sendCommand(b'\x8E\x07') # bump detected
    readList = robot.read(1)
    bumpDetected =(int(readList[0], 2) & 1 == 1 or int(readList[0], 2) & 2 == 2)
    
    if(bumpDetected):
        robot.driveDirect(0, 150, 255, 106)  #rotate 90 degrees in a west direction to get the wall to the right of the wall sensor. #! make sure robot is rotating enought to get a good inital read from the side
        time.sleep(.3)
        robot.driveDirect(0, 0, 0, 0)
        
        
    if(len(byteList) > 5): # don't let the list grow  large
        byteList.pop(0)




'''
*65% of the grade:*
USE P-CONTROLLER ONLY: Write a program that commands the iRobot Create to respond in the following ways:
1. Start the robot driving. It should drive until it contacts a wall – you may ensure there is nothing else in its path. At the wall, it should rotate and align itself parallel to the surface.
2. Once the robot is parallel to the surface of the wall, it should begin translating again keeping a set distance from the surface (you decide distance).
3. While following the wall, it should pay attention to its bump sensors and using those along with its wall range sensor and should attempt to circumnavigate anything–imagine a shoe–it finds in its way.
4. Points will be awarded for how well the robot stabilizes following the wall, how well it corners and how well it circumnavigates obstacles along the wall.

*10% of the grade:*
5. Upload a video of your robot driving along the wall with the same obstacles to YouTube. The video should be named the following way:FMU CS330 Robotics Fall 2022, Lab Project #5, [first, last names of all the students in the team]: Kp=[your Kp].

*15% of your grade:*
6. Create a report where you explain how you choose a period of quering sensor data, reference, Kp, Ki, Kd, transition function, draw a control system you use in your project.

*10% of your grade:*
7. Slack usage:
7.1 Learn how to share files on Slack using Googe Drive. Share a file with your partner (team).
7.2 Learn how to incorporate the Trello app in a slack. Learn how to add a card, make a comment, assign a teammate to a card.
7.3 Send a private video message to your partner  with some meaningful content.using /voice command.
7.4 Set up a zoom conference via slack (using /zoom).
7.5 Also, using the https://lunchtrain.builtbyslack.com/ schedule a lunch with your partner (yourself), and make him join you, show me the reminders from the slack bot
'''
