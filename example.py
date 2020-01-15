from vfd.mitsubishi_d700 import MitsubishiD700
import time


my_vfd = MitsubishiD700()
# Open the serial port

my_vfd.connect("/dev/tty.usbserial-12345678")

print("Starting Motor")
my_vfd.start(None)

for _ in range(10):
    print("Running: {}".format(my_vfd.is_running()))
    print("Frequency: {}".format(my_vfd.get_frequency()))
    print()
    time.sleep(1)

print("Stopping Motor")
my_vfd.stop()

for _ in range(10):
    print("Running: {}".format(my_vfd.is_running()))
    print("Frequency: {}".format(my_vfd.get_frequency()))
    print()
    time.sleep(1)

# Close the serial port
my_vfd.close()
