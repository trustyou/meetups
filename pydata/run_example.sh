#!/usr/bin/env bash

# Crawl all meetups and train a Word2Vec model from their descriptions. Takes a few hours :)
# After running this, look in the "data" folder for output

python -m luigi --local-scheduler --module tasks.analyze AnalyzeTask
