import argparse

from sensors import Gearmotor, SteeringMotor, CameraMotor, Ultrasonic, MPU6050
from time import sleep


class RoboCar:

    def __init__(self):

        self.gearmotor = Gearmotor()
        self.steeringmotor = SteeringMotor()
        self.cameramotor = CameraMotor()
        self.ultrasonic = Ultrasonic()
        #self.ultrasonic.start()
        self.imu = MPU6050()

    def test_gearmotor(self):

        for i in range(0, 100, 5):
            print(i)
            self.gearmotor.set_speed(i)
            sleep(0.5)

        for i in range(105, -105, -5):
            print(i)
            self.gearmotor.set_speed(i)
            sleep(0.5)

        for i in range(-100, 5, 5):
            print(i)
            self.gearmotor.set_speed(i)
            sleep(0.5)

    def test_servomotors(self):

        for i in range(0, 100, 5):
            print(i)
            self.steeringmotor.move(i)
            self.cameramotor.move(i)
            sleep(0.5)

        for i in range(105, 0, -5):
            print(i)
            self.steeringmotor.move(i)
            self.cameramotor.move(i)
            sleep(0.5)

        for i in range(0, 55, 5):
            print(i)
            self.steeringmotor.move(i)
            self.cameramotor.move(i)
            sleep(0.5)


def main():

    # pyRoboCarTest usage
    usage1 = ""

    usage2 = ""

    description = "pyRoboCarTest\n\nUsage:\n    {}\n    {}".format(usage1, usage2)

    # parse arguments for pyRoboCarTest
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawDescriptionHelpFormatter)

    # parse all arguments
    args = parser.parse_args()

    robocar = RoboCar()
    #robocar.test_gearmotor()
    robocar.test_servomotors()

    while True:
        sleep(1)

if __name__ == '__main__':
    main()
