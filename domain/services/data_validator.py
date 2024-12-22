class DataValidator:
    def __init__(self, config_service: ConfigService):
        self.config_service = config_service
        self.validation_rules = self.config_service.get_validation_rules()

    def validate(self, data: list[dict]) -> bool:
        # ... implementation for data validation 
        # using the fetched validation_rules 
        pass