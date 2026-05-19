from model.model import Model

myModel = Model()
myModel.buildGraph(1945)
node, edges = myModel.getGraphDetails()
print(f"nodi: {node}, edges: {edges}")
