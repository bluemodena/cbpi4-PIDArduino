# cbpi4-PIDArduino

PIDArduino Logic for craftbeerpi4

Note: This code borrowed heavily from the cbpi3 PIDArduino plugin and the cbpi4-PIDBoil plugin by avollkopf

Once the target temperature is reached, it will maintain that target temp indefinitely.

Installation:
you can install (or clone) it from the GIT Repo. 

sudo pip3 install cbpi4-PIDArduino
Afterwards you will need to activate the plugin:

sudo cbpi add cbpi4-PIDArduino

Parameters

PIDArduino Settings

P - proportional value
I - integral value
D - derivative value
SampleTime - 2 or 5 seconds -> how often the logic calculates the power setting
max output - heater power which is set above boil threshold


21.12.30: (0.0.9) Initial commit
