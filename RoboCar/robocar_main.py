import argparse
from time import sleep

from sensors import Gearmotor, SteeringMotor, CameraMotor, Ultrasonic, MPU6050
from __init__ import __version__


class RoboCar:

    def __init__(self):

        self.gearmotor = Gearmotor()
        self.steeringmotor = SteeringMotor()
        self.cameramotor = CameraMotor()
        self.ultrasonic = Ultrasonic()
        #self.ultrasonic.start()
        self.imu = MPU6050()


def main():

    # RoboCar usage
    usage1 = "RoboCar gearmotor --speed 50"
    usage2 = "RoboCar steeringmotor --move 25"
    usage3 = "RoboCar cameramotor --move 75"
    usage4 = "RoboCar ultrasonic --distance"
    usage5 = "RoboCar imu --acc"
    usage6 = "RoboCar camera --port 8080"

    description = "Test and Validation Package for the RoboCar Platform\n\nUsage:\n    {}\n    {}\n    {}\n    {}\n    {}\n    {}".format(usage1, usage2, usage3, usage4, usage5, usage6)

    # parse arguments for RoboCar
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawDescriptionHelpFormatter)

    subparser = parser.add_subparsers(dest='parseoption', help='Choose between gearmotor, steeringmotor, cameramotor, ultrasonic, imu, camera')

    gearmotor_parser = subparser.add_parser('gearmotor', help='Options for the gearmotor')

    steeringmotor_parser = subparser.add_parser('steeringmotor', help='Options for the steeringmotor')
    cameramotor_parser = subparser.add_parser('cameramotor', help='Options for the cameramotor')
    ultrasonic_parser = subparser.add_parser('ultrasonic', help='Options for the ultrasonic')
    imu_parser = subparser.add_parser('imu', help='Options for the imu')
    camera_parser = subparser.add_parser('camera', help='Options for the camera')

    gearmotor_parser.add_argument('-s', '--speed', type=str, help='Sets the speed for the gearmotor (-100 - 100)')
    gearmotor_parser.add_argument('-a', '--all', action='store_true', help='Test the extrema position from the gearmotor')

    steeringmotor_parser.add_argument('-m', '--move', type=str, help='Sets the direction of the steering: 0-50 left, 51-100 right')
    steeringmotor_parser.add_argument('-a', '--all', action='store_true', help='Test the extrema position of the steering motor')

    cameramotor_parser.add_argument('-m', '--move', type=str, help='Sets the direction of the cameramotor: 0-50 left, 51-100 right')
    cameramotor_parser.add_argument('-a', '--all', action='store_true', help='Test the extrema position of the camera motor')

    ultrasonic_parser.add_argument('-d', '--distance', action='store_true', help='Print out the distance measurement of the ultrasonic sensor', required=True)

    imu_parser.add_argument('-acc', '--acc', action='store_true', help='Sets the direction of the cameramotor: 0-50 left, 51-100 right')
    imu_parser.add_argument('-g', '--gyro', action='store_true', help='Sets the direction of the cameramotor: 0-50 left, 51-100 right')
    imu_parser.add_argument('-a', '--all', action='store_true', help='Test the extrema position of the camera motor')

    camera_parser.add_argument('-p', '--port', type=int, help='Sets the port for the server')

    parser.add_argument('-v', '--version', action='version',    version=__version__, help='shows the current version')

    # parse all arguments
    args = parser.parse_args()

    if args.parseoption == 'gearmotor':
        if args.speed is not None and args.all is False:
            speed = int(args.speed)

            gearmotor = Gearmotor()
            gearmotor.set_speed(value=speed)

            try:
                while True:
                    sleep(1)
            except KeyboardInterrupt:
                gearmotor.set_speed(value=0)

        elif args.all is True and args.speed is None:

            gearmotor = Gearmotor()
            try:
                gearmotor.test_extrema()
            except KeyboardInterrupt:
                gearmotor.set_speed(0)
        else:
            gearmotor_parser.error("Use either -s or -a as argument")

    elif args.parseoption == 'steeringmotor':
        if args.move is not None and args.all is False:
            move = int(args.move)

            steeringmotor = SteeringMotor()
            steeringmotor.move(value=move)

        elif args.all is True and args.move is None:

            steeringmotor = SteeringMotor()
            try:
                steeringmotor.test_extrema()
            except KeyboardInterrupt:
                steeringmotor.move(50)
        else:
            steeringmotor_parser.error("Use either -m or -a as argument")

    elif args.parseoption == 'cameramotor':
        if args.move is not None and args.all is False:
            move = int(args.move)

            cameramotor = CameraMotor()
            cameramotor.move(value=move)

        elif args.all is True and args.move is None:

            cameramotor = CameraMotor()
            try:
                cameramotor.test_extrema()
            except KeyboardInterrupt:
                cameramotor.move(50)
        else:
            cameramotor_parser.error("Use either -m or -a as argument")

    elif args.parseoption == 'ultrasonic':
        ultrasonic = Ultrasonic()
        while True:
            print("Distance: {} cm".format(ultrasonic.get_distance()))
            sleep(1)

    elif args.parseoption == 'imu':
        if args.acc is True and args.gyro is False and args.all is False:
            imu = MPU6050()

            while True:
                acc = imu.get_accel_data()
                print("AX: {}, AY: {}, AZ: {} m/s²".format(acc['x'], acc['y'], acc['z']))
                sleep(1)

        elif args.gyro is True and args.acc is False and args.all is False:
            imu = MPU6050()

            while True:
                gyro = imu.get_gyro_data()
                print("GX: {}, GY: {}, GZ: {}".format(gyro['x'], gyro['y'], gyro['z']))
                sleep(1)

        elif args.all is True and args.acc is False and args.gyro is False:
            imu = MPU6050()

            while True:
                acc = imu.get_accel_data()
                gyro = imu.get_gyro_data()
                print("AX: {}, AY: {}, AZ: {} m/s² GX: {}, GY: {}, GZ: {}".format(acc['x'], acc['y'], acc['z'], gyro['x'], gyro['y'], gyro['z']))
                sleep(1)
        else:
            imu_parser.error("Use either --acc, --gyro or -a as argument")

    elif args.parseoption == 'camera':
        pass

    else:
        parser.error("No parameter provided!")
    #robocar = RoboCar()
    #robocar.test_gearmotor()
    #robocar.test_servomotors()

    #while True:
    #    sleep(1)

if __name__ == '__main__':
    main()
