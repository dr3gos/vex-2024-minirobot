
# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Project:      AISB VEX 23'-24' Test Code                                   #
# 	Author:       Dragos S.                                                    #
# 	Created:      26/09/2023                                                   #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import math

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello V5")

controller_1 = Controller(PRIMARY)
leftRear = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)       
rightRear = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)       
leftFront = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)       
rightFront = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
lifterMotor = Motor(Ports.PORT5, GearSetting.RATIO_36_1, False)
# puncher = Motor(Ports.PORT15, GearSetting.RATIO_36_1, False)

wait(30, MSEC)

# Functions

# Driving function

# !!! TEST CODE STARTS HERE !!!
# def driving():
#     # input and initial processing
#     x = controller_1.axis3.position() #updown left
#     y = -controller_1.axis4.position() #leftright left
#     turn = controller_1.axis1.position() #lefright right
#     theta = math.atan2(y,x)
#     power = x ** y

#     # further processing
#     sin = math.sin(theta - (math.pi/4))
#     cos = math.cos(theta - (math.pi/4))
#     max_val = max(abs(sin), abs(cos))


#     leftFrontPower = power * cos/max_val + turn
#     rightFrontPower = power * sin/max_val - turn
#     leftRearPower = power * sin/max_val + turn
#     rightRearPower = power * cos/max_val - turn

#     if (power + abs(turn)) < 1:
#         leftFrontPower /= power + abs(turn)
#         rightFrontPower /= power + abs(turn)
#         leftRearPower /= power + abs(turn)
#         rightRearPower /= power + abs(turn)

#     leftFront.set_velocity(leftFrontPower, PERCENT)
#     rightFront.set_velocity(rightFrontPower, PERCENT)
#     leftRear.set_velocity(leftRearPower, PERCENT)
#     rightRear.set_velocity(rightRearPower, PERCENT)

#     leftFront.spin(FORWARD)
#     rightFront.spin(FORWARD)
#     leftRear.spin(FORWARD)
#     rightRear.spin(FORWARD)

# def test():
#     leftFront.set_velocity(10, PERCENT)
#     rightFront.set_velocity(10, PERCENT)
#     leftRear.set_velocity(10, PERCENT)
#     rightRear.set_velocity(10, PERCENT)

#     leftFront.spin(FORWARD)
#     rightFront.spin(FORWARD)
#     leftRear.spin(FORWARD)
#     rightRear.spin(FORWARD)
# !!! TEST CODE ENDS HERE !!!

def move(direction, power, duration):
# 1 = forward, 2 = backward, 3 = left, 4 = right
    if direction == 1:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(REVERSE)
        rightFront.spin(REVERSE)
        leftRear.spin(REVERSE)
        rightRear.spin(REVERSE)
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()
    if direction == 2:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(FORWARD)
        rightFront.spin(FORWARD)
        leftRear.spin(FORWARD)
        rightRear.spin(FORWARD)
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()
    if direction == 3:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(FORWARD) #f
        rightFront.spin(REVERSE) #r
        leftRear.spin(FORWARD) #f
        rightRear.spin(REVERSE) #r
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()
    if direction == 4:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(REVERSE)
        rightFront.spin(FORWARD)
        leftRear.spin(REVERSE)
        rightRear.spin(FORWARD)
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()

def autonomous():
    move(1, 30, 800)

def lifting():
    if controller_1.buttonR1.pressing():
        lifterpower = 100
    elif controller_1.buttonL1.pressing():
        lifterpower = -100
    else:
        lifterpower = 0
    lifterMotor.set_velocity(lifterpower, PERCENT)
    lifterMotor.spin(FORWARD)


def drivingsimple():
    speed = -controller_1.axis3.position() * retarder #updown left
    # strafe = controller_1.axis4.position() #leftright left
    turn = controller_1.axis1.position() * lrretarder  #leftright right

    leftFrontPower = (speed + turn)
    rightFrontPower = (speed - turn)
    # leftFrontPower = (speed)
    # rightFrontPower = (speed)
    leftRearPower = (speed + turn)
    rightRearPower = (speed - turn)

    leftFront.set_velocity(leftFrontPower, PERCENT)
    rightFront.set_velocity(rightFrontPower, PERCENT)
    leftRear.set_velocity(leftRearPower, PERCENT)
    rightRear.set_velocity(rightRearPower, PERCENT)

    leftFront.spin(FORWARD)
    rightFront.spin(FORWARD)
    leftRear.spin(FORWARD)
    rightRear.spin(FORWARD)

# def punch():
#     puncher.set_velocity(100, PERCENT)
#     if controller_1.buttonR2.pressing():
#          puncher.spin(FORWARD)
#     elif controller_1.buttonL2.pressing():
#         puncher.spin(REVERSE)
#     else:
#          puncher.stop()

# init code
retarder = 1
lrretarder = 1


# Main loop
while 1:
    if controller_1.buttonRight.pressing():
        autonomous()
    if controller_1.buttonLeft.pressing():
        while 1:
            drivingsimple()
            # punch()
            lifting()
            if controller_1.buttonUp.pressing():
                if retarder < 1:
                    retarder = round(retarder + 0.1, 2)
                    controller_1.rumble("-")
                    # retarderString = "Retarder: " + str(round(retarder, 2))
                    retarderString = "Retarder: " + str(retarder )
                    controller_1.screen.clear_screen()
                    controller_1.screen.set_cursor(1,1)
                    controller_1.screen.print(retarderString)
                wait(100, MSEC)
            if controller_1.buttonDown.pressing():
                if retarder >= 0.1:
                    retarder = round(retarder - 0.1, 2)
                    controller_1.rumble("-")
                    retarderString = "Retarder: " + str(round(retarder, 2))
                    controller_1.screen.clear_screen()
                    controller_1.screen.set_cursor(1,1)
                    controller_1.screen.print(retarderString)
            if controller_1.buttonLeft.pressing():
                if lrretarder < 1:
                    lrretarder = round(lrretarder + 0.1, 2)
                    lrretarderString = "LR Retarder: " + str(round(lrretarder, 2))
                    controller_1.rumble("-")
                    controller_1.screen.clear_screen()
                    controller_1.screen.set_cursor(1,1)
                    controller_1.screen.print(lrretarderString)
                wait(100, MSEC)
            if controller_1.buttonRight.pressing():
                if lrretarder >= 0.1:
                    lrretarder = round(lrretarder - 0.1, 2)
                    lrretarderString = "LR Retarder: " + str(round(lrretarder, 2))
                    controller_1.rumble("-")
                    controller_1.screen.clear_screen()
                    controller_1.screen.set_cursor(1,1)
                    controller_1.screen.print(lrretarderString)
                    wait(100, MSEC)


            






    # if controller_1.buttonRight.pressing():
    #     while 1:
    #         driving()

    # if controller_1.buttonDown.pressing():
    #     while 1:
    #         test()
    

    wait(5, MSEC)

    


