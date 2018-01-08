from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
	redis.set('hits', 0)
	return 'This is the 2nd container under the /sub directory; upon access, the counter will reset to 0.'

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80,debug=True)
