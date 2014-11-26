-- we put the load command in a separate file so we can import it several times

define load_gdelt() returns gdelt {
	$gdelt = load '$gdelt_file' as (
		event_id: chararray,
		sql_date: chararray,
		month_year: chararray,
		year: chararray,
		fraction_date: chararray,
		actor1: chararray,
		actor1_name: chararray,
		actor1_country: chararray,
		actor1_known_group: chararray,
		actor1_ethnic: chararray,
		actor1_religion1: chararray,
		actor1_religion2: chararray,
		actor1_type1: chararray,
		actor1_type2: chararray,
		actor1_type3: chararray,

		-- actor 2
		actor2: chararray,
		actor2_name: chararray,
		actor2_country: chararray,
		actor2_known_group: chararray,
		actor2_ethnic: chararray,
		actor2_religion1: chararray,
		actor2_religion2: chararray,
		actor2_type1: chararray,
		actor2_type2: chararray,
		actor2_type3: chararray,
		
		is_root_event: int,
		event: int,
		event_base: int,
		event_root: int,
		quad_class: int,
		
		goldstein_scale: float,
		num_mentions: int,
		num_sources: int,
		num_articles: int,
		avg_tone: float,
		
		actor1_geo_type: chararray,
		actor1_geo_full_name: chararray,
		actor1_geo_country: chararray,
		actor1_geo_adm1_code: chararray,
		actor1_lat: float,
		actor1_lng: float,
		actor1_feature_id: chararray,
		
		actor2_geo_type: chararray,
		actor2_geo_full_name: chararray,
		actor2_geo_country: chararray,
		actor2_geo_adm1_code: chararray,
		actor2_lat: float,
		actor2_lng: float,
		actor2_feature_id: chararray,
		
		action_geo_type: chararray,
		action_geo_full_name: chararray,
		action_geo_country: chararray,
		action_geo_adm1_code: chararray,
		action_lat: float,
		action_lng: float,
		action_feature_id: chararray,
		
		date_added: chararray,
		source_url: chararray
		
	);
};