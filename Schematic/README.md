## Schematic for the RoboCar Platform

![](schematic_robocar_platform.png)


## GPIO (BCM) / Bus Mapping

**Gearmotor** <br>
GPIO 5: Direction Pin <br>
GPIO 12: PWM Pin <br>

**HC-SR04** <br>
GPIO 23: Trigger Pin <br>
GPIO 24: Echo Pin <br>

**MPU9250** <br>
I2C Bus address: 0x68 <br>

**CameraServoMotor** <br>
Channel 14 <br>
I2C Bus address: 0x40 <br>

**SteeringServoMotor** <br>
Channel: 15 <br>
I2C Bus address: 0x40 <br>

**RPLidar A2** <br>
Connected to USB `/dev/ttyUSBO` <br>
Baurdate: 115200


