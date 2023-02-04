CREATE TABLE countries ( 
country_id varchar(2),
country_name  varchar(40),
region_id  decimal(10,0),
CHECK(COUNTRY_NAME IN('Italy','India','China'))
);

INSERT INTO countries (country_id, country_name, region_id)
VALUES (1, 'India', 111);

INSERT INTO countries (country_id, country_name, region_id)
VALUES (2, 'China', 222);

INSERT INTO countries (country_id, country_name, region_id)
VALUES (3, 'USA', 333);

INSERT INTO countries (country_id, country_name, region_id)
VALUES (3, 'Italy', 333);

SELECT * FROM countries;

DESC countries;