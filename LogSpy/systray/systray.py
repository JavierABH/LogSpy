import pystray
import PIL.Image

import win32serviceutil
import win32service

# def check_service_status(service_name):
#     try:
#         # Obtiene el estado del servicio
#         service_status = win32serviceutil.QueryServiceStatus(service_name)[1]
#         if service_status == win32service.SERVICE_RUNNING:
#             return "Service running"
#         else:
#             return "Service stopped"
#     except win32serviceutil.error as e:
#         # En caso de error, devolver el estado del servicio como "Desconocido"
#         print(f"Error al obtener el estado del servicio: {e}")
#         return "Unknown"

def app():
    image = PIL.Image.open("LogSpy\systray\icon.png")
   
    def on_clicked(icon, item):
        if str(item) == "Exit":
            icon.stop()

    def status_service(icon, item):
        # If service is running, change "Service stopped" to "Service running"
        
    
    def status_basedata(icon, item):
        pass

    icon = pystray.Icon("LogSpy", image, menu=pystray.Menu(
        pystray.MenuItem("Service stopped", status_service),
        pystray.MenuItem("Basedata running", status_basedata),
        pystray.MenuItem("Exit", on_clicked)
        ))

    icon.run()

