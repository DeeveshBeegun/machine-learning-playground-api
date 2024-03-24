import nltk
from flask import Flask, request, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm
from transformer import pipeline

nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route('/analyse', methods=['POST'])
def vader_analyse():
	sentimentAnalyzer = SentimentIntensityAnalyzer()
	text = request.form['text']
	senti_dict = sentimentAnalyzer.polarity_scores(text)

	senti_dict["compound"] = round(senti_dict["compound"]*100, 1)
	senti_dict["neg"] = round(senti_dict["neg"]*100, 1)
	senti_dict["neu"] = round(senti_dict["neu"]*100, 1)
	senti_dict["pos"] = round(senti_dict["pos"]*100, 1)

	return senti_dict

@app.route('/duplicate', methods=['POST'])
def dupliate():
	text = request.form['text']
	num_duplicates = request.form['times']

	return (text + " ") * int(num_duplicates)


@app.route('/summarize', methods=['POST'])
def summarize():
	text = request.form['text']
	summarizer = pipeline('summarization', model="sshleifer/distilbart-cnn-12-6")

	return summarizer(text, do_sample=False)

if __name__=='__main__':
	app.run()
	create_app()