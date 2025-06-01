from azure.servicebus import ServiceBusClient, ServiceBusMessage
from models.orden import OrdenCompra
import os
from dotenv import load_dotenv

load_dotenv()


CONNECTION_STR = os.getenv("AZURE_SERVICEBUS_CONNECTION_SEND")
QUEUE_NAME = "items"

orden = OrdenCompra("Romel Gualoto", "Teclado mecánico", "electronica", 2)
mensaje = orden.to_json()

with ServiceBusClient.from_connection_string(CONNECTION_STR) as client:
    sender = client.get_queue_sender(queue_name=QUEUE_NAME)
    with sender:
        msg = ServiceBusMessage(mensaje)
        sender.send_messages(msg)

print("✅ Orden enviada a Azure Service Bus")
