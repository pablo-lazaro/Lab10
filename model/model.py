import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        # Carichiamo tutti i paesi una volta sola per velocizzare
        all_countries = DAO.getAllCountries()

        # Inizializziamo la mappa vuota
        self._idMap = {}

        # Popoliamo la mappa con un ciclo for classico
        for c in all_countries:
            codice = c.CCode
            self._idMap[codice] = c

    def buildGraph(self, anno):
        self._graph.clear()
        edges = DAO.getEdges(anno)

        for s1, s2 in edges:
            self._graph.add_edge(self._idMap[s1], self._idMap[s2])

    def get_details(self):
        # Restituisce i dati generali richiesti
        nodes_count = len(self._graph.nodes)
        edges_count = len(self._graph.edges)

        return nodes_count, edges_count

    def get_sgradi_nodi(self):
        risultato = []
        for n in self._graph.nodes:
            # Recuperiamo la lista dei vicini del nodo n
            vicini = list(self._graph.neighbors(n))
            # Il grado è la lunghezza di questa lista
            grado = len(vicini)
            risultato.append((n, grado))
        return risultato