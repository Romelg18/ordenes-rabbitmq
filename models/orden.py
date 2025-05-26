import json
from datetime import datetime

class OrdenCompra:
    def __init__(self, cliente, producto, categoria, cantidad):
        self.cliente = cliente
        self.producto = producto
        self.categoria = categoria
        self.cantidad = cantidad
        self.fecha = datetime.utcnow()

    def to_json(self):
        return json.dumps({
            'cliente': self.cliente,
            'producto': self.producto,
            'categoria': self.categoria,
            'cantidad': self.cantidad,
            'fecha': self.fecha.isoformat()
        })
