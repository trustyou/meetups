#!/usr/bin/env bash

# Luigi example shown in the meetup http://www.meetup.com/Big-Data-Data-Science-Meetup-Cluj-Napoca/events/216156792/
# After running this, look in the "data" folder for output

./luigi_demo.py --local-scheduler ExtractTask --url http://www.trustyou.com
