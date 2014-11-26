/*
 * Example: Histogram of actor countries
 */

import 'load_gdelt.pig';

gdelt = load_gdelt();

gdelt_grp = group gdelt by actor1_country;

gdelt_cnt = foreach gdelt_grp generate
	group as country,
	COUNT(gdelt) as count;

store gdelt_cnt into '02_country_counts.tsv';