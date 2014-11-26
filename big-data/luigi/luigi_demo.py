#!/usr/bin/env python

import hashlib
import os.path

import bs4
import luigi
import requests

class CrawlTask(luigi.Task):
	"""
	Crawl a URL and store the response on disk.
	"""
	
	url = luigi.Parameter()

	def output(self):
		url_hash = hashlib.md5(self.url).hexdigest()
		return luigi.LocalTarget(os.path.join("data", "crawl_" + url_hash))

	def run(self):
		req = requests.get(self.url)
		res = req.text
		with self.output().open("w") as out:
			out.write(res.encode("utf-8"))

class ExtractTask(luigi.Task):
	"""
	Extract the URLs from all <a> nodes of a previously crawled page.
	"""

	url = luigi.Parameter()

	def requires(self):
		return CrawlTask(self.url)

	def output(self):
		url_hash = hashlib.md5(self.url).hexdigest()
		return luigi.LocalTarget(os.path.join("data", "extract_" + url_hash))

	def run(self):
		soup = bs4.BeautifulSoup(self.input().open().read())
		with self.output().open("w") as out:
			for link in soup.find_all("a"):
				out.write(str(link.get("href")) + "\n")

if __name__ == "__main__":
	luigi.run()
