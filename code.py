import time
import board
import digitalio
import pwmio

from adafruit_motor import motor

left_motor_forward = board.GP12
left_motor_backward = board.GP13

pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000)
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb)
Left_Motor_speed = 0

right_motor_forward = board.GP14
right_motor_backward = board.GP15

pwm_Ra = pwmio.PWMOut(right_motor_forward, frequency=10000)
pwm_Rb = pwmio.PWMOut(right_motor_backward, frequency=10000)

Right_Motor = motor.DCMotor(pwm_Ra, pwm_Rb)
Right_Motor_speed = 0


while True:

    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(2)
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(2)

    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)


# Write your code here :-)
