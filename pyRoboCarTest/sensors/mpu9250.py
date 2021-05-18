from sensors import IMU


class MPU9250(IMU):

    def __init__(self, address=0x68, bus=1):

        super().__init__(address=address, bus=bus)

