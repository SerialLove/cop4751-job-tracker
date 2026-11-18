	#	Time	Action	Message	Duration / Fetch
3	1	19:14:01	CREATE DATABASE IF NOT EXISTS job_tracker	1 row(s) affected	0.000 sec
3	2	19:14:01	USE job_tracker	0 row(s) affected	0.000 sec
1	3	19:14:01	DROP TABLE IF EXISTS applications	0 row(s) affected, 1 warning(s):
 1051 Unknown table 'job_tracker.applications'	0.016 sec
1	4	19:14:01	DROP TABLE IF EXISTS contacts	0 row(s) affected, 1 warning(s):
 1051 Unknown table 'job_tracker.contacts'	0.000 sec
1	5	19:14:01	DROP TABLE IF EXISTS jobs	0 row(s) affected, 1 warning(s):
 1051 Unknown table 'job_tracker.jobs'	0.000 sec
1	6	19:14:01	DROP TABLE IF EXISTS companies	0 row(s) affected, 1 warning(s):
 1051 Unknown table 'job_tracker.companies'	0.000 sec
3	7	19:14:01	CREATE TABLE companies (
     company_id INT PRIMARY KEY AUTO_INCREMENT,
     company_name VARCHAR(100) NOT NULL,
     industry VARCHAR(50),
     website VARCHAR(200),
     city VARCHAR(50),
     state VARCHAR(50),
     notes TEXT
 )	0 row(s) affected	0.031 sec
3	8	19:14:01	CREATE TABLE jobs (
     job_id INT PRIMARY KEY AUTO_INCREMENT,
     company_id INT NOT NULL,
     job_title VARCHAR(100) NOT NULL,
     job_type ENUM('Full-time', 'Part-time', 'Contract', 'Internship') DEFAULT 'Full-time',
     salary_min INT,
     salary_max INT,
     job_url VARCHAR(300),
     date_posted DATE,
     requirements JSON,
     FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
 )	0 row(s) affected	0.016 sec
0	9	19:14:01	CREATE TABLE applications (
     application_id INT PRIMARY KEY AUTO_INCREMENT,
     job_id INT NOT NULL,
     application_date DATE NOT NULL,
     status ENUM('Applied', 'Screening', 'Interview', 'Offer', 'Rejected', 'Withdrawn') DEFAULT 'Applied',
     resume_version VARCHAR(50),
     cover_letter_sent BOOLEAN DEFAULT FALSE,
     interview_data JSON,
     FOREIGN	Error Code: 1064. You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 9	0.015 sec
1	10	19:32:49	CREATE DATABASE IF NOT EXISTS job_tracker	1 row(s) affected, 1 warning(s):
 1007 Can't create database 'job_tracker'; database exists	0.000 sec
3	11	19:32:49	USE job_tracker	0 row(s) affected	0.000 sec
1	12	19:32:49	DROP TABLE IF EXISTS applications	0 row(s) affected, 1 warning(s):
 1051 Unknown table 'job_tracker.applications'	0.000 sec
1	13	19:32:49	DROP TABLE IF EXISTS contacts	0 row(s) affected, 1 warning(s):
 1051 Unknown table 'job_tracker.contacts'	0.015 sec
3	14	19:32:49	DROP TABLE IF EXISTS jobs	0 row(s) affected	0.016 sec
3	15	19:32:49	DROP TABLE IF EXISTS companies	0 row(s) affected	0.000 sec
3	16	19:32:49	CREATE TABLE companies (
     company_id INT PRIMARY KEY AUTO_INCREMENT,
     company_name VARCHAR(100) NOT NULL,
     industry VARCHAR(50),
     website VARCHAR(200),
     city VARCHAR(50),
     state VARCHAR(50),
     notes TEXT
 )	0 row(s) affected	0.015 sec
3	17	19:32:50	CREATE TABLE jobs (
     job_id INT PRIMARY KEY AUTO_INCREMENT,
     company_id INT NOT NULL,
     job_title VARCHAR(100) NOT NULL,
     job_type ENUM('Full-time', 'Part-time', 'Contract', 'Internship') DEFAULT 'Full-time',
     salary_min INT,
     salary_max INT,
     job_url VARCHAR(300),
     date_posted DATE,
     requirements JSON,
     FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
 )	0 row(s) affected	0.032 sec
0	18	19:32:50	CREATE TABLE applications (
     application_id INT PRIMARY KEY AUTO_INCREMENT,
     job_id INT NOT NULL,
     application_date DATE NOT NULL,
     status ENUM('Applied', 'Screening', 'Interview', 'Offer', 'Rejected', 'Withdrawn') DEFAULT 'Applied',
     resume_version VARCHAR(50),
     cover_letter_sent BOOLEAN DEFAULT FALSE,
     interview_data JSON,
     FOREIGN	Error Code: 1064. You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 9	0.000 sec
1	19	19:34:03	CREATE DATABASE IF NOT EXISTS job_tracker	1 row(s) affected, 1 warning(s):
 1007 Can't create database 'job_tracker'; database exists	0.000 sec
3	20	19:34:03	USE job_tracker	0 row(s) affected	0.000 sec
1	21	19:34:03	DROP TABLE IF EXISTS applications	0 row(s) affected, 1 warning(s):
 1051 Unknown table 'job_tracker.applications'	0.000 sec
1	22	19:34:03	DROP TABLE IF EXISTS contacts	0 row(s) affected, 1 warning(s):
 1051 Unknown table 'job_tracker.contacts'	0.000 sec
3	23	19:34:03	DROP TABLE IF EXISTS jobs	0 row(s) affected	0.015 sec
3	24	19:34:03	DROP TABLE IF EXISTS companies	0 row(s) affected	0.016 sec
3	25	19:34:03	CREATE TABLE companies (
     company_id INT PRIMARY KEY AUTO_INCREMENT,
     company_name VARCHAR(100) NOT NULL,
     industry VARCHAR(50),
     website VARCHAR(200),
     city VARCHAR(50),
     state VARCHAR(50),
     notes TEXT
 )	0 row(s) affected	0.015 sec
3	26	19:34:03	CREATE TABLE jobs (
     job_id INT PRIMARY KEY AUTO_INCREMENT,
     company_id INT NOT NULL,
     job_title VARCHAR(100) NOT NULL,
     job_type ENUM('Full-time', 'Part-time', 'Contract', 'Internship') DEFAULT 'Full-time',
     salary_min INT,
     salary_max INT,
     job_url VARCHAR(300),
     date_posted DATE,
     requirements JSON,
     FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
 )	0 row(s) affected	0.032 sec
0	27	19:34:03	CREATE TABLE applications (
     application_id INT PRIMARY KEY AUTO_INCREMENT,
     job_id INT NOT NULL,
     application_date DATE NOT NULL,
     status ENUM('Applied', 'Screening', 'Interview', 'Offer', 'Rejected', 'Withdrawn') DEFAULT 'Applied',
     resume_version VARCHAR(50),
     cover_letter_sent BOOLEAN DEFAULT FALSE,
     interview_data JSON,
     FOREIGN	Error Code: 1064. You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 9	0.015 sec
1	28	19:35:14	CREATE DATABASE IF NOT EXISTS job_tracker	1 row(s) affected, 1 warning(s):
 1007 Can't create database 'job_tracker'; database exists	0.000 sec
3	29	19:35:14	USE job_tracker	0 row(s) affected	0.000 sec
1	30	19:35:14	DROP TABLE IF EXISTS applications	0 row(s) affected, 1 warning(s):
 1051 Unknown table 'job_tracker.applications'	0.000 sec
1	31	19:35:14	DROP TABLE IF EXISTS contacts	0 row(s) affected, 1 warning(s):
 1051 Unknown table 'job_tracker.contacts'	0.000 sec
3	32	19:35:14	DROP TABLE IF EXISTS jobs	0 row(s) affected	0.000 sec
3	33	19:35:14	DROP TABLE IF EXISTS companies	0 row(s) affected	0.000 sec
3	34	19:35:14	CREATE TABLE companies (
     company_id INT PRIMARY KEY AUTO_INCREMENT,
     company_name VARCHAR(100) NOT NULL,
     industry VARCHAR(50),
     website VARCHAR(200),
     city VARCHAR(50),
     state VARCHAR(50),
     notes TEXT
 )	0 row(s) affected	0.031 sec
3	35	19:35:14	CREATE TABLE jobs (
     job_id INT PRIMARY KEY AUTO_INCREMENT,
     company_id INT NOT NULL,
     job_title VARCHAR(100) NOT NULL,
     job_type ENUM('Full-time', 'Part-time', 'Contract', 'Internship') DEFAULT 'Full-time',
     salary_min INT,
     salary_max INT,
     job_url VARCHAR(300),
     date_posted DATE,
     requirements JSON,
     FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
 )	0 row(s) affected	0.031 sec
3	36	19:35:14	CREATE TABLE applications (
     application_id INT PRIMARY KEY AUTO_INCREMENT,
     job_id INT NOT NULL,
     application_date DATE NOT NULL,
     status ENUM('Applied', 'Screening', 'Interview', 'Offer', 'Rejected', 'Withdrawn') DEFAULT 'Applied',
     resume_version VARCHAR(50),
     cover_letter_sent BOOLEAN DEFAULT FALSE,
     interview_data JSON,
     FOREIGN KEY (job_id) REFERENCES jobs(job_id) ON DELETE CASCADE
 )	0 row(s) affected	0.016 sec
3	37	19:35:14	CREATE TABLE contacts (
     contact_id INT PRIMARY KEY AUTO_INCREMENT,
     company_id INT NOT NULL,
     contact_name VARCHAR(100) NOT NULL,
     title VARCHAR(100),
     email VARCHAR(100),
     phone VARCHAR(20),
     linkedin_url VARCHAR(200),
     notes TEXT,
     FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
 )	0 row(s) affected	0.031 sec
3	38	19:35:14	INSERT INTO companies (company_name, industry, website, city, state, notes) VALUES
 ('TechCorp Solutions', 'Software Development', 'https://techcorp.example.com', 'Miami', 'FL', 'Strong engineering culture, hybrid work model.'),
 ('CyberShield Security', 'Cybersecurity', 'https://cybershield.example.com', 'Fort Lauderdale', 'FL', 'Specializes in SOC operations and enterprise DLP.'),
 ('DataCo Analytics', 'Data Science', 'https://dataco.example.com', 'Austin', 'TX', 'Remote-first data analytics consultancy.')	3 row(s) affected
 Records: 3  Duplicates: 0  Warnings: 0	0.016 sec
3	39	19:35:14	INSERT INTO jobs (company_id, job_title, job_type, salary_min, salary_max, job_url, date_posted, requirements) VALUES
 (1, 'Junior Software Developer', 'Full-time', 75000, 90000, 'https://techcorp.example.com/jobs/101', '2026-11-01', '["Python", "SQL", "Flask"]'),
 (2, 'SOC Analyst I', 'Full-time', 70000, 85000, 'https://cybershield.example.com/jobs/202', '2026-11-05', '["Python", "SQL", "Linux", "SIEM", "Networking"]'),
 (3, 'Data Analyst', 'Full-time', 68000, 82000, 'https://dataco.example.com/jobs/303', '2026-11-08', '["Python", "SQL", "Tableau"]'),
 (2, 'Security Automation Intern', 'Internship', 45000, 55000, 'https://cybershield.example.com/jobs/204', '2026-11-10', '["Python", "Regex", "Git"]')	4 row(s) affected
 Records: 4  Duplicates: 0  Warnings: 0	0.000 sec
3	40	19:35:14	INSERT INTO applications (job_id, application_date, status, resume_version, cover_letter_sent, interview_data) VALUES
 (1, '2026-11-03', 'Interview', 'v2_backend_focused.pdf', TRUE, '{"round": 1, "interviewer": "Sarah Jenkins", "notes": "Technical screening passed, system design next."}'),
 (2, '2026-11-07', 'Screening', 'v2_cyber_soc.pdf', TRUE, '{"round": 0, "notes": "Recruiter phone screen scheduled for Friday."}'),
 (3, '2026-11-10', 'Applied', 'v1_general.pdf', FALSE, '{}')	3 row(s) affected
 Records: 3  Duplicates: 0  Warnings: 0	0.000 sec
3	41	19:35:14	INSERT INTO contacts (company_id, contact_name, title, email, phone, linkedin_url, notes) VALUES
 (1, 'Sarah Jenkins', 'Technical Recruiter', 's.jenkins@techcorp.example.com', '305-555-0192', 'https://linkedin.com/in/sarahjenkins-recruiter', 'Very responsive via email.'),
 (2, 'Marcus Vance', 'SOC Manager', 'mvance@cybershield.example.com', '954-555-0148', 'https://linkedin.com/in/marcusvance-sec', 'Connected at local BSides conference.')	2 row(s) affected
 Records: 2  Duplicates: 0  Warnings: 0	0.015 sec