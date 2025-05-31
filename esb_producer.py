import os
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env.producer")


# Leer datos del archivo .env
conn_str = os.getenv("SERVICE_BUS_CONNECTION_STRING")
queue_name = os.getenv("QUEUE_NAME")

# Conexión con Azure Service Bus
client = ServiceBusClient.from_connection_string(conn_str)

with client:
    sender = client.get_queue_sender(queue_name)
    with sender:
        # Crear el mensaje de pedido
        mensaje = ServiceBusMessage(" Pedido nuevo: Cliente A, Producto Z, Cantidad: 2")
        sender.send_messages(mensaje)
        print("Pedido enviado al ESB")
