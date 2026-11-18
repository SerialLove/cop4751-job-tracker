# COP4751 - Job Tracker Web Application

A full-stack web application designed to help users manage job applications, track target companies, log networking contacts, and match their personal technical skills against job requirements using a dynamic percentage scoring algorithm.

## Features
- **Dashboard:** Real-time summary metrics of total applications, active job postings, target companies, and recent application activity.
- **Company & Job Management:** Complete CRUD (Create, Read, Update, Delete) functionality for target companies and job listings.
- **JSON Requirements Parsing:** Job listings store required technical skills in a JSON format to dynamically display skill badges and calculate requirement breakdowns.
- **Application Tracking:** Track interview rounds, statuses (Applied, Interviewing, Offer, Rejected), and upload history.
- **Skill-Based Job Matcher (`/match`):** Input a comma-weighted list of personal technical skills to automatically compute match percentages against stored job postings and sort them by relevance.
- **Networking Contacts:** Log professional connections and tie them directly to target companies.

## Tech Stack
- **Backend:** Python, Flask framework
- **Database:** MySQL (via `mysql-connector-python`)
- **Frontend:** HTML5, Bootstrap 5, Jinja2 Templating
- **Data Handling:** JSON serialization for job requirements and interview notes

## Installation & Setup Instructions

1. **Clone or Download the Repository:**
   Ensure all project files (`app.py`, `database.py`, `schema.sql`, `requirements.txt`, and the `templates/` folder) are in your local project directory.

2. **Install Dependencies:**
   Open your terminal in the project root directory and run:
   ```bash
   pip install -r requirements.txt