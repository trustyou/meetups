"""
Building a Word2Vec model from the data we've crawled from meetup.com.
"""

import json
import luigi
import os.path

import gensim
import nltk

from tasks.crawl import DeepCrawlTask

class AnalyzeTask(luigi.Task):
	"""
	Build and save a Word2Vec model based on meetup descriptions.
	"""
	
	def requires(self):
		return DeepCrawlTask()

	def output(self):
		output_path = os.path.join("data", "word2vec")
		return luigi.LocalTarget(output_path)
	
	def run(self):

		def descr_sentences():
			"""
			Stream sentences from meetup descriptions from disk.
			"""
			with open("meetup.jsonl") as city_file:
				for meetup_str in city_file:
					meetup = json.loads(meetup_str)
					for sentence in nltk.sent_tokenize(meetup["description"]):
						# Lower-case for normalization
						yield nltk.word_tokenize(sentence.lower())

		# Build a bigram model so that we capture phrases like "big_data"
		bigrams_model = gensim.models.Phrases(descr_sentences())

		class bigrams:
			def __iter__(self):
				for sentence in descr_sentences():
					yield bigrams_model[sentence]

		model = gensim.models.Word2Vec(bigrams(), workers=4, min_count=10)
		model.save(self.output().path)
