from abc import ABC, abstractmethod


class VFD(ABC):

    @abstractmethod
    def connect(self, port):
        pass

    @abstractmethod
    def is_running(self):
        pass

    @abstractmethod
    def get_frequency(self):
        pass

    @abstractmethod
    def start(self, speed):
        pass

    @abstractmethod
    def stop(self):
        pass

    def close(self):
        self.serial.close()
