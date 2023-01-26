# CraftBeerPi 4

[![Build](https://github.com/avollkopf/craftbeerpi4/actions/workflows/build.yml/badge.svg)](https://github.com/avollkopf/craftbeerpi4/actions/workflows/build.yml)
[![GitHub license](https://img.shields.io/github/license/avollkopf/craftbeerpi4)](https://github.com/avollkopf/craftbeerpi4/blob/master/LICENSE)
![GitHub issues](https://img.shields.io/github/issues-raw/avollkopf/craftbeerpi4)
![PyPI](https://img.shields.io/pypi/v/cbpi4)
![Happy Brewing](https://img.shields.io/badge/CraftBeerPi%204-Happy%20Brewing-%23FBB117)

<p align="center">
  <img src="https://github.com/avollkopf/craftbeerpi4-ui/blob/main/cbpi4gui/public/logo192.png?raw=true" alt="CraftBeerPi Logo"/>
</p>

CraftBeerPi 4 is an open source software solution to control the brewing and
fermentation of beer :beer:.

## 📚 Documentation
Instructions on how to install CraftBeerPi and use its plugins is described
in the documentation, that can be found here: [gitbook.io](https://openbrewing.gitbook.io/craftbeerpi4_support/).

### Plugins
Plugins extend the base functionality of CraftBeerPi 4.
You can find a list of available plugins [here](https://openbrewing.gitbook.io/craftbeerpi4_support/master/plugin-installation#plugin-list).

## 🧑‍🤝‍🧑 Contribute
You want to help develop CraftBeerPi4? To get you quickly stated, this repository comes with a preconfigured
development environment. To be able to use this environment you need 2 things installed on your computer:

- docker
- visual studio code (vscode)

To start developing clone this repository, open the folder in vscode and use the _development container_ feature. The command is called _Reopen in container_. Please note that this quick start setup does not work if you want to develop directly on a 32bit raspberry pi os because docker is only available for 64bit arm plattform. Please use the regular development setup for that.

For a more detailed description of a development setup without the _development container_ feature see the documentation page:
[gitbook.io](https://openbrewing.gitbook.io/craftbeerpi4_support/)

### Contributors
Thanks to all the people who have contributed

[![contributors](https://contributors-img.web.app/image?repo=avollkopf/craftbeerpi4)](https://github.com/avollkopf/craftbeerpi4/graphs/contributors)

## Install on Radxa Rock3
### Enable One Wire GPIO (DS18b20 sensors)
```bash
echo dtoverlay=$(ls /boot/dtbs/$(uname -r)/rockchip/overlay/*w1-gpio* | sed -e 's/\.dtbo$//' | xargs -n 1 basename) | sudo tee -a /boot/config.txt > /dev/null
sudo /usr/local/sbin/update_extlinux.sh
sudo reboot
```

Test by listing one wire devices :
```bash
sudo modprobe w1-gpio
sudo modprobe w1-therm
ls /sys/bus/w1/devices
```

### Enable PWM 

### Prereq
```bash
sudo apt install python3.9 python3.9-dev python3.9-distutils
curl -sS https://bootstrap.pypa.io/get-pip.py | sudo python3.9
sudo ln -s /usr/local/lib/python3.8/dist-packages/mraa.py /usr/local/lib/python3.9/dist-packages/mraa.py
sudo ln -s /usr/local/lib/python3.8/dist-packages/_mraa.so /usr/local/lib/python3.9/dist-packages/_mraa.so
```
