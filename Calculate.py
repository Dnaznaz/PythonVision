import platform
import subprocess
import os
import networktables
import math


class Point():
    def __init__(self, x, y):
        self.X = x
        self.Y = y


class GRIPClaculator():
    resolutionX = 640
    resolutionY = 480
    offsetX = 0
    offsetY = 0
    cTable = None
    lTable = None

    def __init__(self):
        networktables.NetworkTable.setClientMode()
        try:
            cTable = networktables.networktable.NetworkTable.getTable("GRIP/Contoures")
            lTable = networktables.networktable.NetworkTable.getTable("GRIP/Lines")
        except Exception:
            print(Exception.args)

    def CalculateTargetAngleX():
        if(cTable == None || lTabel == None):
            throw new NUllPointerException()
        dst = calculateTargetPoint()

        targetAngle = math.degrees(math.atan((-resolutionY + dst.y)/(resolutionX/2 - dst.x)))
		if (targetAngle < 0):
            targetAngle = 180 + targetAngle
		return (targetAngle - 90)/2 #negative to left, positive to right
    
    def CalculateTargetAngleY():
        
        if(cTable == None || lTabel == None):
            throw new NUllPointerException()
        dst = calculateTargetPoint()

        targetAngle = math.degrees(math.atan((-resolutionY/2 + dst.y)/(-dst.x)))
		return targetAngle #negative is down, positive is up

    def CalculateTargetPoint(self):
        cX = cTable.getNumberArray("centerX", defaultValue)
        cY = cTable.getNumberArray("centerY", defaultValue)
        cHeight = cTable.getNumberArray("height", defaultValue)
        cWidth = cTable.getNumberArray("width", defaultValue)
        cArea = cTable.getNumberArray("area", defaultValue)
        lX1 = lTable.getNumberArray("x1", defaultValue)
        lY1 = lTable.getNumberArray("y1", defaultValue)
		
		if(cArea.count == 0 || lX1.count == 0):
            throw new NullPointerException()
		
		target = 0
		if (cArea.count > 1):
			for i in range(1, cArea.count):
				if (cArea[i] > cArea[target]):
					target = i
		
		targetLines = []
		for i in range(0, lX1.count):
			if ((lX1[i] >= cX[target] - (cWidth[target]/2) and lX1[i] <= cX[target] + (cWidth[target]/2)) and
					(lY1[i] >= cY[target] - (cHeight[target]/2) and lY1[i] <= cY[target] + (cHeight[target]/2))):
				targetLines.add(i)

		if(targetLines.count < 1):
				throw new NullPointerException()	
		elif (targetLines.count > 1):
			target = 0
			for i in range(1, targetLines.count + 1):
				if (lX1[target] < lX1[i])
					target = i;
		else:
			target = 0
		point = new Point(lX1[target], lY1[target])
		return point

def startGRIP():
    print("The file is at %s", os.path.dirname(os.path.realpath(__file__))#Debug
    #subprocess.call(os.path.dirname(os.path.realpath(__file__)) + "\GRIPStarter.sh")


def main():
    startGRIP()

    #calculator = GRIPClaculator()


if __name__ == '__main__':
    main()