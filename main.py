from db.connect import DBConnection

def main():
    db = DBConnection("./db/forex.db")
    db.insertInstrumentData('USDJPY', 'Dukascopy','1H', 'ASK', './csv/USDJPY/1H/USDJPY_Candlestick_1_Hour_ASK_31.12.2004-06.12.2019.csv')
    db.insertInstrumentData('USDJPY', 'Dukascopy','1H', 'BID', './csv/USDJPY/1H/USDJPY_Candlestick_1_Hour_BID_31.12.2004-06.12.2019.csv')
    

if __name__ == "__main__":
    main()