CREATE TABLE countries ( 
country_id varchar(2),
country_name  varchar(40),
region_id  decimal(10,0),
CHECK(COUNTRY_NAME IN('Italy','India','China'))
);
