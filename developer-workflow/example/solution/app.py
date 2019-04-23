import time, redis, os
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=os.getenv('REDIS_PORT', '6379'))

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv('FLASK_PORT', '8080'), debug=True)