from database.DB_connect import DBConnect
from model.country import Country

class DAO():
    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        # Usiamo i nomi esatti dal tuo screenshot 2
        query = "SELECT StateAbb, CCode, StateNme FROM country"
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(Country(**row))
        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getEdges(annoUtente):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        # Tabella contiguity (screenshot 1)
        # Prendiamo solo gli archi dove state1no < state2no per non duplicarli nel grafo
        query = """SELECT state1no, state2no
                   FROM contiguity
                   WHERE year <= %s 
                   AND conttype = 1 
                   AND state1no < state2no"""
        cursor.execute(query, (annoUtente,))
        res = []
        for row in cursor:
            res.append((row['state1no'], row['state2no']))
        cursor.close()
        conn.close()
        return res
