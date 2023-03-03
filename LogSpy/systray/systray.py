import pystray
import PIL.Image

def app():
    image = PIL.Image.open("LogSpy\systray\icon.png")
    str_status_service = "Service stopped"
    str_status_bd = "Service stopped"

    def on_clicked(icon, item):
        if str(item) == "Exit":
            icon.stop()

    def status_service(icon, item):
        # If service is running, change "Service stopped" to "Service running"
        pass
    
    def status_basedata(icon, item):
        pass

    icon = pystray.Icon("LogSpy", image, menu=pystray.Menu(
        pystray.MenuItem(str_status_service, status_service),
        pystray.MenuItem(str_status_bd, status_basedata),
        pystray.MenuItem("Exit", on_clicked)
        ))

    icon.run()