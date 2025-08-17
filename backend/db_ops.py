import sqlite3

def add_job(company, role, status='Applied'):
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Jobs (company, role, status)
        VALUES (?, ?, ?)
    ''', (company, role, status))

    conn.commit()
    conn.close()

def view_jobs():
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    jobs = cursor.execute('SELECT * FROM Jobs').fetchall()

    conn.close()

    return jobs

