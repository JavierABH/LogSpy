
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket

class PythonService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'XblGameSave'
    _svc_display_name_ = 'Xbox Live Game Save'
    _svc_description_ = 'This service syncs save data for Xbox Live save enabled games.  If this service is stopped, game save data will not upload to or download from Xbox Live.'

    @classmethod
    def parse_command_line(cls):
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def start(self):
        self.isrunning = True

    def stop(self):
       self.isrunning = False

    def main(self):
        pass


if __name__ == '__main__':
    myservice = PythonService()
    myservice.start()