import wiringpi
from time import sleep

MAX_SPEED = 480


class Gearmotor:

    def __init__(self, pwm_pin=12, direction_pin=5):
        """

        :param pwm_pin:
        :param direction_pin:
        """

        self.pwm_pin = pwm_pin
        self.direction_pin = direction_pin

        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(self.pwm_pin, wiringpi.GPIO.PWM_OUTPUT)
        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
        wiringpi.pwmSetRange(MAX_SPEED)
        wiringpi.pwmSetClock(2)

        wiringpi.pinMode(self.direction_pin, wiringpi.GPIO.OUTPUT)

    def set_speed(self, speed):

        if speed < 0:
            speed = -speed
            dir_value = 1
        else:
            dir_value = 0

        if speed > MAX_SPEED:
            speed = MAX_SPEED

        wiringpi.digitalWrite(self.direction_pin, dir_value)
        wiringpi.pwmWrite(self.pwm_pin, speed)

    def set_speed2(self, value):
        """

        :param value:
        :return:
        """

        if 0 <= value <= 100:
            backward_direction = 0
        elif -100 <= value < 0:
            value = -value
            backward_direction = 1
        else:
            if value > 100:
                value = 100
                backward_direction = 0
            elif value < -100:
                value = 100
                backward_direction = 1
            else:
                backward_direction = 0

        speed = int(value * 4.8)
        wiringpi.digitalWrite(self.direction_pin, backward_direction)
        wiringpi.pwmWrite(self.pwm_pin, speed)

if __name__ == '__main__':
    motor = Gearmotor()

    #for i in range(0, 100, 5):
    #    print(i)
    #    motor.set_speed2(i)
    #    sleep(0.5)

    for i in range(100, -100, -5):
        #print(i)
        motor.set_speed2(i)
        sleep(1)
