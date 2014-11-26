/*
 * Example: Count events and distinct event types
 */

import 'load_gdelt.pig';

gdelt = load_gdelt();

gdelt_grp = group gdelt all;
gdelt_cnt = foreach gdelt_grp generate COUNT(gdelt);
store gdelt_cnt into '03_count_events.tsv';

event = foreach gdelt generate event;
event_dis = distinct event;
event_grp = group event_dis all;
event_cnt = foreach event_grp generate COUNT(event_dis);
store event_cnt into '03_count_event_types.tsv';

