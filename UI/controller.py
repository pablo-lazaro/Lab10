import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):

        valoreAnnoUtente = self._view._txtAnno.value

        # Verifico che la stringa non sia vuota
        if valoreAnnoUtente == "":
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"Inserire un valore all'interno della casella di testo.", color="red"))
            self._view.update_page()
            return

        # Verifico che sia intero
        try:
            valoreAnnoUtenteIntero = int(valoreAnnoUtente)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"Inserire un valore intero all'interno della casella di testo.", color="red"))
            self._view.update_page()
            return

        # Verifico che il numero sia positivo
        if valoreAnnoUtenteIntero < 1816 or valoreAnnoUtenteIntero > 2016:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"Inseire un anno compreso tra 1816 e 2016", color="red"))
            self._view.update_page()
            return

        self._model.buildGraph(valoreAnnoUtenteIntero)
        numNode, numEdges = self._model.getGraphDetails()

        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato!"))
        #self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {numNode} nodi e {numEdges} archi.", color="green"))
        self._view.update_page()

        # --- PUNTO D: Stampa il numero di componenti connesse ---
        num_comp = self._model.get_numero_componenti_connesse()
        self._view._txt_result.controls.append(
            ft.Text(f"\nIl grafo ha {num_comp} componenti connesse."))

        # Aggiorna la pagina per mostrare i nuovi elementi
        self._view.update_page()

        # --- PUNTO C: Stampa l'elenco degli stati e il numero di vicini ---
        self._view._txt_result.controls.append(
            ft.Text("Di seguito il dettaglio su i nodi:"))

        stati_vicini = self._model.get_stati_confinanti()
        stati_vicini.sort(key=lambda x: x[0].StateNme)  # ← ordine alfabetico

        for stato, grado in stati_vicini:
            # Cambia .StateName con il nome reale dell'attributo della tua classe Country
            self._view._txt_result.controls.append(ft.Text(f"- {stato.StateNme}: {grado} vicini"))
        self._view.update_page()

