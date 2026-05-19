import networkx as nx

from database.DAO import DAO
from model import country


class Model:

    def __init__(self):

        self._graph = nx.Graph()
        self._countries = DAO.getAllCountries() # Lista paesi
        self._idMapCountries = {}

        for c in self._countries:
            self._idMapCountries[c.CCode] = c

    def buildGraph(self, annoMin):
        self._graph.clear()

        allConfini = DAO.getAllConfini(annoMin, self._idMapCountries)

        # Usa getAllNodes che restituisce solo i paesi che compaiono nei confini
        nodi = DAO.getAllNodes(annoMin, self._idMapCountries)
        self._graph.add_nodes_from(nodi)

        for c in allConfini:
            self._graph.add_edge(c.stato1, c.stato2)

    def addEdges(self, annoMin):

        allConfini = DAO.getAllConfini(annoMin, self._idMapCountries) # lista di oggetti di tipo confine

        # Ho due problemi:
        # 1) archi diretti e inversi
        # 2) archi fra confini già filtrati

        for c in allConfini:
            if c.stato1 in self._graph and c.stato2 in self._graph:
                # Allora posso aggiungerlo, salto in conteggio pesi di altri es perche non ci sono
                self._graph.add_edge(c.stato1, c.stato2)


    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def get_stati_confinanti(self):
        """Restituisce una lista di tuple (Stato, numero_vicini)"""
        risultato = []
        for nodo in self._graph.nodes:
            # Il grado del nodo corrisponde al numero di archi incidenti (stati confinanti)
            grado = self._graph.degree(nodo)
            # Puoi usare una proprietà del tuo oggetto Country per il nome, es: nodo.StateName o simile
            risultato.append((nodo, grado))
        return risultato

    def get_numero_componenti_connesse(self):
        """Restituisce il numero di componenti connesse del grafo"""
        return nx.number_connected_components(self._graph)








