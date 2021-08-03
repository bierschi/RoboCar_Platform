## Ubuntu MATE 20.04 LTS

### Ubuntu/ROS Version Mapping
- Ubuntu MATE 20.04 LTS <-> [ROS Noetic](http://wiki.ros.org/noetic)
- Ubuntu MATE 18.04 LTS <-> [ROS Melodic](http://wiki.ros.org/melodic)
- Ubuntu MATE 16.04 LTS <-> [ROS Kinetic](http://wiki.ros.org/kinetic)

For older versions 1604/1804 checkout the Ubuntu Mate [Archive](https://releases.ubuntu-mate.org/archived/)

### Ubuntu Settings

Download Ubuntu MATE 20.04 LTS from [https://ubuntu-mate.org/raspberry-pi/](https://ubuntu-mate.org/raspberry-pi/)

Set hostname to `robocar`
<pre><code>
sudo hostnamectl set-hostname robocar
</code></pre>

Update (Upgrade) APT package manager and install packages
<pre><code>
sudo apt update
(sudo apt upgrade)
sudo apt install net-tools ssh python3-pip curl cmake wiringpi
</code></pre>

Enable the necessary interfaces with `raspi-config`

<pre><code>
sudo raspi-config
</code></pre>

if not available, please download the following script
<pre><code>
wget https://github.com/EmilGus/install_raspi-config/blob/master/install.sh
sudo sh install.sh
sudo raspi-config
</code></pre>

Add user to group `dialout` to access the usb ports

<pre><code>
sudo usermod -a -G dialout &lt;user&gt;
</code></pre>

Make sure that the following interfaces work correctly:
- Wifi
- Bluetooth
- Camera
- SSH
- I2C

### Install [ROS Noetic](http://wiki.ros.org/noetic)

Add the official ROS repo to sources.list
<pre><code>
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
</code></pre>

Update the sources list
<pre><code>
echo "deb http://packages.ros.org/ros/ubuntu focal main" | sudo tee /etc/apt/sources.list.d/ros-focal.list
</code></pre>

Add the ROS keyserver
<pre><code>
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
</code></pre>

or alternative
<pre><code>
curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -
</code></pre>

Update the apt package manager
<pre><code>
sudo apt update
</code></pre>

Install ROS Noetic
<pre><code>
sudo apt install ros-noetic-desktop
(sudo apt install ros-melodic-desktop)
</code></pre>


### ROS Settings
Setup ROS environment
<pre><code>
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source /opt/ros/noetic/setup.bash
</code></pre>

Start the roscore to check wether everything works or not
<pre><code>
roscore
</code></pre>

Create a file named `roscore.service` in `/etc/systemd/system` and insert:
<pre><code>
[Unit]
Description=Start roscore master as a systemd service

[Service]
Type=simple
ExecStart=/bin/bash -c "source /opt/ros/noetic/setup.bash; /usr/bin/python3 /opt/ros/noetic/bin/roscore"
Restart=on-failure

[Install]
WantedBy=multi-user.target
</code></pre>

Enable this service file on boot
<pre><code>
sudo systemctl enable roscore.service
</code></pre>

Now the roscore master should be available on each boot. Check the status with:
<pre><code>
sudo systemctl status roscore.service
</code></pre>

### WiringPi
Version 2.52 is needed for RPi4
<pre><code>
cd /tmp
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
</code></pre>

Test the gpio`s
<pre><code>
gpio -v
gpio readall
</code></pre>

### Troubleshooting 
Known errors during the installation of 16.04 or 18.04 <br> <br>

`sshd` gives the error `error: Could not load host key: /etc/ssh/ssh_host_rsa_key`. Execute this command to resolve the problem
<pre><code>
sudo /usr/bin/ssh-keygen -A
</code></pre>

ROS Melodic installation Tutorial
<pre><code>
https://varhowto.com/install-ros-melodic-ubuntu-18-04/
</code></pre>

