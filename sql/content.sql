create table content
(
	content_id integer primary key autoincrement, 
	name_dictionary varchar(500),
	value varchar(2000),
	foreign key (name_dictionary) references dictionary(name)

);
