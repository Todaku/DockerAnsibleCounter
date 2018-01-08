from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
	redis.incr('hits')
	return 'Counter: %s; refreshing this page increments by 1; going to :5001 container will reset counter' % redis.get('hits')

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)
