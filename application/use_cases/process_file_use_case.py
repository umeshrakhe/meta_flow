from adapters.file_readers.csv_reader import CSVReader
from adapters.file_writers.csv_writer import CSVWriter
from adapters.logger.logger import Logger
from domain.services.data_transformer import DataTransformer
from domain.services.data_validator import DataValidator
from domain.services.stats_calculator import StatsCollector
from infrastructure.config.config_service import ConfigService


class ProcessFileUseCase:
    def __init__(self, config_service: ConfigService, 
                 csv_reader: CSVReader, 
                 data_transformer: DataTransformer, 
                 data_validator: DataValidator, 
                 stats_collector: StatsCollector, 
                 logger: Logger, 
                 csv_writer: CSVWriter):
        self.config_service = config_service
        self.csv_reader = csv_reader
        self.data_transformer = data_transformer
        self.data_validator = data_validator
        self.stats_collector = stats_collector
        self.logger = logger
        self.csv_writer = csv_writer

    def execute(self, file_key: str) -> None:
        file_metadata = self.config_service.get_file_metadata(file_key) 
        input_file_path = file_metadata['input_file_path']
        output_file_path = file_metadata['output_file_path']
        # ... 
        # Configure data_transformer and data_validator 
        # using rules from file_metadata 
        # ...

        try:
            data = self.csv_reader.read(input_file_path)
            if self.data_validator.validate(data):
                transformed_data = self.data_transformer.transform(data)
                stats = self.stats_collector.collect_stats(data)
                self.logger.log(f"Processed {len(data)} rows. Statistics: {stats}")
                self.csv_writer.write(transformed_data, output_file_path)
            else:
                self.logger.log("Data validation failed.", level='ERROR')
        except Exception as e:
            self.logger.log(f"An error occurred: {str(e)}", level='ERROR')