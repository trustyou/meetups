meetups
=======

Code samples and materials for tech talks and meetups hosted by TrustYou

# [BigData/DataScience Cluj-Napoca meetup](http://www.meetup.com/Big-Data-Data-Science-Meetup-Cluj-Napoca/events/216156792/)

In this meetup we shared some insights into the TrustYou big data tech stack, and gave introductions to two tools we've found useful: [Apache Pig](http://pig.apache.org/) and [Luigi](https://github.com/spotify/luigi). The examples from the slides are contained in this repo.

## Apache Pig

Install Apache Pig, e.g. from their website. No Hadoop necessary! Alternatively, give the Hortonworks sandbox a try if you're planning to try out other Hadoop-related technologies as well. Then, run this:

```
cd pig
./run_examples.sh
```

Look in the *.tsv sub folders for the output - when run locally, Apache Pig mimics the folder structure of job output in the HDFS, so the data will be in part files.

## Luigi

Install dependencies by running `pip install -r requirements.txt` from luigi folder. Then, run:

```
cd luigi
./run_example.sh
```