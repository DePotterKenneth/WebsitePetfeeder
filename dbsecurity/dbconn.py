
class DbConnection:
    def __init__(self, database):
        self.__dsn = {
            "host": "localhost",
            "user": "petfeeder_sql",
            "passwd": "Tinfoil",
            "db": database,
        }
        from mysql import connector
        self.__connection = connector.connect(**self.__dsn)


    # voor lezen (SELECT)
    # met query(..., return_dict=True) krijg je een dictionary terug,
    # dat vermindert de kans op fouten (zeker bij SELECT * FROM..)
    def query(self, query: str, data: dict = None, dictionary=False):
        cursor = self.__connection.cursor(dictionary=dictionary)
        cursor.execute(query, data)
        result = cursor.fetchall()
        cursor.close()
        return result

    # voor schrijven (INSERT, UPDATE, ...)
    def execute(self, query: str, data: dict = None):
        cursor = self.__connection.cursor()
        cursor.execute(query, data)
        result = cursor.lastrowid
        self.__connection.commit()
        cursor.close()
        return result


