import redis

REDIS = redis.Redis(host='cache', port=6379, decode_responses=True)

API_URL = 'https://jservice.io/api/random'

APP_DESCRITION = (
    'This app, - gives question'
    ' with answer by using POST request.'
)
