# WRITING GPIO4 PIN

from time import sleep

# Write to a new file or overwrite an existing one
with open("/mnt/ramdisk/gpio4", "w") as file:
    file.write("1")
sleep(5)
with open("/mnt/ramdisk/gpio4", "w") as file:
    file.write("0")
