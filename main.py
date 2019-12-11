from data.db.connect import DBConnection

def main():
    db = DBConnection("./data/db/forex.db")
    print(db.listTables())

if __name__ == "__main__":
    main()