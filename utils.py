import redis
import os
from dotenv import load_dotenv

load_dotenv()

def get_redis_connection():
    return redis.Redis(
        host=os.getenv("REDIS_HOST"),
        port=int(os.getenv("REDIS_PORT")),
        password=os.getenv("REDIS_PASSWORD"),
        ssl=bool(os.getenv("REDIS_USE_SSL", "False") == "True"),
        decode_responses=True
    )