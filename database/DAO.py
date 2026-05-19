from database.DB_connect import DBConnect
from model.confine import Confine
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """SELECT *
                    FROM country"""
        cursor.execute(query)

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(annoMin, idMap):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """select c.state1no as stato1, c.state2no as stato2
                   from contiguity c
                   where c.year <= %s \
                     and c.conttype = 1"""
        cursor.execute(query, (annoMin,))

        for row in cursor:
            result.append(idMap[row["stato1"]])
            result.append(idMap[row["stato2"]])  # ← aggiunto

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConfini(annoMin, idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """select c.state1no as stato1, c.state2no as stato2, c.year as anno
                   from contiguity c
                   where c.year <= %s \
                     and c.conttype = 1"""
        cursor.execute(query, (annoMin,))

        for row in cursor:
            result.append(Confine(idMap[row["stato1"]], idMap[row["stato2"]], row["anno"]))

        cursor.close()
        conn.close()
        return result  # Ritorno una lista di confini
