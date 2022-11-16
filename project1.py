import serial
import time
import struct

connection = serial.Serial("COM10", baudrate=115200, timeout=1)

#  Samuel Howell / 9-13-22 / CS330 / Project 1

connection.write(b'\x80\x07') # start and reset
time.sleep(4)
connection.write(b'\x80') # start it again
time.sleep(2)
connection.write(b'\x83') # put it in safe mode
time.sleep(2)
connection.write(b'\x91\x00\x80\x00\x80') # drive forward for 2 seconds
time.sleep(2)


connection.write(b'\x91\x01\xF4\x01\xF4') # drive forward faster for 2 seconds 
time.sleep(2)


connection.write(b'\x91\xFF\x00\xFF\x00') # drive reverse
time.sleep(4)

connection.write(b'\x91\x00\x00\x00\x00') # stop the motors



connection.write(b'\xA4\x37\x37\x37\x37') # make display show 7777
time.sleep(2)


connection.write(b'\xA4\x30\x30\x30\x30') # make display show 0000
time.sleep(2)



connection.write(b'\xA4\x32\x30\x30\x32') # make display show 2002
time.sleep(2)


connection.write(b'\x91\x00\x80\x00\x00') # make one wheel drive and the other one stop
time.sleep(2)



connection.write(b'\x91\x00\x80\xFF\x80') # make one wheel drive one directiona and one drive the other
time.sleep(2)


connection.write(b'\x91\x00\x00\x00\x00') # stop the motors

time.sleep(7) # wait 7 seconds so I can pick the robot up

connection.reset_input_buffer() 
connection.reset_output_buffer()
connection.flush()


count = 25 #   how many times the loop will iterate before the robot stops.
while(count != 0):
    time.sleep(2)
    connection.write(b'\x8E\x07') # check for left, right bumper pressed and wheeldrop left and right triggered
    data = connection.read()
    byteH = struct.unpack('B', data)[0]
    binaryH = '{0:08b}'.format(byteH)

    print('---------------------')
   
    print('---------------------')
        
    rightBump =(int(binaryH, 2) & 1 == 1)   #  use bitmasking to isolate and check each status bit to determine which sensors have been triggered
    leftBump = (int(binaryH, 2) & 2 == 2)
    wheelDropRight = (int(binaryH, 2) & 4 == 4)
    wheelDropLeft = (int(binaryH, 2) & 8 == 8)

    connection.reset_input_buffer()        # clear out the buffer so the robot can read the high byte on the next command.
    connection.reset_output_buffer()
    connection.flush()

    connection.write(b'\x8E\x09') # cliff left
    data = connection.read()
    byteH = struct.unpack('B', data)[0]
    binaryH = '{0:08b}'.format(byteH)

    cliffLeft =(int(binaryH, 2) & 1 == 1)

    connection.reset_input_buffer() 
    connection.reset_output_buffer()
    connection.flush()

    connection.write(b'\x8E\x0C') # cliff right
    data = connection.read()
    byteH = struct.unpack('B', data)[0]
    binaryH = '{0:08b}'.format(byteH)

    cliffRight =(int(binaryH, 2) & 1 == 1)

    connection.reset_input_buffer() 
    connection.reset_output_buffer()
    connection.flush()

    connection.write(b'\x8E\x0A') # cliff left front
    data = connection.read()
    byteH = struct.unpack('B', data)[0]
    binaryH = '{0:08b}'.format(byteH)

    cliffLeftFront =(int(binaryH, 2) & 1 == 1)

    connection.reset_input_buffer() 
    connection.reset_output_buffer()
    connection.flush()

    connection.write(b'\x8E\x0B') # cliff right front
    data = connection.read()
    byteH = struct.unpack('B', data)[0]
    binaryH = '{0:08b}'.format(byteH)

    cliffRightFront =(int(binaryH, 2) & 1 == 1)

    connection.reset_input_buffer() 
    connection.reset_output_buffer()
    connection.flush()

    connection.write(b'\x8E\x08') # wall detected
    data = connection.read()
    byteH = struct.unpack('B', data)[0]
    binaryH = '{0:08b}'.format(byteH)

    wallDetected =(int(binaryH, 2) & 1 == 1)

    print('status: '                                    #  create a status readout to console so user can see which sensors have been triggered
    + '\nwallDetected: ' +str(wallDetected)
    + '\nrightBump: ' + str(rightBump) 
    + '\nleftBump: ' + str(leftBump)
    + '\nwheelDropRight: ' + str(wheelDropRight)
    + '\nwheelDropLeft: ' + str(wheelDropLeft)
    + '\ncliffLeft: ' + str(cliffLeft)
    + '\ncliffRight: ' + str(cliffRight)
    + '\ncliffLeftFront: ' + str(cliffLeftFront)
    + '\ncliffRightFront: ' + str(cliffRightFront))


    connection.reset_input_buffer() 
    connection.reset_output_buffer()
    connection.flush()

    time.sleep(5)           #  sleep for 5 seconds between iterations so we can test different sensors.

    
    count = count - 1



connection.write(b'\x80\x07') # start and reset
time.sleep(4)


connection.close()
