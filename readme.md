# Azure Service Bus con Python – Caso de uso: Sistema de Pedidos
- Elaborado por: Romel Gualoto
- Diseñó y arquitectura de Software
Este proyecto implementa un **productor** y un **consumidor** de mensajes utilizando **Azure Service Bus (ESB)** en Python, como parte de un caso de uso real: **gestión de pedidos**.

Este sistema incluye:

- `esb_producer.py`: envía un mensaje (pedido) a la cola `pedidos`.
- `esb_consumer.py`: escucha la cola y procesa los pedidos recibidos.

Se utilizan **dos archivos `.env` separados** para mantener seguras las credenciales de envío y recepción.

## Configuración inicial para poder ejecutar el programa 

### Paso 1: Instalar dependencias

pip install -r requirements.txt

### Paso 2: Crear archivos `.env`

Usa las plantillas `.env.producer.example` y `.env.consumer.example` para crear:

- `.env.producer` (con clave que tiene permiso `send`)
- `.env.consumer` (con clave que tiene permiso `listen`)

### `.env.producer` ejemplo (no contiene claves importantes de Azure):

SERVICE_BUS_CONNECTION_STRING=Endpoint=sb://ordenes-esb-romel.servicebus.windows.net/;SharedAccessKeyName=sendpedidosEvents;SharedAccessKey=TU_CLAVE  
QUEUE_NAME=pedidos

### `.env.consumer` ejemplo (no contiene claves importantes de Azure):

SERVICE_BUS_CONNECTION_STRING=Endpoint=sb://ordenes-esb-romel.servicebus.windows.net/;SharedAccessKeyName=listenpedidosEvents;SharedAccessKey=TU_CLAVE  
QUEUE_NAME=pedidos

##  Ejecución del programa

### Ejecutar el productor

python esb_producer.py

Esto enviará un pedido simulado a la cola.

### Ejecutar el consumidor

python esb_consumer.py

Esto recibirá el mensaje desde la cola y lo mostrará en consola.

