import time
import RPi.GPIO as GPIO


class Ultrasonic:

    def __init__(self, trigger=23, echo=24):
        """ Class Ultrasonic to measure the distance to obstacles

        :param trigger: pin for the trigger
        :param echo: pin for the echo
        """
        self.trigger = trigger
        self.echo = echo

        self.pulse_start = 0
        self.pulse_end = 0

        # define board layout
        GPIO.setmode(GPIO.BCM)

        # set trigger pin as output and echo pin as input
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def __del__(self):
        """destructor"""

        GPIO.cleanup()

    def measurement(self):
        """ performs the measurement

        :return: raw distance measurement
        """

        if GPIO.input(self.trigger):
            GPIO.output(self.trigger, False)
            time.sleep(0.0001)

        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)

        while GPIO.input(self.echo) == 0:
            self.pulse_start = time.time()

        while GPIO.input(self.echo) == 1:
            self.pulse_end = time.time()

        return self.pulse_end - self.pulse_start

    def get_distance(self):
        """ get the distance in cm

        :return: distance in cm
        """
        pulse_duration = self.measurement()
        distance = pulse_duration * 17150

        distance = round(distance, 4)
        #print("Distance: {} cm".format(distance))

        return distance


if __name__ == '__main__':
    ultrasonic = Ultrasonic()
    while True:
        ultrasonic.get_distance()
        time.sleep(0.1)
