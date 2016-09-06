import platform
import subprocess
import os
from pynetworktables import Networktable
import math

def startNetworkTables(ipAddress):
        Networktable.setIPAddress(ipAddress)
        NetworkTable.setClientMode()
        Networktable.initalize()

def getTable(param, path):
        try:
            param = NetworkTable.getTable(path)
        except Exception:
            print(Exception.args)

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


class GRIPClaculator:
    resolutionX
    resolutionY
    offsetX
    offsetY
    cTable
    lTable

    def __init__(self):
        resolutionX = 640
        resolutionY = 480
        offsetX = 0
        offsetY = 0
        cTable = None
        lTable = None

        while cTable == None:
            getTable(cTable, "GRIP/Contoures")
        while lTable == None:
            getTable(lTable, "GRIP/Lines")
        
    def getTargetX(self):
        dst = calculateTargetPoint()

        targetAngle = math.degrees(math.atan((-resolutionY + dst.y)/(resolutionX/2 - dst.x)))
		if (targetAngle < 0):
            targetAngle = 180 + targetAngle
		return (targetAngle - 90)/2 #negative to left, positive to right
    
    def getTargetY(self):
        dst = calculateTargetPoint()
        
        targetAngle = math.degrees(math.atan((-resolutionY/2 + dst.y)/(-dst.x)))
		return targetAngle #negative is down, positive is up

    def calculateTargetPoint(self):
        if(cTable == None):
            raise 'No contours table'
        if(lTable == None):
            raise 'No lines table'

        centerX = cTable.getNumber("centerX")
        centerY = cTable.getNumber("centerY")
        height = cTable.getNumber("height")
        width = cTable.getNumber("width")
        targetX = lTable.getNumber("x1")
        targetY = lTable.getNumber("y1")
        targetLen = lTable.getNumber("length")
		
		if(centerX.count == 0 or centerY.count == 0 or height.count == 0 or width.count == 0 or targetX.count == 0 or targetY.count == 0):
            raise 'No area or targetX'
		
		target = 0
        for i in range(1, width.count + 1):
            if (width[i] < width[target]):
                target = i
		
		targetLines = []
		for i in range(0, targetX.count + 1):
			if ((targetX[i] >= centerX[target] - (width[target]/2) and targetX[i] <= centerX[target] + (width[target]/2)) and
            (targetY[i] >= centerY[target] - (height[target]/2) and targetY[i] <= centerY[target] + (height[target]/2))):
				targetLines.append(i)

		if(targetLines.count < 1):
				raise 'No lines found'
		elif (targetLines.count > 1):
			target = 0
			for i in range(1, targetLines.count + 1):
				if (targetX[target] < targetX[i])
					target = i;
		else:
			target = 0

		return Point(targetX[target], targetY[target])

def startGRIP():
    print("The file is at %s", os.path.dirname(os.path.realpath(__file__))#Debug
    #subprocess.call(os.path.dirname(os.path.realpath(__file__)) + "\GRIPStarter.sh")


def main():
    startGRIP()
    calculator = GRIPClaculator('10.43.20.2')
    
    requestsTable = None
    while requestsTable == None:
        getTable(requestsTable, 'ImageRequests')

    while not requestsTable.getBoolean('close'):
        if(requestsTable.getBoolean('shooterReq') == True):
            requestsTable.putNumber('shooterError', calculator.getTargetY())
        if(requestsTable.getBoolean('chassisReq') == True):
            requestsTable.putNumber('chassisError', calculator.getTargetX)

if __name__ == '__main__':
    main()