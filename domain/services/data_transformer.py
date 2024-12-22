class DataTransformer:
    def __init__(self, config_service: ConfigService):
        self.config_service = config_service
        self.transformation_rules = self.config_service.get_transformation_rules() 

    def transform(self, data: list[dict]) -> list[dict]:
        # ... implementation for data transformation 
        # using the fetched transformation_rules 
        pass