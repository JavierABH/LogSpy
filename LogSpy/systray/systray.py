import pystray
import PIL.Image

def app():
    image = PIL.Image.open("LogSpy\systray\icon.png")
   
    def on_clicked(icon, item):
        if str(item) == "Exit":
            icon.stop()
        elif str(item) == "Log Path":
            pass

    def status_service(icon, item):
        pass
    
    def status_basedata(icon, item):
        pass

    icon = pystray.Icon("LogSpy", image, menu=pystray.Menu(
        pystray.MenuItem("Service running", status_service),
        pystray.MenuItem("Basedata running", status_basedata),
        pystray.MenuItem("Settings", pystray.Menu(
        pystray.MenuItem("Log Path", on_clicked),
        )),
        pystray.MenuItem("Exit", on_clicked)
        ))

    icon.run()

