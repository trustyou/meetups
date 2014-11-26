meetups
=======

Code samples and materials for tech talks and meetups hosted by TrustYou

# [BigData/DataScience Cluj-Napoca meetup](http://www.meetup.com/Big-Data-Data-Science-Meetup-Cluj-Napoca/events/216156792/)

In this meetup we shared some insights into the TrustYou big data tech stack, and gave introductions to two tools we've found useful: [Apache Pig](http://pig.apache.org/) and [Luigi](https://github.com/spotify/luigi). The examples from the slides are contained in this repo.

## Apache Pig

Install Apache Pig, e.g. from their website. No Hadoop necessary! Alternatively, give the Hortonworks sandbox a try if you're planning to try out other Hadoop-related technologies as well. Then, run this:

```
$ cd big-data/pig
$ ./run_examples.sh
```

Look in the *.tsv sub folders for the output - when run locally, Apache Pig mimics the folder structure of job output in the HDFS, so the data will be in part files.

## Luigi

Install dependencies by running `pip install -r requirements.txt` from luigi folder. Then, run:

```
$ cd big-data/luigi
$ ./run_example.sh
```

# [Cluj.py "Extending Python in C" meetup](http://www.meetup.com/Cluj-py/events/218034932/)

We had a look behind the scenes of CPython, the reference implementation of Python, and its C API which allows you to extend the Python language in C. Finally we checked out [Cython](http://cython.org/), which seems to be the sanest way of writing C extensions of Python.

In the examples we focused on benchmarking different implementations of QuickSort in Python, C and Cython. Before trying them, run `pip install -r requirements.txt` from the python-c folder. I propose to run the following inside a [virtualenv](http://virtualenv.readthedocs.org/en/latest/):

```
$ virtualenv venv
$ . venv/bin/activate 
(venv) $ cd python-c
(venv) $ ./run_examples.sh
```