import pika
from models.orden import OrdenCompra

# Crear orden de ejemplo
orden = OrdenCompra("Romel Gualoto", "Teclado mecánico", "electronica", 2)
mensaje = orden.to_json()

# Conectar a RabbitMQ
conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()

# Crear Exchanges
canal.exchange_declare(exchange='direct_ordenes', exchange_type='direct')
canal.exchange_declare(exchange='fanout_reporte', exchange_type='fanout')

# Enviar al direct exchange con routing key 'orden.electronica'
canal.basic_publish(
    exchange='direct_ordenes',
    routing_key='orden.electronica',
    body=mensaje
)

# Enviar también al fanout (reporte general)
canal.basic_publish(
    exchange='fanout_reporte',
    routing_key='',
    body=mensaje
)

print("Orden enviada a ambos exchanges")
conexion.close()
