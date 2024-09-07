import flet as ft
import networkx as fx

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):


        #prendo input, controllo non sia vuoto, controllo sia numerico
        #e in particolare un anno tra tot e tot;
        input= self._view._txtAnno.value
        if input=="" or input==None or input=="Anno":
            self._view._txt_result.clean()
            self._view._txt_result.controls.append(ft.Text(f"inserisci un anno"))
            self._view.update_page()
            return
        try:
            year=int(input)
        except ValueError:
            self._view._txt_result.clean()
            self._view._txt_result.controls.append(ft.Text(f"inserisci un valore numerico"))
            self._view.update_page()
            return
        if year<1816 or year>2016:
            self._view._txt_result.clean()
            self._view._txt_result.controls.append(ft.Text(f"inserisci un anno tra 1816 e 2016"))
            self._view.update_page()
            return

        self._model.creaGrafo(year)
        self._view._txt_result.clean()
        self._view._txt_result.controls.append(ft.Text(f"Numero nodi: {len(self._model._grafo.nodes())}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero nodi: {len(self._model._grafo.edges())}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero componenti connesse: {fx.number_connected_components(self._model._grafo)}"))

        for nodo in self._model._grafo.nodes():
            self._view._txt_result.controls.append(ft.Text(f"{nodo} -- {len(list(self._model._grafo.neighbors(nodo)))} vicini"))

        self._view.update_page()

