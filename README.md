# 🧭 Smart Queue - Queue Service

The **Queue Service** is a lightweight microservice in the **Smart Queue Management System** designed for **real-time queue handling**. It enables reactive updates through **Redis Pub/Sub**, listening to appointment events and broadcasting them to subscribers like the Notification Service.

---

## 🚀 Features

* ⚡ Subscribes to real-time `queue_updates` channel from Redis
* 📡 Enables reactive microservices (e.g., email/SMS alerts)
* 🐍 Built in Python for fast, script-based operation
* 🔌 Decoupled architecture using Redis Pub/Sub
* 🐳 Dockerized for containerized deployment

---

## 🛠️ Tech Stack

* **Language**: Python 3.12
* **Messaging**: Redis (Azure Cache for Redis)
* **Environment**: .env based configuration
* **Pattern**: Publisher/Subscriber
* **Containerization**: Docker

---

## 📁 Project Structure

```
smart-queue-queue-service/
├── queue_subscriber.py     # Main Redis subscriber script
├── queue_publisher.py      # Sample message publisher (for testing)
├── utils.py                # Utility for Redis connection setup
├── requirements.txt        # Python dependencies
├── .env                    # Redis credentials
├── Dockerfile              # Docker setup
└── venv/                   # Local virtualenv (excluded in Docker)
```

---

## 🔁 Redis Pub/Sub Integration

This service **listens** to the `queue_updates` Redis channel and can optionally **publish test messages** using `queue_publisher.py`.

### Sample message format:

```json
{
  "event": "appointment_created",
  "data": {
    "appointmentId": "1234",
    "patientName": "Mustafa",
    "time": "2025-05-10T14:30:00Z"
  }
}
```

### Redis `.env` file format:

```ini
REDIS_HOST=smartqueueredis.redis.cache.windows.net
REDIS_PORT=6380
REDIS_PASSWORD=your_password
REDIS_USE_SSL=True
```

---

## 🐳 Docker Instructions

### 🔧 Build the image

```bash
docker build -t smart-queue-queue-service .
```

### ▶️ Run the container

```bash
docker run --env-file .env smart-queue-queue-service
```

> The container will automatically subscribe to `queue_updates` and start listening.

---

## 🧪 Testing the Pub/Sub

You can publish a sample message using the test script:

```bash
python queue_publisher.py
```

You should see the message consumed by `queue_subscriber.py` or by the Notification Service.

---

## 📄 Example Docker Compose Snippet

```yaml
queue-service:
  build: ./smart-queue-queue-service
  command: python queue_subscriber.py
  env_file:
    - ./smart-queue-queue-service/.env
```

---

## 📄 License

This project is licensed under the MIT License.
