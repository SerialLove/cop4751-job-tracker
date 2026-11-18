from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db
import json

app = Flask(__name__)
app.secret_key = 'cop4751_job_tracker_secret'

# ==========================================
# 1. DASHBOARD ROUTE
# ==========================================
@app.route('/')
def dashboard():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total FROM applications")
    total_apps = cursor.fetchone()['total']

    cursor.execute("SELECT COUNT(*) AS total FROM companies")
    total_companies = cursor.fetchone()['total']

    cursor.execute("SELECT COUNT(*) AS total FROM jobs")
    total_jobs = cursor.fetchone()['total']

    cursor.execute("""
        SELECT status, COUNT(*) AS count 
        FROM applications 
        GROUP BY status
    """)
    status_counts = cursor.fetchall()

    cursor.execute("""
        SELECT a.application_id, a.application_date, a.status, a.resume_version,
               j.job_title, j.job_type, c.company_name
        FROM applications a
        JOIN jobs j ON a.job_id = j.job_id
        JOIN companies c ON j.company_id = c.company_id
        ORDER BY a.application_date DESC
        LIMIT 5
    """)
    recent_apps = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        'dashboard.html',
        total_apps=total_apps,
        total_companies=total_companies,
        total_jobs=total_jobs,
        status_counts=status_counts,
        recent_apps=recent_apps
    )

# ==========================================
# 2. COMPANIES ROUTES (Full CRUD)
# ==========================================
@app.route('/companies')
def list_companies():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM companies ORDER BY company_name ASC")
    companies = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('companies.html', companies=companies)

@app.route('/companies/add', methods=['POST'])
def add_company():
    name = request.form['company_name']
    industry = request.form.get('industry', '')
    website = request.form.get('website', '')
    city = request.form.get('city', '')
    state = request.form.get('state', '')
    notes = request.form.get('notes', '')

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO companies (company_name, industry, website, city, state, notes)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (name, industry, website, city, state, notes))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Company added successfully!', 'success')
    return redirect(url_for('list_companies'))

@app.route('/companies/edit/<int:company_id>', methods=['POST'])
def edit_company(company_id):
    name = request.form['company_name']
    industry = request.form.get('industry', '')
    website = request.form.get('website', '')
    city = request.form.get('city', '')
    state = request.form.get('state', '')
    notes = request.form.get('notes', '')

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE companies
        SET company_name = %s, industry = %s, website = %s, city = %s, state = %s, notes = %s
        WHERE company_id = %s
    """, (name, industry, website, city, state, notes, company_id))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Company updated successfully!', 'info')
    return redirect(url_for('list_companies'))

@app.route('/companies/delete/<int:company_id>', methods=['POST'])
def delete_company(company_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM companies WHERE company_id = %s", (company_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Company deleted.', 'warning')
    return redirect(url_for('list_companies'))

# ==========================================
# 3. JOBS ROUTES (Full CRUD + JSON Requirements)
# ==========================================
@app.route('/jobs')
def list_jobs():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT j.*, c.company_name
        FROM jobs j
        JOIN companies c ON j.company_id = c.company_id
        ORDER BY j.date_posted DESC
    """)
    jobs = cursor.fetchall()

    for job in jobs:
        if job['requirements']:
            job['req_list'] = json.loads(job['requirements'])
        else:
            job['req_list'] = []

    cursor.execute("SELECT company_id, company_name FROM companies ORDER BY company_name ASC")
    companies = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('jobs.html', jobs=jobs, companies=companies)

@app.route('/jobs/add', methods=['POST'])
def add_job():
    company_id = request.form['company_id']
    job_title = request.form['job_title']
    job_type = request.form['job_type']
    salary_min = request.form.get('salary_min') or None
    salary_max = request.form.get('salary_max') or None
    job_url = request.form.get('job_url', '')
    date_posted = request.form.get('date_posted') or None

    raw_reqs = request.form.get('requirements', '')
    req_list = [skill.strip() for skill in raw_reqs.split(',') if skill.strip()]
    requirements_json = json.dumps(req_list)

    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO jobs (company_id, job_title, job_type, salary_min, salary_max, job_url, date_posted, requirements)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (company_id, job_title, job_type, salary_min, salary_max, job_url, date_posted, requirements_json))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Job posting added!', 'success')
    except Exception:
        flash('Could not add job: please check that all fields and dates are valid.', 'danger')

    return redirect(url_for('list_jobs'))

@app.route('/jobs/edit/<int:job_id>', methods=['POST'])
def edit_job(job_id):
    company_id = request.form['company_id']
    job_title = request.form['job_title']
    job_type = request.form['job_type']
    salary_min = request.form.get('salary_min') or None
    salary_max = request.form.get('salary_max') or None
    job_url = request.form.get('job_url', '')
    date_posted = request.form.get('date_posted') or None

    raw_reqs = request.form.get('requirements', '')
    req_list = [skill.strip() for skill in raw_reqs.split(',') if skill.strip()]
    requirements_json = json.dumps(req_list)

    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE jobs
            SET company_id = %s, job_title = %s, job_type = %s, salary_min = %s,
                salary_max = %s, job_url = %s, date_posted = %s, requirements = %s
            WHERE job_id = %s
        """, (company_id, job_title, job_type, salary_min, salary_max, job_url, date_posted, requirements_json, job_id))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Job posting updated!', 'info')
    except Exception:
        flash('Could not update job: please verify your input values.', 'danger')

    return redirect(url_for('list_jobs'))

@app.route('/jobs/delete/<int:job_id>', methods=['POST'])
def delete_job(job_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jobs WHERE job_id = %s", (job_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Job deleted.', 'warning')
    return redirect(url_for('list_jobs'))

# ==========================================
# 4. APPLICATIONS ROUTES (Full CRUD + JSON)
# ==========================================
@app.route('/applications')
def list_applications():
    status_filter = request.args.get('status', '')
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT a.*, j.job_title, c.company_name
        FROM applications a
        JOIN jobs j ON a.job_id = j.job_id
        JOIN companies c ON j.company_id = c.company_id
    """
    params = []
    if status_filter:
        query += " WHERE a.status = %s"
        params.append(status_filter)

    query += " ORDER BY a.application_date DESC"
    cursor.execute(query, tuple(params))
    applications = cursor.fetchall()

    for app_item in applications:
        if app_item['interview_data']:
            app_item['interview_dict'] = json.loads(app_item['interview_data'])
        else:
            app_item['interview_dict'] = {}

    cursor.execute("""
        SELECT j.job_id, j.job_title, c.company_name
        FROM jobs j
        JOIN companies c ON j.company_id = c.company_id
        ORDER BY c.company_name ASC
    """)
    jobs = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('applications.html', applications=applications, jobs=jobs, current_filter=status_filter)

@app.route('/applications/add', methods=['POST'])
def add_application():
    job_id = request.form['job_id']
    application_date = request.form['application_date']
    status = request.form['status']
    resume_version = request.form.get('resume_version', '')
    cover_letter_sent = True if request.form.get('cover_letter_sent') else False

    round_num = request.form.get('round', '')
    interviewer = request.form.get('interviewer', '')
    notes = request.form.get('interview_notes', '')

    interview_obj = {}
    if round_num or interviewer or notes:
        interview_obj = {
            'round': round_num,
            'interviewer': interviewer,
            'notes': notes
        }
    interview_json = json.dumps(interview_obj)

    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO applications (job_id, application_date, status, resume_version, cover_letter_sent, interview_data)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (job_id, application_date, status, resume_version, cover_letter_sent, interview_json))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Application logged!', 'success')
    except Exception:
        flash('Could not log application: please enter a valid 4-digit year date (YYYY-MM-DD).', 'danger')

    return redirect(url_for('list_applications'))

@app.route('/applications/update_status/<int:application_id>', methods=['POST'])
def update_application_status(application_id):
    new_status = request.form['status']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE applications SET status = %s WHERE application_id = %s", (new_status, application_id))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Application status updated!', 'info')
    return redirect(url_for('list_applications'))

@app.route('/applications/delete/<int:application_id>', methods=['POST'])
def delete_application(application_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM applications WHERE application_id = %s", (application_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Application deleted.', 'warning')
    return redirect(url_for('list_applications'))

# ==========================================
# 5. CONTACTS ROUTES (Full CRUD)
# ==========================================
@app.route('/contacts')
def list_contacts():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT ct.*, c.company_name
        FROM contacts ct
        JOIN companies c ON ct.company_id = c.company_id
        ORDER BY ct.contact_name ASC
    """)
    contacts = cursor.fetchall()

    cursor.execute("SELECT company_id, company_name FROM companies ORDER BY company_name ASC")
    companies = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('contacts.html', contacts=contacts, companies=companies)

@app.route('/contacts/add', methods=['POST'])
def add_contact():
    company_id = request.form['company_id']
    contact_name = request.form['contact_name']
    title = request.form.get('title', '')
    email = request.form.get('email', '')
    phone = request.form.get('phone', '')
    notes = request.form.get('notes', '')

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO contacts (company_id, contact_name, title, email, phone, notes)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (company_id, contact_name, title, email, phone, notes))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Contact added successfully!', 'success')
    return redirect(url_for('list_contacts'))

@app.route('/contacts/edit/<int:contact_id>', methods=['POST'])
def edit_contact(contact_id):
    company_id = request.form['company_id']
    contact_name = request.form['contact_name']
    title = request.form.get('title', '')
    email = request.form.get('email', '')
    phone = request.form.get('phone', '')
    notes = request.form.get('notes', '')

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE contacts
        SET company_id = %s, contact_name = %s, title = %s, email = %s, phone = %s, notes = %s
        WHERE contact_id = %s
    """, (company_id, contact_name, title, email, phone, notes, contact_id))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Contact updated successfully!', 'info')
    return redirect(url_for('list_contacts'))

@app.route('/contacts/delete/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE contact_id = %s", (contact_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Contact deleted.', 'warning')
    return redirect(url_for('list_contacts'))

# ==========================================
# 6. SKILL-BASED JOB MATCH ROUTE
# ==========================================
@app.route('/match', methods=['GET', 'POST'])
def job_match():
    results = []
    raw_skills = ""

    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT j.*, c.company_name
        FROM jobs j
        JOIN companies c ON j.company_id = c.company_id
    """)
    jobs = cursor.fetchall()
    cursor.close()
    conn.close()

    if request.method == 'POST':
        raw_skills = request.form.get('user_skills', '')
        user_skills_set = {s.strip().lower() for s in raw_skills.split(',') if s.strip()}

        for job in jobs:
            reqs = []
            if job['requirements']:
                try:
                    reqs = json.loads(job['requirements'])
                except Exception:
                    reqs = []

            reqs_lower = [r.strip().lower() for r in reqs]
            reqs_set = set(reqs_lower)

            if reqs_set:
                matched = user_skills_set.intersection(reqs_set)
                missing = reqs_set - user_skills_set
                match_pct = int((len(matched) / len(reqs_set)) * 100)
            else:
                matched = set()
                missing = set()
                match_pct = 0

            matched_original = [r for r in reqs if r.strip().lower() in matched]
            missing_original = [r for r in reqs if r.strip().lower() in missing]

            results.append({
                'job_title': job['job_title'],
                'company_name': job['company_name'],
                'job_type': job['job_type'],
                'match_pct': match_pct,
                'matched_skills': matched_original,
                'missing_skills': missing_original,
                'salary_min': job['salary_min'],
                'salary_max': job['salary_max']
            })

        results = sorted(results, key=lambda x: x['match_pct'], reverse=True)

    return render_template('match.html', results=results, raw_skills=raw_skills)

if __name__ == '__main__':
    app.run(debug=True)