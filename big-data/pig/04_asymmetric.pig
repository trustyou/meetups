/*
 * Example: Asymmetric country relations
 */

import 'load_gdelt.pig';

gdelt = load_gdelt();

-- we're only interested in countries
gdelt = filter (
	foreach gdelt generate actor1_country, actor2_country, goldstein_scale
	) by actor1_country != '' and actor2_country != '';

gdelt_grp = group gdelt by (actor1_country, actor2_country);

-- it's not necessary to aggregate twice - except that Pig doesn't allow self joins
gold_1 = foreach gdelt_grp generate
	group.actor1_country as actor1_country,
	group.actor2_country as actor2_country,
	SUM(gdelt.goldstein_scale) as goldstein_scale;
gold_2 = foreach gdelt_grp generate
	group.actor1_country as actor1_country,
	group.actor2_country as actor2_country,
	SUM(gdelt.goldstein_scale) as goldstein_scale;

-- join both sums together, to get the Goldstein values for both directions in one row
gold = join gold_1 by (actor1_country, actor2_country), gold_2 by (actor2_country, actor1_country);

-- compute the difference in Goldstein score
gold = foreach gold generate
	gold_1::actor1_country as actor1_country,
	gold_1::actor2_country as actor2_country,
	gold_1::goldstein_scale as gold_1,
	gold_2::goldstein_scale as gold_2,
	ABS(gold_1::goldstein_scale - gold_2::goldstein_scale) as diff;

-- keep only the values where one direction is positive, the other negative
-- also, remove all duplicate rows
gold = filter gold by gold_1 * gold_2 < 0 and actor1_country < actor2_country;

gold = order gold by diff desc;

store gold into '04_asymmetric.tsv';