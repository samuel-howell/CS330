from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from Robot import Robot
import keyboard
import time
import sys

dir = "n"
robot = Robot('COM9')

#! MAKE SURE THE CORD IS PLUGGED ALL THE WAY IN
def initRobot():
    robot.reset() 
    time.sleep(2)
    robot.start()
    time.sleep(2)
    robot.safe()
    time.sleep(2)
    print("ready to run")

def changeDir(a):
    dir = a
    if (dir == "n"):
        ttk.Label(frm, image = robotN).grid(column=2, row=2)
        robot.driveDirect(0, 250, 0, 250)
    elif (dir == "ne"):
        ttk.Label(frm, image = robotNE).grid(column=2, row=2)
        robot.driveDirect(0, 150, 0, 250) 
    elif (dir == "nw"):
        ttk.Label(frm, image = robotNW).grid(column=2, row=2)
        robot.driveDirect(0, 250, 0, 150)
    elif (dir == "s"):
        ttk.Label(frm, image = robotS).grid(column=2, row=2)
        robot.driveDirect(255, 106, 255, 106)
    elif (dir == "se"):
        ttk.Label(frm, image = robotSE).grid(column=2, row=2)
        robot.driveDirect(255, 106, 255, 6)
    elif (dir == "sw"):
        ttk.Label(frm, image = robotSW).grid(column=2, row=2)
        robot.driveDirect(255, 6, 255, 106)
    elif (dir == "w"):
        ttk.Label(frm, image = robotW).grid(column=2, row=2)
        robot.driveDirect(0, 150, 255, 106)
    elif (dir == "e"):
        ttk.Label(frm, image = robotE).grid(column=2, row=2)
        robot.driveDirect(255, 106, 0, 150)
    else:
        ttk.Label(frm, image = robotNE).grid(column=2, row=2)
        robot.driveDirect(0,0,0,0) 
   
def moveN():
    if keyboard.is_pressed("w"): #N
        print("n")
        robot.driveDirect(0, 250, 0, 250)
        ttk.Label(frm, image = robotN).grid(column=2, row=2)
        if keyboard.is_pressed("a"): #NW
            print("nw")
            ttk.Label(frm, image = robotNW).grid(column=2, row=2)
            robot.driveDirect(0, 250, 0, 150)
        if keyboard.is_pressed("d"): #NE
            print("ne")
            ttk.Label(frm, image = robotNE).grid(column=2, row=2)
            robot.driveDirect(0, 150, 0, 250) 
    else:
        if(keyboard.is_pressed("f")):
            robot.driveDirect(0,0,0,0)

def moveW():
    if keyboard.is_pressed("a"): #W
        ttk.Label(frm, image = robotW).grid(column=2, row=2)
        robot.driveDirect(0, 150, 255, 106)
        if keyboard.is_pressed("w"): #NW
            ttk.Label(frm, image = robotNW).grid(column=2, row=2)
            robot.driveDirect(0, 250, 0, 150)
        if keyboard.is_pressed("s"): #SW
            ttk.Label(frm, image = robotSW).grid(column=2, row=2)
            robot.driveDirect(255,6,255,106)
    else:
        if(keyboard.is_pressed("f")):
            robot.driveDirect(0,0,0,0)

def moveS():
    if keyboard.is_pressed("s"): #S
        ttk.Label(frm, image = robotS).grid(column=2, row=2)
        print("keyboard s is pressed")
        robot.driveDirect(255, 106, 255, 106)
        if keyboard.is_pressed("a"): #SW  
            ttk.Label(frm, image = robotSW).grid(column=2, row=2)              
            robot.driveDirect(255, 6, 255, 106)
        if keyboard.is_pressed("d"): #SE    
            ttk.Label(frm, image = robotSE).grid(column=2, row=2)            
            robot.driveDirect(255, 106, 255, 6)
    else:
        if(keyboard.is_pressed("f")):
            robot.driveDirect(0,0,0,0)

def moveE():
        if keyboard.is_pressed("d"): #E   
            ttk.Label(frm, image = robotE).grid(column=2, row=2)        
            robot.driveDirect(255, 106, 0, 150)
            if keyboard.is_pressed("w"): #NE  
                ttk.Label(frm, image = robotNE).grid(column=2, row=2)             
                robot.driveDirect(0, 150, 0, 250)
            if keyboard.is_pressed("s"): #SE  
                ttk.Label(frm, image = robotSE).grid(column=2, row=2)             
                robot.driveDirect(255, 106, 255, 6)
        if(keyboard.is_pressed("f")):
            robot.driveDirect(0,0,0,0)

def endProgram():
    root.destroy()
    robot.driveDirect(0,0,0,0)
    robot.closeConnection()
    print("hit end program")

def playSong(): 
    robot.createSongOne()
    robot.createSongTwo()

    robot.playSongOne()
    time.sleep(15) # wait 15 seconds before sending the second song play so the buffer isn't overwritten and the song doens't play
    robot.playSongTwo()

    print("operation finished")
    robot.clearBuffer()

def stopRobot():
    robot.driveDirect(0,0,0,0)

def submit():
 
    
    value = num_entry.get()
   
   
    values = list(value) # split the 4digits up into an array using "" as delim

    try:
        digit3 = ord(values[0]) #ord gives us ascii representation
        digit2 = ord(values[1])
        digit1 = ord(values[2])
        digit0 = ord(values[3])

        robot.digitLEDsASCII(digit3, digit2, digit1, digit0)

    except Exception:
        print("Invalid input. please enter 4 digits.")
     

def changeLED(color):
    if(color == "red"):
        robot.leds(2,255,255)
    elif(color == "orange"):
        robot.leds(2,32,255)
    elif(color == "green"):
        robot.leds(2,0,255)
    elif(color == "yellow"):
        robot.leds(2,8,255)
    else:
        print("color not recognized") # should never hit this

def validate(P): # validate so only 4 chars can be entered in the entry box. 
    
    if len(P) <= 4:
        # Entry with 4 digit is ok
        return True
    else:
        # Anything else, reject it
        return False



initRobot()
root = Tk()
root.geometry("800x800")
root.resizable(False,False)
# root.bind('<Key>', key_press)
root.bind('w', lambda w: moveN())
root.bind('a', lambda a: moveW())
root.bind('s', lambda s: moveS())
root.bind('d', lambda d: moveE())
root.bind('f', lambda f: stopRobot())
vcmd = (root.register(validate), '%P') 

#region   IMAGE FORMATTING
# Load the image
aW=Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\arrows\\arrowW.png')
aE=Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\arrows\\arrowE.png')
aN=Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\arrows\\arrowN.png')
aS=Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\arrows\\arrowS.png')
aNW=Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\arrows\\arrowNW.png')
aNE=Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\arrows\\arrowNE.png')
aSW=Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\arrows\\arrowSW.png')
aSE=Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\arrows\\arrowSE.png')

rE = Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\robot\\mE.png') 
rW = Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\robot\\mW.png') 
rN = Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\robot\\mN.png') 
rS = Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\robot\\mS.png') 
rNW = Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\robot\\mNW.png') 
rSW = Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\robot\\mSW.png') 
rNE = Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\robot\\mNE.png') 
rSE = Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\robot\\mSE.png') 

playbtn = Image.open('C:\\Users\slide\\.vscode\\vsCode_Projects\\Python\\CS-330\\images\\robot\\playbtn.png') 

aW=aW.resize((50, 50))
aE=aE.resize((50, 50))
aN=aN.resize((50, 50))
aS=aS.resize((50, 50))
aNE=aNE.resize((50, 50))
aNW=aNW.resize((50, 50))
aSW=aSW.resize((50, 50))
aSE=aSE.resize((50, 50))

rW=rW.resize((150, 150))
rE=rE.resize((150, 150))
rN=rN.resize((150, 150))
rS=rS.resize((150, 150))
rNE=rNE.resize((150, 150))
rNW=rNW.resize((150, 150))
rSW=rSW.resize((150, 150))
rSE=rSE.resize((150, 150))

playbtn = playbtn.resize((50,50))


arrowN=ImageTk.PhotoImage(aN)
arrowE=ImageTk.PhotoImage(aE)
arrowS=ImageTk.PhotoImage(aS)
arrowW=ImageTk.PhotoImage(aW)
arrowNE=ImageTk.PhotoImage(aNE)
arrowNW=ImageTk.PhotoImage(aNW)
arrowSE=ImageTk.PhotoImage(aSE)
arrowSW=ImageTk.PhotoImage(aSW)

robotN=ImageTk.PhotoImage(rN)
robotE=ImageTk.PhotoImage(rE)
robotS=ImageTk.PhotoImage(rS)
robotW=ImageTk.PhotoImage(rW)
robotNE=ImageTk.PhotoImage(rNE)
robotNW=ImageTk.PhotoImage(rNW)
robotSE=ImageTk.PhotoImage(rSE)
robotSW=ImageTk.PhotoImage(rSW)

playbtn = ImageTk.PhotoImage(playbtn)

#endregion


frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Exit", command= lambda: endProgram()).grid(column=6, row=2)

ttk.Button(frm, image = arrowW, command =lambda: changeDir("w")).grid(column=1, row=2)
ttk.Button(frm, image = arrowNW, command =lambda: changeDir("nw")).grid(column=1, row=1)
ttk.Button(frm, image = arrowNE, command =lambda: changeDir("ne")).grid(column=3, row=1)
ttk.Button(frm, image = arrowE, command =lambda: changeDir("e")).grid(column=3, row=2)
ttk.Button(frm, image = arrowN, command =lambda: changeDir("n")).grid(column=2, row=1)
ttk.Button(frm, image = arrowS, command =lambda: changeDir("s")).grid(column=2, row=3)
ttk.Button(frm, image = arrowSW,command =lambda: changeDir("sw")).grid(column=1, row=3)
ttk.Button(frm, image = arrowSE, command =lambda: changeDir("se")).grid(column=3, row=3)

ttk.Label(frm, image = robotN).grid(column=2, row=2) #the main pic of the robot

ttk.Button(frm, image = playbtn, command = lambda: playSong()).grid(column=5, row=2)



ttk.Label(frm, text ="Enter 4 digits to display on robot").grid(column=5, row =1) #! idk if this should be form or root
num_entry=tk.Entry(frm, textvar=input, validate="key", validatecommand=vcmd)
num_entry.grid(column=6, row=1)
ttk.Button(frm, text="Submit", command = lambda: submit()).grid(column=7, row=1)


tk.Button(frm, padx =10, bg = 'red', command = lambda: changeLED("red")).grid(column=4, row=6)
tk.Button(frm, padx =10, bg = 'orange', command = lambda: changeLED("orange")).grid(column=6, row=6)
tk.Button(frm, padx =10, bg = 'green', command = lambda: changeLED("green")).grid(column=5, row=6)
tk.Button(frm, padx =10, bg = 'yellow', command = lambda: changeLED("yellow")).grid(column=7, row=6)




root.mainloop()
    



"""
In this project we will learn create GUI which would control the robot's movements.

75% of your grade:
1. Create a GUI to control your robot with at least four buttons.
2. The GUI should have an image at the center which would be changing depending on the motion direction of the robot (here is a screenshot). This image should be in at least 8 possible positions (pointing north, south, west, east, north-west, north-east, south-west, south-east, etc.).
3. The direction should be changing depending on the button pressed as well as keys pressed on the keyboard - w, s, a, d or arrows.
4. The GUI needs to have a "play a tune" button: your tune from the previous lab should be played when one presses it
5. The GUI needs to have a four-symbol input field. If you type any four-digit number, that number should be displayed on the Digit LEDs.
6. The GUI needs to have a four buttons without any text but with colors (red, orange, green, yellow). When any of the buttons is pressed, the Clean/Power LED should have corresponding color.
7. You can optionally add a booster speed button, stop button or any other buttons you would like to have.
Any of the buttons should be able to work at the same time, e.g. if the robot is driving and a user presses "play a tune button", the tune should be played without any interruption of the robot's motion.

15% of your grade: write a short well-formatted one page report (PDF), submit to the BB by 11.59PM deadline. The report should describe  the assignment, what you have done, where you had any issues, conclusion (i.e. what you learned in this project)

10% of your grade (Slack exercises, both you and your partner should complete this exercise, you both should also be able to redo this if I ask you to):
1. "Monkey Test" any website;
2. Create/join a Google Hangouts conference with your partner
3. Set a reminder to yourself to submit a project report by 11.00PM of the duedate.
4. Create a Google Calendar event to meet with your partner
5. Create a Skype conference with your partner from Slack
"""