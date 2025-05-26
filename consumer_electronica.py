import pika
import json

def callback(ch, method, properties, body):
    orden = json.loads(body)
    print("Orden Electrónica Procesada:")
    print(orden)

# Conectar
conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()

# Declarar cola y exchange
canal.exchange_declare(exchange='direct_ordenes', exchange_type='direct')
canal.queue_declare(queue='cola_electronica')
canal.queue_bind(exchange='direct_ordenes', queue='cola_electronica', routing_key='orden.electronica')

canal.basic_consume(queue='cola_electronica', on_message_callback=callback, auto_ack=True)
print(" Esperando órdenes electrónicas...")
canal.start_consuming()
