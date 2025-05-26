import json
from datetime import datetime

class OrdenTracking:
    def __init__(self, cliente, producto, categoria):
        self.cliente = cliente
        self.producto = producto
        self.categoria = categoria
        self.fecha_recepcion = datetime.now().isoformat()

    def to_json(self):
        return json.dumps(self.__dict__)
