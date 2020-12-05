import redis
from config.database import redis as cfg

__all__:['r']

r = redis.Redis(
    host=cfg['host'],
    port=cfg['port'],
    password=cfg['password'],
    db=cfg['database']
)