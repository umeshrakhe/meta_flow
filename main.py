#from adapters.file_readers.csv_reader import CSVReader
#from adapters.file_writers.csv_writer import CSVWriter
#from adapters.logger import logger
#from application.use_cases.process_file_use_case import ProcessFileUseCase
#from domain.services.data_transformer import DataTransformer
#from domain.services.data_validator import DataValidator
#from domain.services.stats_calculator import StatsCollector
#from infrastructure.config.config_service import DatabaseConfigService
from infrastructure.metadata_repository import OracleDbConnection
from infrastructure.utils.helper_functions import get_arguments 

def main():
    Session =OracleDbConnection(get_arguments()) 
    """db_connection = # ... establish database connection
    config_service = DatabaseConfigService(db_connection) 
    csv_reader = CSVReader()
    data_transformer = DataTransformer(config_service)
    data_validator = DataValidator(config_service)
    csv_writer = CSVWriter()
    use_case = ProcessFileUseCase(config_service, 
                                 csv_reader, 
                                 data_transformer, 
                                 data_validator, 
                                 StatsCollector, 
                                 logger, 
                                 csv_writer)
    use_case.execute("SRC_FILE_1") """
    print(Session)
if __name__ == "__main__":
    main()