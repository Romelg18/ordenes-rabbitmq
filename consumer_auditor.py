from azure.servicebus import ServiceBusClient
import json
import os

from dotenv import load_dotenv
load_dotenv()


CONNECTION_STR = os.getenv("AZURE_SERVICEBUS_CONNECTION_LISTEN")
QUEUE_NAME = "items"

def callback(msg):
    orden = json.loads(str(msg))
    print("Auditoría recibió orden:")
    print(orden)

with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
    receiver = client.get_queue_receiver(queue_name=QUEUE_NAME)
    with receiver:
        for msg in receiver:
            callback(msg)
            receiver.complete_message(msg)
