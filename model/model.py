import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._DAO= DAO
        self._graph = nx.Graph()

    def get_Anni(self):
        return self._DAO.getAnni()
    def get_Team(self,anno1):
        anno = int(anno1)
        return self._DAO.getTeams(anno)
    def buildGraph(self,anno1):
        self._graph.clear()
        anno = int(anno1)
        idMap = {t.ID: t for t in self._DAO.getTeams(anno)}
        for team in self._DAO.getTeams(anno):
            self._graph.add_node(team)
        edges = self._DAO.getEdges(anno)
        for team1_ID, peso1 in edges:
            for team2_ID,peso2 in edges:
                if team1_ID<team2_ID:
                    team1 = idMap.get(team1_ID)
                    team2 = idMap.get(team2_ID)
                    peso = peso1+peso2
                    self._graph.add_edge(team1,team2,weight=peso)

    def getDettagli(self, squadra):
        if squadra not in self._graph.nodes:
            return []
            
        vicini = self._graph.neighbors(squadra)
        dettagli = []
        
        for vicino in vicini:
            peso = self._graph[squadra][vicino]['weight']
            dettagli.append((vicino, peso))
            
        dettagli.sort(key=lambda x: x[1], reverse=True)
        
        return dettagli

