from abc import abstractmethod


class FileAdapter:
    @abstractmethod
    def parse(self, file_path: str) -> list:
        """
        Abstract method to parse the file and return structured data.
        :param file_path: Path to the file to parse
        :return: List of parsed data
        """
        pass

class CSVAdapter(FileAdapter):
    def parse(self, file_path: str) -> list:
        # Implementation for parsing CSV files
        pass

class JSONAdapter(FileAdapter):
    def parse(self, file_path: str) -> list:
        # Implementation for parsing JSON files
        pass

# Other adapters (XML, Excel) can follow a similar structure
