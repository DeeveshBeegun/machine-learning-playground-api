from flask import Flask, request, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm

app = Flask(__name__)

@app.route('/analyse', methods=['POST'])
def vader_analyse():
	sentimentAnalyzer = SentimentIntensityAnalyzer()
	text = request.form['text']
	senti_dict = sentimentAnalyzer.polarity_scores(text)

	return str(senti_dict["compound"])

if __name__=='__main__':
	app.run()
	create_app()