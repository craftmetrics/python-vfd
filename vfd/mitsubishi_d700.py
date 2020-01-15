from . import VFD
from umodbus.client.serial import rtu
import serial
import serial.rs485


DEVICE_ADDRESS = 1

# Read/write
#########################

# Page 202:
# Starting address = Starting register address (decimal)-40001
# For example, setting of the starting address 0001 reads the
# data of the holding register 40002.
REG_START = 40001

# Inverter status/control input instruction (page 207)
REG_STATUS_CONTROL = 40009 - REG_START

# Other status registers (page 207)
REG_OUTPUT_FREQ = 40201 - REG_START
REG_OUTPUT_CURRENT = 40202 - REG_START
REG_MOTOR_LOAD = 40224 - REG_START


class MitsubishiD700(VFD):

    def connect(self, port):
        self.serial = serial.rs485.RS485(
            port=port,
            baudrate=9600,
            parity=serial.PARITY_EVEN,
            stopbits=1,
            bytesize=8,
            timeout=1,
        )

    def is_running(self):
        message = rtu.read_holding_registers(
            DEVICE_ADDRESS, REG_STATUS_CONTROL, 1)
        (response,) = rtu.send_message(message, self.serial)
        return bool(response & 0x1)

    def get_frequency(self):
        message = rtu.read_holding_registers(
            DEVICE_ADDRESS, REG_OUTPUT_FREQ, 1)
        (response,) = rtu.send_message(message, self.serial)
        return response * 0.01  # Hz

    def start(self, speed):
        message = rtu.write_single_register(
            DEVICE_ADDRESS, REG_STATUS_CONTROL, 0b10)
        response = rtu.send_message(message, self.serial)
        return response

    def stop(self):
        message = rtu.write_single_register(
            DEVICE_ADDRESS, REG_STATUS_CONTROL, 0b1)
        response = rtu.send_message(message, self.serial)
        return response
