from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyse', methods=['POST'])
def vader_analyse():
	print('Hello Vader')


if __name__=='__main__':
	app.run()