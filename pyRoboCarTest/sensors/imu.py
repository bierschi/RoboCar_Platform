import smbus
from abc import ABC, abstractmethod


class IMU(ABC):

    def __init__(self, address, bus):
        self.address = address
        self.bus = smbus.SMBus(bus)

    @abstractmethod
    def get_accel_data(self, g=False):
        pass

    @abstractmethod
    def get_gyro_data(self):
        pass

    def get_temp(self):
        pass

