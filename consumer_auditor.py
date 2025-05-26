import pika
import json

def callback(ch, method, properties, body):
    orden = json.loads(body)
    print(" Auditoría recibió orden:")
    print(orden)

# Conectar
conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()

# Crear exchange fanout y cola auditoría
canal.exchange_declare(exchange='fanout_reporte', exchange_type='fanout')
canal.queue_declare(queue='cola_auditoria')
canal.queue_bind(exchange='fanout_reporte', queue='cola_auditoria')

canal.basic_consume(queue='cola_auditoria', on_message_callback=callback, auto_ack=True)
print("Auditor escuchando todas las órdenes...")
canal.start_consuming()
