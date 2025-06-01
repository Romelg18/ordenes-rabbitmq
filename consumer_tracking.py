from azure.servicebus import ServiceBusClient
import json
import os
from models.order_tracking import OrdenTracking
from dotenv import load_dotenv
load_dotenv()


CONNECTION_STR = os.getenv("AZURE_SERVICEBUS_CONNECTION_LISTEN")
QUEUE_NAME = "items"

def callback(msg):
    data = json.loads(str(msg))
    tracking = OrdenTracking(
        cliente=data['cliente'],
        producto=data['producto'],
        categoria=data['categoria']
    )

    print("🚚 Seguimiento de Orden:")
    print(tracking.__dict__)

    with open("tracking_log.txt", "a") as archivo:
        archivo.write(tracking.to_json() + "\n")

with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
    receiver = client.get_queue_receiver(queue_name=QUEUE_NAME)
    with receiver:
        for msg in receiver:
            callback(msg)
            receiver.complete_message(msg)
