# RoboCar Platform
RoboCar is a low cost Autonomous Driving Platform

- Low cost [Hardware](https://github.com/bierschi/RoboCar_Platform/tree/main/Hardware) Components
- Sensor Suit for an AD Platform (Lidar, IMU, Ultrasonic, Camera, Motors)  
- [Schematic](https://github.com/bierschi/RoboCar_Platform/tree/main/Schematic) for the RoboCar Platform
- Provides all Settings for the Ubuntu MATE [Operating System](https://github.com/bierschi/RoboCar_Platform/tree/main/OperatingSystem)
- Control the Platform with the [RoboCar](https://github.com/bierschi/RoboCar_Platform/tree/main/RoboCar) Python Package
- C++ Software Development Kit [RoboCar_SDK](https://github.com/bierschi/RoboCar_SDK) in Development

![](Images/robocar_platform.png)

## Installation
Install [RoboCar]() with pip
<pre><code>
pip3 install RoboCar
</code></pre>

or from source code
<pre><code>
git clone https://github.com/bierschi/RoboCar_Platform.git
cd RoboCar_Platform
sudo python3 setup.py install
</code></pre>

## Usage

<pre><code>
RoboCar --help
</code></pre>

<pre><code>
RoboCarControl --help
</code></pre>

## Changelog
All changes and versioning information can be found in the [CHANGELOG](https://github.com/bierschi/RoboCar_Platform/blob/master/CHANGELOG.rst)

## License
Copyright (c) 2021 Bierschneider Christian. See [LICENSE](https://github.com/bierschi/RoboCar_Platform/blob/master/LICENSE)
for details
