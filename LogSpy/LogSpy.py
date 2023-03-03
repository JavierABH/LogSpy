from systray.systray import app
import threading

def main():
    hilo = threading.Thread(target=app)
    hilo.start()

if __name__ == "__main__":
    main()
