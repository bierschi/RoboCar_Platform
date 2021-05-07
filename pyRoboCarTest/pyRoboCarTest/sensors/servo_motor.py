from abc import ABC, abstractmethod
from Adafruit_PCA9685 import PCA9685
from time import sleep


class ServoMotor(ABC):

    def __init__(self, channel, frequency=60):
        """ Base class ServoMotor

        :param channel: used channel
        :param frequency: used frequency
        """
        self.channel = channel
        self.frequency = frequency

        self.pwm = PCA9685()
        self.pwm.set_pwm_freq(self.frequency)

    def set_movement(self, value):
        """ set movement for the servo motor

        :param value: value as int
        """
        self.pwm.set_pwm(self.channel, 0, value)

    @abstractmethod
    def move(self, value):
        """ abstract method move

        :param value: value as int
        """
        pass


class SteeringMotor(ServoMotor):

    def __init__(self, channel=15, frequency=60):
        """ class SteeringMotor

        :param channel: used channel
        :param frequency: used frequency
        """
        # init base class
        super().__init__(channel, frequency)

        self.min = 150
        self.max = 490

        self.middle = 360

        self.range_factor_left = 200
        self.factor_left = self.range_factor_left/50

        self.range_factor_right = 140
        self.factor_right = self.range_factor_right/50

    def move(self, value=50):
        """ move the servomotor with the given value

        :param value: value between 0 and 100, 0-50: left, 50-100: right
        """
        if 0 <= value < 50:  # left direction
            calc = int(self.middle + ((value * self.factor_left) - self.range_factor_left))
            self.set_movement(value=int(calc))
        elif 50 <= value <= 100:  # right direction
            calc = int(self.middle + ((value * self.factor_right) - self.range_factor_right))
            self.set_movement(value=calc)
        else:
            print("Value not in range of 0 - 100!")


class CameraMotor(ServoMotor):

    def __init__(self, channel=14, frequency=60):
        """ class CameraMotor

        :param channel: used channel
        :param frequency: used frequency
        """
        # init base class
        super().__init__(channel, frequency)

        self.min = 170
        self.max = 560

        self.middle = 370
        self.range_factor = (self.max - self.min) / 2
        self.factor = self.range_factor/50

    def move(self, value=50):
        """ move the servomotor with the given value

        :param value: value between 0 and 100, 0-50: left, 50-100: right
        """

        if 0 <= value < 50:  # left direction
            calc = int(self.middle - ((value * self.factor) - self.range_factor))
            self.set_movement(value=calc)
        elif 50 <= value <= 100:  # right direction
            calc = int(self.middle - ((value * self.factor) - self.range_factor))
            self.set_movement(value=calc)
        else:
            print("Value not in range of 0 - 100!")


if __name__ == '__main__':

    steering = SteeringMotor(channel=15)
    camera = CameraMotor(channel=14)

    for i in range(0, 105, 5):
        print(i)
        steering.move(i)
        camera.move(i)
        sleep(0.1)

    for i in range(100, 0, -5):
        print(i)
        steering.move(i)
        camera.move(i)
        sleep(0.1)

    for i in range(0, 55, 5):
        print(i)
        steering.move(i)
        camera.move(i)
        sleep(0.1)
