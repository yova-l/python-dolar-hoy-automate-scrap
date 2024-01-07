import constants

# class _Dolar:
#     def __init__(self):
#         self.buy = None
#         self.sell = None
#     def get_buy(self):
#         return self.buy
#     def get_sell(self):
#         return self.sell
#     def set_buy(self, buy_price):
#         self.buy = buy_price
#     def set_sell(self, sell_price):
#         self.sell = sell_price

class MoneyExchange:
    def __init__(self):
        self.dolars = {key: [None, None] for key in constants.DH_DOLLARS }
        
    def get_value(self, dol_type, operation):
        return (self.dolars[dol_type])[operation]
    
    def set_value(self, dol_type, operation, value):
        (self.dolars[dol_type])[operation] = value
