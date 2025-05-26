import pika
import json
from models.order_tracking import OrdenTracking

def callback(ch, method, properties, body):
    data = json.loads(body)
    tracking = OrdenTracking(
        cliente=data['cliente'],
        producto=data['producto'],
        categoria=data['categoria']
    )

    print("🚚 Seguimiento de Orden:")
    print(tracking.__dict__)

    # Guardar en archivo 
    with open("tracking_log.txt", "a") as archivo:
        archivo.write(tracking.to_json() + "\n")

conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()

canal.exchange_declare(exchange='fanout_reporte', exchange_type='fanout')
canal.queue_declare(queue='cola_tracking')
canal.queue_bind(exchange='fanout_reporte', queue='cola_tracking')

canal.basic_consume(queue='cola_tracking', on_message_callback=callback, auto_ack=True)
print("📦 Esperando órdenes para seguimiento...")
canal.start_consuming()
