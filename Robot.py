####################################################
##   Author:     Samuel Howell
##   Written:	 9-20-22
##   
##   Robot class that we can instantiate to control
##   iRobot Create2.
##
####################################################


import struct
from typing import List
import serial  
import time

class Robot:
	startCMD				=  b'\x80'
	resetCMD				=  b'\x07'
	
	# commands definitions
	start					=  b'\x80'
	safeCMD					=  b'\x83'
	sensors					=  b'\x8E'
	reset					=  b'\x07'
	stopCMD					=  b'\xAD'
	buttons					=  b'\xA5'
	driveDirect				=  b'\x91'
	driveCMD				=  b'\x89'
	leds					=  b'\x8B'
	seekDockCMD             =  b'\x8F'
	
	# packet IDs definitions
	wall					=  b'\x08'  
	bumpsAndWheels			=  b'\x07'
	cliffLeft				=  b'\x09'
	cliffFrontLeft			=  b'\x0A'
	cliffFrontRight			=  b'\x0B'
	cliffRight				=  b'\x0C'
	virtualWall				=  b'\x0D'
	buttons					=  b'\x12'
	distance				=  b'\x13'
	angle					=  b'\x14'
	chargingState			=  b'\x15'
	voltage					=  b'\x16'
	temperature				=  b'\x18'
	batteryCharge			=  b'\x19'
	wallSignal				=  b'\x1B'
	cliffLeftSignal			=  b'\x1C'
	cliffFrontLeftSignal	=  b'\x1D'
	cliffFrontRightSignal	=  b'\x1E'
	cliffRightSignal		=  b'\x1F'
	
	
	def __init__(self, port):
		try:
			self.serial_connection = serial.Serial(port, baudrate=115200,timeout =1)
			print ("Connected!")
		except serial.SerialException:
			print ("Connection failure!")
		time.sleep(1)
		self.serial_connection.close()
		time.sleep(1)
		self.serial_connection.open()

	def sendCommand(self, input):
		self.serial_connection.write(input)

	def closeConnection(self):
		self.serial_connection.close()

	def clearBuffer(self):
		self.serial_connection.reset_input_buffer
		self.serial_connection.reset_output_buffer
		self.serial_connection.flush

	def pController(self, currentByte):
		k = 0.2
		convertedByte = float(currentByte) * k
		intByte = int(convertedByte) # converts the double val to int
		return intByte

	def read(self, howManyBytes):
		self.serial_connection.flushInput()
		
		readList =[]

		for i in range(howManyBytes):
			data1 = self.serial_connection.read()
			byteH = struct.unpack('B', data1)[0]
			binaryH = '{0:08b}'.format(byteH)
			readList.append(binaryH)
			return readList


	def readTwo(self):
		# self.serial_connection.flushInput()
		
		readList =[]


		data1 = self.serial_connection.read()
		data2 = self.serial_connection.read()

		byteH = struct.unpack('B', data1)[0]
		byteL = struct.unpack('B', data2)[0]

		binaryH = '{0:08b}'.format(byteH)
		binaryL = '{0:08b}'.format(byteL)

		num1 = int(binaryH, 2)
		num2 = int(binaryL, 2)

		# readList.append(binaryH)
		# readList.append(binaryL)

		# print("byteH is " + str(byteH) + " binaryH is " + str(binaryH) +" and num 1 would then be " + str(num1<<8))
		# print("byteL is " + str(byteL) + " binaryL is " + str(binaryL) +" and num 2 would then be " + str(num2))
		readList.append(num1 + num2) # bitshft it 8 because it is the high byte

		#binaryCombined = (byteH<<8) + byteL
		#binaryConverted = int(binaryCombined, 2) #converts from binary to decimal
	

		return readList

	def start(self):
	
		self.sendCommand(self.startCMD)
		print ("Started")
		time.sleep(1)



	def stop(self):
		self.sendCommand(self.stopCMD)
		time.sleep(1)
		

	def reset(self):
		self.sendCommand(self.resetCMD)
		time.sleep(2)

	def safe(self):
		self.sendCommand(self.safeCMD)
		time.sleep(1)
		

	def seekDock(self):
		self.sendCommand(self.seekDockCMD)
		

	def drive(self, velocityHighByte, velocityLowByte, radiusHighByte, radiusLowByte):
		arr = [137, velocityHighByte, velocityLowByte, radiusHighByte, radiusLowByte]
		byte_array = bytearray(arr)

		self.sendCommand(byte_array)
		self.clearBuffer()


	def driveDirect(self, rightWheelHighByte, rightWheelLowByte, leftWheelHighByte, leftWheelLowByte):
		arr = [145, rightWheelHighByte, rightWheelLowByte, leftWheelHighByte, leftWheelLowByte]
		byte_array = bytearray(arr)
		#print("hit the drive direct command")
		self.sendCommand(byte_array)
		self.clearBuffer()
		

	def queryLight(self):
		arr = [142, 27]
		byte_array = bytearray(arr)

		self.sendCommand(byte_array)


		

	def leds(self, ledBits, powerColor, powerIntensity):
		arr = [139, ledBits, powerColor, powerIntensity]
		byte_array = bytearray(arr)

		self.sendCommand(byte_array)
		self.clearBuffer()
		

	def digitLEDsASCII(self, digit3, digit2, digit1, digit0):
		arr = [164, digit3, digit2, digit1, digit0]
		byte_array = bytearray(arr)
		self.sendCommand(byte_array)
		self.clearBuffer()

	def playSongOne(self):
		arr = [141, 1]
		byte_array = bytearray(arr)

		self.sendCommand(byte_array)
		self.clearBuffer()

	def playSongTwo(self):
		arr = [141, 2]
		byte_array = bytearray(arr)

		self.sendCommand(byte_array)
		self.clearBuffer()






	# first 16 notes in Mary Had a Little Lamb from  https://riffspot.com/music/mary-had-a-little-lamb-beginner/2331/
	def createSongOne(self):
		# 50 is a quarter note. 100 is a half note. 200 is a whole note
		arr = [140, 1, 16, 
		76, 50, # E
		74, 50, # D
		72, 50, # C
		74, 50, # D
		76, 50, # E
		76, 50, # E
		76, 100, # E
		74, 50, # D
		74, 50, # D
		74, 100, # D
		76, 50, # E
		79, 50, # G
		79, 100, # G
		76, 50, # E
		74, 50, # D
		72, 50, # C
		]
		byte_array = bytearray(arr)

		self.sendCommand(byte_array)
		self.clearBuffer()

	def createSongTwo(self):
				# 50 is a quarter note. 100 is a half note. 200 is a whole note
				arr = [140, 2, 10, 
				74, 50, # D
				76, 50, # E
				76, 50, # E
				76, 50, # E
				76, 50, # E
				74, 50, # D
				74, 50, # D
				76, 50, # E
				74, 50, # D
				72, 200, # C
				]
				byte_array = bytearray(arr)

				self.sendCommand(byte_array)
				self.clearBuffer()
			
	
	
	

