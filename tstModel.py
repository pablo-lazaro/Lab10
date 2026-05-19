from model.model import Model

myModel = Model()
myModel.buildGraph(1945)
node, edges = myModel.getGraphDetails()
print(f"nodi: {node}, edges: {edges}")


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