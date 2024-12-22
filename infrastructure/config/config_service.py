from abc import ABC, abstractmethod

class ConfigService(ABC):
    @abstractmethod
    def get_validation_rules(self) -> dict:
        """Fetches validation rules from the configuration source."""
        pass

    @abstractmethod
    def get_transformation_rules(self) -> dict:
        """Fetches transformation rules from the configuration source."""
        pass

    def get_file_metadata(self, file_key: str) -> dict:
        """
        Fetches file/database metadata based on the provided key.

        Args:
            file_key: The key identifying the file/database metadata.

        Returns:
            A dictionary containing the metadata (input_file_path, output_file_path, 
            validation_rules, transformation_rules, etc.).
        """
        # ... implementation to fetch metadata based on file_key ...

class DatabaseConfigService(ConfigService):
    def __init__(self, db_connection): 
        self.db_connection = db_connection 

    def get_validation_rules(self) -> dict:
        # Logic to fetch validation rules from the database
        pass

    def get_transformation_rules(self) -> dict:
        # Logic to fetch transformation rules from the database
        pass

class FileConfigService(ConfigService):
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path 

    def get_validation_rules(self) -> dict:
        # Logic to read validation rules from the configuration file
        pass

    def get_transformation_rules(self) -> dict:
        # Logic to read transformation rules from the configuration file
        pass