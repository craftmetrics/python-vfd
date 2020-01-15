from . import VFD
from umodbus.client.serial import rtu
import serial
import serial.rs485


DEVICE_ADDRESS = 1

# Read/write
#########################

REG_PO1_CONTROL_WORD = 0
# 0x0006 = Start
# 0x0002 = Stop with deceleration (P-03)
# 0x0001 = Stop with coast
# 0x0000 = Stop with alternate deceleration (P-24)

REG_PO2_SETPOINT_SPEED = 1  # 0 – 16384
# 0x4000 = full speed
# 0x2000 = half speed
# 0xC000 = full speed reverse
# 0xDFFF = half speed reverse

REG_PO3_RAMP_TIME = 2      # 100 ms – 65535 ms

# Read-only
#########################
REG_PI1_STATUS_WORD = 5
REG_PI2_ACTUAL_SPEED = 6
REG_PI3_ACTUAL_CURRENT = 7
REG_PI4_MOTOR_TORQUE = 8


class MovitracLTEB(VFD):

    def connect(self, port):
        self.serial = serial.rs485.RS485(
            port=port,
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=1,
            bytesize=8,
            timeout=1,
        )

    def is_running(self):
        message = rtu.read_holding_registers(
            DEVICE_ADDRESS, REG_PI1_STATUS_WORD, 1)
        (response,) = rtu.send_message(message, self.serial)
        return bool(response & 0b0000010000000000)

    def get_frequency(self):
        message = rtu.read_holding_registers(
            DEVICE_ADDRESS, REG_PI2_ACTUAL_SPEED, 1)
        (response,) = rtu.send_message(message, self.serial)
        return response

    def start(self, speed):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()
