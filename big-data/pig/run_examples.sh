#!/usr/bin/env bash

# Pig examples shown in the meetup http://www.meetup.com/Big-Data-Data-Science-Meetup-Cluj-Napoca/events/216156792/
# When run in local mode, Pig creates folders and files similar to the structure of mapper & reducer output in HDFS. So you'll find the output in "part-*" files in sub folders.

set -e

if ! hash pig 2>/dev/null; then
    echo >&2 "Please install Apache Pig, e.g. from http://pig.apache.org/"
    exit 1
fi

gdelt_file=20141112.export.CSV
if [ ! -f "$gdelt_file" ]; then
    wget "http://data.gdeltproject.org/events/$gdelt_file.zip"
    unzip "$gdelt_file.zip"
fi

echo "*** Running example 1"
rm -r 01_list_countries.tsv 2>/dev/null || true
pig -x local -param gdelt_file=$gdelt_file 01_list_countries.pig
head 01_list_countries.tsv/part-*

echo "*** Running example 2"
rm -r 02_country_counts.tsv 2>/dev/null || true
pig -x local -param gdelt_file=$gdelt_file 02_country_counts.pig
head 02_country_counts.tsv/part-*

echo "*** Running example 3"
rm -r 03_count_events.tsv 03_count_event_types.tsv 2>/dev/null || true
pig -x local -param gdelt_file=$gdelt_file 03_count_events.pig
cat 03_count_events.tsv/part-*
cat 03_count_event_types.tsv/part-*

echo "*** Running example 4"
rm -r 04_asymmetric.tsv 2>/dev/null || true
pig -x local -param gdelt_file=$gdelt_file 04_asymmetric.pig
head 04_asymmetric.tsv/part-*
