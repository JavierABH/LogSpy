from abc import ABC, abstractmethod

class LogInterface(ABC):
    @abstractmethod
    def get_station(self):
        pass

    @abstractmethod
    def get_serial(self):
        pass

    @abstractmethod
    def get_partnumber(self):
        pass

    @abstractmethod
    def get_date(self):
        pass
    
    @abstractmethod
    def get_datetime(self):
        pass
    
    @abstractmethod
    def get_cycletime(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def get_fail(self):
        pass

    @abstractmethod
    def get_measurement(self):
        pass