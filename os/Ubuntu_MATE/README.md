## Ubuntu MATE 20.04 LTS

Download Ubuntu MATE 20.04 LTS from
<pre><code>
https://ubuntu-mate.org/raspberry-pi/
</code></pre>

Set hostname to
<pre><code>
robocar
</code></pre>

Install packages
<pre><code>
sudo apt update
sudo apt upgrade
sudo apt install net-tools ssh python3-pip cmake
</code></pre>

Enable the necessary interfaces
<pre><code>
wget https://github.com/EmilGus/install_raspi-config/blob/master/install.sh
sudo sh install.sh
sudo raspi-config
</code></pre>

Make sure that the following interfaces work:
- Wifi
- Bluetooth
- Camera
- SSH
- I2C

Install ROS Noetic
<pre><code>
https://roboticsbackend.com/install-ros-on-raspberry-pi-3/
https://varhowto.com/install-ros-noetic-ubuntu-20-04/
</code></pre>
