drop table if exists configs;
create table config (
	id integer primary key autoincrement,	 
	    config_catalog string not null,
        config_key string not null,
        config_value string null);
		
drop table if exists sources;
create table sources (
	id integer primary key autoincrement,
	    name string not null,
		description string not null,
	    ftp_user string not null,
        ftp_pass string not null,
        ftp_host string not null,
		ftp_portno string null,
		ftp_path string null,
		ftp_filter string null,
		ftp_filter_max_date integer null		
		);
		
drop table if exists files;
create table files (
	id integer primary key autoincrement,
	  name string not null,
		location string not null,
	  location_used string not null,
    status string not null,
		total_length integer null,
		start_date timestamp not null,
		completed_date timestamp null,
		completed_length integer null);

drop table if exists logs;
create table logs (
	id integer primary key autoincrement,
	    log_time timestamp not null,
		level string null,
		description string null);		
		
		
		
