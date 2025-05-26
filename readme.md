# Sistema de Procesamiento de Órdenes con RabbitMQ

Este proyecto simula un sistema distribuido en el que se procesan órdenes de compra mediante un gestor de colas (RabbitMQ), utilizando dos tipos de exchanges: **direct** y **fanout**.

---

## ⚙️ Tecnologías utilizadas

-  Python 3.x
-  RabbitMQ
- pika (cliente AMQP para Python)

---

## Estructura del sistema

ordenes-rabbitmq/
├── producer.py # Envía órdenes a dos exchanges
├── consumer_electronica.py # Procesa órdenes de categoría "electronica"
├── consumer_auditor.py # Audita todas las órdenes (fanout)
├── models/
│ └── orden.py # Clase de modelo de orden
├── requirements.txt
└── README.md


---

## Exchanges usados

| Exchange         | Tipo     | Función                                      |
|------------------|----------|----------------------------------------------|
| direct_ordenes   | direct   | Enruta por categoría (ej. orden.electronica) |
| fanout_reporte   | fanout   | Envía cada orden a todos los consumidores    |

---

## Instalación y ejecución

### 1. Instalar dependencias
pip install -r requirements.txt

### 2. Iniciar consumidores (en terminales separadas)

**Consumidor 1: Electrónica**
python consumer_electronica.py
**Consumidor 2: Auditoría**
python consumer_auditor.py
### 3. Ejecutar productor

---

## Explicacion de que hace paso a paso 

- El **productor** envía una orden a:
  - Un exchange `direct` → llega a la cola específica por categoría
  - Un exchange `fanout` → llega a todos los consumidores

- RabbitMQ enruta los mensajes según los bindings definidos
- Los consumidores muestran la información procesada por consola

---

## Autores

- Romel Gualoto  
- William Ramirez 

Ambos integrantes participaron con commits identificables en el repositorio.

---

## Pasos para Visualización en RabbitMQ

- Ingresar al panel en [http://localhost:15672](http://localhost:15672)
- Usuario: `guest` | Contraseña: `guest`
- Ver en pestañas:
  - **Exchanges**: `direct_ordenes`, `fanout_reporte`
  - **Queues**: `cola_electronica`, `cola_auditoria`
  - **Bindings** y mensajes en tiempo real

