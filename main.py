from db.connect import DBConnection

def main():
    db = DBConnection("./db/forex.db")
    db.createTable('USDJPY', '1H')

if __name__ == "__main__":
    main()