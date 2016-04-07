DROP TABLE energy;

create external table energy (
	timestamp string, 
	url string, 
	created_at string,  
	ba string, 
	market string, 
	carbon double, 
	freq string, 
    	genmix_biogas_gen_MW double,
	genmix_biomass_gen_MW double, 
	genmix_solar_gen_MW double,
	genmix_nonwind_gen_MW double, 
	genmix_renewable_gen_MW double, 
	genmix_wind_gen_MW double, 
	genmix_nuclear_gen_MW double,
	genmix_thermal_gen_MW double, 
	genmix_coal_gen_MW double, 
	genmix_refuse_gen_MW double, 
	genmix_other_gen_MW double, 
	genmix_natgas_gen_MW double, 
	genmix_hydro_gen_MW double
  )
row format serde 'org.openx.data.jsonserde.JsonSerDe'
with serdeproperties (
'paths'= 'timestamp string, 
	url string, 
	created_at string,  
	ba string, 
	market string, 
	carbon double, 
	freq string, 
    genmix_biogas_gen_MW double,
	genmix_biomass_gen_MW double, 
	genmix_solar_gen_MW double,
	genmix_nonwind_gen_MW double, 
	genmix_renewable_gen_MW double, 
	genmix_wind_gen_MW double, 
	genmix_nuclear_gen_MW double,
	genmix_thermal_gen_MW double, 
	genmix_coal_gen_MW double, 
	genmix_refuse_gen_MW double, 
	genmix_other_gen_MW double, 
	genmix_natgas_gen_MW double, 
	genmix_hydro_gen_MW double'
)
stored as textfile
location '/user/w205/W205FinalProject' ;
