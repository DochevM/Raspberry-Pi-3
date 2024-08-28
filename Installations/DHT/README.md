## Needed installations for DHT22:
### Setting up the Raspberry Pi for DHT
Lets update all packages of the raspberry:
```
sudo apt update
```
```
sudo apt upgrade
```
Lets install "python3-dev" and "python3-pip" if there are not installed already:
```
sudo apt install python3-dev python3-pip
```
### Setting up a Python Virtual Environment for the DHT22 Humidity Sensor
Making a directory called "dht22"

```
mkdir ~/dht22
```
Navigating to the new directory:

```
cd ~/dht22
```
Creating the enviroment:
```
python3 -m venv env
```
Lets utilize it as its source:
```
source env/bin/activate
```
Now lets intall the lirary for our dht:
```
python3 -m pip install adafruit-circuitpython-dht
```

Making the file file, where the code will be placed:
```
nano ~/dht22/DHT22.py
```

### The code can be found in [my projects folder](https://github.com/DochevM/Raspberry_Pi_3/tree/main/Software/DHT22-Digital%20thermometer%20and%20humidity%20meter)

