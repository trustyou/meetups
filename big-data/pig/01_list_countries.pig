/*
 * Example: Look at all non-empty actor countries
 */

import 'load_gdelt.pig';

gdelt = load_gdelt();

-- where:
gdelt = filter gdelt by actor1_country != '';

-- select:
country = foreach gdelt generate actor1_country;

store country into '01_list_countries.tsv';