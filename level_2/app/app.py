import json
from flask import (
    Flask, 
    request
)
import redis
from slow_computation import compute

from lib.celery import make_celery
from lib.exceptions import LogException
from lib.logs import (
    parse_log_to_dict,
)

app = Flask(__name__)
app.config.update(CELERY_CONFIG={
    'broker_url': 'redis://redis-queue:6379',
    'result_backend': 'redis://redis-queue:6379',
})
redis_logs = redis.Redis(host='redis-logs', port=6379)

@app.post('/')
def handle_log():
    try:
        log = parse_log_to_dict(log=request.json['log'])
        process_and_store_log.delay(log)
        return (request.json, 201)
    except LogException as e:
        return (f'LogException: {e}', 400)


celery = make_celery(app)

@celery.task(name='app.app.process_and_store_log')
def process_and_store_log(
    log: dict
):
    """
    Process and Add Log to Redis List
    """
    print(log)
    print(redis_logs)
    enriched_log = {**log}
    compute(enriched_log)
    print(enriched_log)
    # client.lpush('Loglist', json.dumps(enriched_log))


if __name__ == '__main__':
    app.run(debug=True)