"""
Scrapy crawl commands, wrapped in Luigi tasks.
"""

import os
import os.path
import subprocess

import luigi

class CrawlTask(luigi.Task):
	"""
	Crawl a specific city.
	"""
	
	city = luigi.Parameter()
	
	def output(self):
		output_path = os.path.join("data", "{}.jsonl".format(self.city))
		return luigi.LocalTarget(output_path)

	def run(self):
		# Scrapy starts a Twisted reactor. You can try invoking scrapy
		# programmatically, but it does not play well with Luigi process pools.
		# So let's just start a sub process.
		tmp_output_path = self.output().path + "_tmp"
		subprocess.check_output(["scrapy", "crawl", "city", "-a", "city={}".format(self.city), "-o", tmp_output_path, "-t", "jsonlines"])
		os.rename(tmp_output_path, self.output().path)

class DeepCrawlTask(luigi.Task):
	"""
	Utilize the meetup.com/sitemap.xml to discover all visible meetup groups.
	"""

	def output(self):
		output_path = os.path.join("data", "all_meetups.jsonl")
		return luigi.LocalTarget(output_path)

	def run(self):
		tmp_output_path = self.output().path + "_tmp"
		subprocess.check_output(["scrapy", "crawl", "all","-o", tmp_output_path, "-t", "jsonlines"])
		os.rename(tmp_output_path, self.output().path)
