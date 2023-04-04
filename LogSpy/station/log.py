import logging
import re
from datetime import datetime
from typing import List
import configparser

config = configparser.ConfigParser()
config.read('config\config.ini')
test_name_path = config["Paths"]["TestName"]
filename_pattern = config["Paths"]["TestName"]

partnumbers_map = {
    "47257764-E": "22-47257764+E",
    "47257764-C": "47257764+C"
}

class Log:
    """
    Representa un log generado por una estacion de prueba
    """

    def __init__(self, path: str) -> None:
        """
        Inicializa una instancia de la clase Log.

        Args:
            path (str): Ruta al archivo de registro.

        Raises:
            FileNotFoundError: Si el archivo de registro no existe en la ruta especificada.
        """
        self.path = path
        self.filename = path.split('\\')[-1]
        self.lines_iter = self._generate_lines()
        self.serial = None
        self.datetime = None
        self.partnumber = None
        if self.is_valid():
            self._set_path_data()

    def is_valid(self) -> bool:
        """
        Verifica si el nombre de archivo cumple con el patrón de nomenclatura esperado.

        Returns:
            bool: True si el nombre de archivo es válido, False de lo contrario.
        """
        if re.match(self.filename_pattern, self.filename):
            return True
        else:
            logging.warning(f"Nombre de archivo inválido: {self.filename}")
            return False

    def inserted(self) -> bool:
        """
        Verifica en el log si la prueba se subió a trazabilidad.

        Returns:
            bool: True si el proceso de inserción ha finalizado correctamente, False de lo contrario.
        """
        iter_lines = self._generate_lines(reversed=True)
        for idx, line in enumerate(iter_lines):
            if "InsertProcess:" in line:
                if re.split(" {2,}", line.lstrip())[-1] in ["Passed", "Done"]:
                    return True
            if idx > 10:
                break
        return False

    def _set_path_data(self) -> None:
        """
        Establece los atributos serial, datetime y partnumber de la instancia de la clase Log.
        """
        try:
            self.serial, date, time = tuple(re.findall(r'\[(.*?)\]', self.path))
            self.datetime = datetime.strptime(" ".join([date, time]), "%m %d %Y %I %M %S %p")
            self.partnumber = partnumbers_map[self.serial[2:12]]
        except Exception as e:
            logging.error(f"Error al establecer los datos del archivo {self.filename}: {e}")
            raise

    def _generate_lines(self, reversed=False) -> List[str]:
        """
        Genera un iterador para las líneas del archivo de registro.

        Args:
            reversed (bool, optional): Si se establece en True, el iterador se generará en orden inverso.
                Por defecto es False.

        Yields:
            str: Cada línea del archivo de registro.
        """
        with open(self.path) as log:
            lines = log.readlines()
            if reversed:
                lines.reverse()
            for line in lines:
                yield line.rstrip()

    def get_log_lines(self) -> List[str]:
        """
        Devuelve todas las líneas del archivo de registro como una lista.

        Returns:
            List[str]: Lista de cadenas que representan cada línea del archivo de registro.
        """
        with open(self.path) as f:
            return [line.rstrip() for line in f]

    def get_raw(self) -> str:
        """
        Devuelve el contenido completo del archivo de registro como una cadena.

        Returns:
            str: Contenido completo del archivo de registro como una cadena.
        """
        with open(self.path) as f:
            return f.read()

def get_testnames() -> List[str]:
    """
    Devuelve una lista de los nombres de prueba registrados en el archivo 'log_testnames.txt'.

    Returns:
        List[str]: Lista de cadenas que representan cada nombre de prueba registrado en el archivo.
    """
    with open(test_name_path) as f:
        return [line.rstrip() for line in f]
