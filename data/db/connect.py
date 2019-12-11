import sqlite3

class DBConnection:
    def __init__(self, locationOfDb):
        self.connection = sqlite3.connect(locationOfDb)
    
    def selectInstrumentData(self, name, source, timeframe):
        """
        Description:
            Selects all data for a given instrument in order
        Params: 
            1. name: Name of instrument to query (ex. USDEUR)
            2. source: Source of the Data (ex. Dukescopy)
            3. timeframe: time frame of data (tick, 1M, 1H, etc..)
        """
        return 

    def insertInstrumentData(self, name, source, timeframe, listOfInsertableData):
        return 

    def listTables(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('SELECT name from sqlite_master where type= "table"')
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            cursor.close()
