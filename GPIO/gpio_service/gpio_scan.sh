# SCANING GPIO USING RAM FILES
#!/bin/bash

touch /mnt/ramdisk/gpio4
echo 0 > /mnt/ramdisk/gpio4

while true
do
	LINE=4
	gpioset gpiochip0 $LINE=$(cat /mnt/ramdisk/gpio$LINE)
	sleep 0.9
done
