class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol            
        self.__company_name = company_name  

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def get_stock_list():
    stock1 = Stock("AAPL", "Apple Inc")
    stock2 = Stock("CAT", "Caterpillar")
    stock3 = Stock("EK", "Eastman Kodak")
    stock4 = Stock("GOOG", "Google")
    stock5 = Stock("MSFT", "Microsoft")

    stock_list = [stock1, stock2, stock3, stock4, stock5]

    return stock_list

def create_stock_file():
    stock_data = [
        ("AAPL", "Apple Inc"),
        ("CAT", "Caterpillar"),
        ("EK", "Eastman Kodak"),
        ("GOOG", "Google"),
        ("MSFT", "Microsoft")
    ]
    
    with open("stock_file.dat", "w") as file:
        for symbol, company_name in stock_data:
            file.write(f"{symbol} {company_name}\n")
    print("Stock data has been written to stock_file.dat.")