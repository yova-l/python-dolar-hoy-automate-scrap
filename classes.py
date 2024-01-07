import constants

class MoneyExchange:
    def __init__(self):
        self.dolars = {key: [None, None] for key in constants.DH_DOLLARS }
        
    def get_value(self, dol_type, operation):
        return (self.dolars[dol_type])[operation]
    
    def set_value(self, dol_type, operation, value):
        (self.dolars[dol_type])[operation] = value
