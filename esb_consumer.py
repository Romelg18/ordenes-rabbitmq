import os
from azure.servicebus import ServiceBusClient
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env.consumer")


conn_str = os.getenv("SERVICE_BUS_CONNECTION_STRING")
queue_name = os.getenv("QUEUE_NAME")

# Conexión con Azure Service Bus
client = ServiceBusClient.from_connection_string(conn_str)

with client:
    receiver = client.get_queue_receiver(queue_name)
    with receiver:
        print("Esperando mensajes en la cola...")
        for msg in receiver.receive_messages(max_message_count=1, max_wait_time=10):
            print(f" Pedido recibido: {str(msg)}")
            receiver.complete_message(msg)
