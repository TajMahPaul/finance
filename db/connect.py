import sqlite3
import csv

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

    def insertInstrumentData(self, name, source, timeframe, typeOfValue, locationOfData):
        listOfDataPoints = self.csvToList(locationOfData)
        newList = []
        cursor = self.connection.cursor()
        self.createTable(name, timeframe)
        try:
            for row in listOfDataPoints:
                newTuple = (row[0], source, typeOfValue, row[1], row[2], row[3], row[4], row[5])
                newList.append(newTuple)

            cursor.executemany("""INSERT INTO "{0}_{1}" values (?,?,?,?,?,?,?,?)""".format(timeframe, name), newList)
            self.connection.commit()
        except Exception as e:
            print(str(e))
        finally:
            cursor.close()

    def listTables(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('SELECT name from sqlite_master where type= "table"')
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            cursor.close()
    
    def createTable(self, name, timeframe):
        cursor = self.connection.cursor()
        try:
            strSQL = """CREATE TABLE IF NOT EXISTS "{0}_{1}" (
                        local_time text NOT NULL,
                        source text NOT NULL,
                        type test NOT NULL,
                        open real NOT NULL,
                        high real NOT NULL,
                        low real NOT NULL,
                        close real NOT NULL,
                        volume real NOT NULL,
                        PRIMARY KEY (local_time, source, type))""".format(timeframe, name)
            cursor.execute(strSQL)
        except Exception as e:
            print(str(e))
        finally:
            cursor.close()

    def csvToList(self, locationOfCSV):
        try:
            with open(locationOfCSV, 'r') as f:
                reader = csv.reader(f)
                your_list = list(reader)
            return your_list
        except Exception as e:
            print(str(e))