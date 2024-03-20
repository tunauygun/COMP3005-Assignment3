CREATE TABLE students (
	 student_id		SERIAL PRIMARY KEY,
	 first_name		VARCHAR(255) NOT NULL,
	 last_name		VARCHAR(255) NOT NULL,
	 email			VARCHAR(255) NOT NULL UNIQUE,
	 enrollment_date	DATE
);