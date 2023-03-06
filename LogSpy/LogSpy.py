from systray.systray import app
import threading
import configparser


settings = configparser.ConfigParser()
settings.read('settings\config.ini')

def main():
    hilo = threading.Thread(target=app)
    hilo.start()


if __name__ == "__main__":
    main()
