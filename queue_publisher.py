import redis
import os
from dotenv import load_dotenv

load_dotenv()

redis_conn = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    password=os.getenv("REDIS_PASSWORD"),
    ssl=True
)

def publish_update(channel, message):
    redis_conn.publish(channel, message)
    print(f"✅ Published: {message} to {channel}")

# Test publish
publish_update("queue_updates", "Patient B has entered the queue.")