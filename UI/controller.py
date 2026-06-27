import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._squadre_map = {}


    def handleAnni(self):
        for anno in self._model.get_Anni():
            self._view._ddAnno.options.append(ft.dropdown.Option(str(anno)))

    def handleTeams(self,e):
        self._view._ddSquadra.options.clear()
        anno = self._view._ddAnno.value
        if anno is None:
            self._view._txtOutSquadre.controls.append(ft.Text(f"Errore! scegli l'anno", color = "red"))
            self._view.update_page()
            return
        teams = self._model.get_Team(anno)
        self._view._txtOutSquadre.controls.clear()
        self._view._txtOutSquadre.controls.append(ft.Text(f"N. squadre: {len(teams)}"))
        self._squadre_map.clear()
        for team in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(f"id: {team.ID}\n"))
            self._view._ddSquadra.options.append(ft.dropdown.Option(key=team.name, text=str(team.name)))
            self._squadre_map[team.name] = team
        self._view.update_page()

    def handleCreaGrafo(self, e):
        anno = self._view._ddAnno.value
        if anno is None:
            self._view._txtOutSquadre.controls.append(ft.Text(f"Errore! un anno maggiore di 1980", color="red"))
            self._view.update_page()
            return
        if int(anno) < 1980:
            self._view._txtOutSquadre.controls.append(ft.Text(f"Errore! un anno maggiore di 1980", color="red"))
            self._view.update_page()
            return
        self._model.buildGraph(anno)

        # Pulisci i vecchi risultati
        self._view._txt_result.controls.clear()

        # Ottieni numero nodi e archi per mostrarli a schermo
        nodi = len(self._model._graph.nodes)
        archi = len(self._model._graph.edges)

        # Aggiungi il testo alla casella _txt_result invece di _txtOutSquadre
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato correttamente!"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di nodi: {nodi}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di archi: {archi}"))

        self._view.update_page()
    def handleDettagli(self, e):
        nome_squadra = self._view._ddSquadra.value
        if nome_squadra is None:
            self._view._txt_result.controls.append(ft.Text("Errore! Seleziona una squadra.", color="red"))
            self._view.update_page()
            return
            
        squadra_selezionata = self._squadre_map.get(nome_squadra)
        if not squadra_selezionata:
            return
            
        dettagli = self._model.getDettagli(squadra_selezionata)
        
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Squadre adiacenti a {squadra_selezionata.name}:", weight=ft.FontWeight.BOLD))
        
        if not dettagli:
            self._view._txt_result.controls.append(ft.Text("Nessuna squadra adiacente presente."))
        else:
            for vicino, peso in dettagli:
                self._view._txt_result.controls.append(ft.Text(f"{vicino.name} - Peso arco: {peso}"))
            
        self._view.update_page()

    def handlePercorso(self, e):
        pass