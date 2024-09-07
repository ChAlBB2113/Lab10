import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._nodi=[]
        self._archi=[]
        self._grafo= nx.Graph()

    def creaGrafo(self, year):
        self._nodi.clear()
        self._archi.clear()
        self._grafo.clear()

        nomi=DAO.nomi()

        self._listaNodi=DAO.ottieniNodi(year)
        self._listaArchi=DAO.ottieniArchi(year)
        listaArchiNomi=[]

        for arco in self._listaArchi:
            listaArchiNomi.append((nomi[arco[0]], nomi[arco[1]]))

        self._grafo.add_edges_from(listaArchiNomi)
        lista=[]
        for i in self._listaNodi:
            print (nomi[i])
            lista.append(nomi[i])

        print(len(lista))

        self._grafo.add_nodes_from(lista)



