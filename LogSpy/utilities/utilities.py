import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import configparser

class LogFileHandler(FileSystemEventHandler):
    def __init__(self, on_created_callback):
        """
        Inicializa un objeto LogFileHandler.

        Args:
            on_created_callback (callable): Función de devolución de llamada que se ejecutará cuando se cree un archivo.
        """
        super().__init__()
        self.on_created_callback = on_created_callback

    def on_created(self, event):
        """
        Método que se ejecuta cuando se crea un archivo en el directorio observado.

        Args:
            event (watchdog.events.FileSystemEvent): Evento que representa la creación del archivo.
        """
        if event.is_directory:
            return
        self.on_created_callback(event.src_path)

def watch_directory(directory_path: str, on_created_callback: callable) -> None:
    """
    Observa el directorio especificado en busca de nuevos archivos y ejecuta una función de devolución de llamada
    cuando se crea un nuevo archivo.

    Args:
        directory_path (str): Ruta del directorio a observar.
        on_created_callback (callable): Función de devolución de llamada que se ejecutará cuando se cree un archivo.
    """
    event_handler = LogFileHandler(on_created_callback)
    observer = Observer()
    observer.schedule(event_handler, directory_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def configure_directory() -> str:
    """
    Lee la ruta del directorio a observar desde el archivo de configuración y devuelve su valor como una cadena.

    Returns:
        str: Ruta del directorio a observar.
    """
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    return config['Paths']['WatchedDirectory']
