import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        anno_str = self._view._txtAnno.value

        try:
            anno = int(anno_str)
        except ValueError:
            self._view.create_alert("Errore: Inserisci un anno numerico.")
            return

        if not (1816 <= anno <= 2016):
            self._view.create_alert("L'anno deve essere tra 1816 e 2016.")
            return

        # Logica
        self._model.buildGraph(anno)
        n_nodi, n_archi = self._model.get_details()

        # Pulizia e Stampa
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato.", color="green", weight="bold"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di vertici: {n_nodi}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di archi: {n_archi}"))

        # Punto (c): Elenco stati e grado
        self._view._txt_result.controls.append(ft.Text("\nElenco degli stati e numero di confini:", weight="bold"))
        lista_gradi = self._model.get_sgradi_nodi()
        for paese, grado in lista_gradi:
            self._view._txt_result.controls.append(ft.Text(f"{paese.StateNme}: {grado} confini"))

        self._view.update_page()





