import redis
import os
from dotenv import load_dotenv

load_dotenv()

redis_conn = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    password=os.getenv("REDIS_PASSWORD"),
    ssl=True  # Azure Redis requires SSL
)

pubsub = redis_conn.pubsub()
pubsub.subscribe('queue_updates')

print("Subscribed to queue_updates. Waiting for messages...")

for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"📩 New message received: {message['data'].decode()}")