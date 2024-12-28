from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message: str, level: str = 'INFO') -> None:
        """Logs a message with the specified log level."""
        pass

class FileLogger(Logger):
    def __init__(self, log_file_path: str):
        self.log_file_path = log_file_path

    def log(self, message: str, level: str = 'INFO') -> None:
        # ... implementation for logging to a file ...


class DatabaseLogger(Logger):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def log(self, message: str, level: str = 'INFO') -> None:
        # ... implementation for logging to a database ...