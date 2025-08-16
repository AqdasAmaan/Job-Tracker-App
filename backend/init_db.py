import sqlite3

conn = sqlite3.connect('jobs.db')

sql = conn.cursor()

sql.execute('''
            CREATE TABLE IF NOT EXISTS Jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company TEXT NOT NULL,
                role TEXT NOT NULL,
                status TEXT CHECK( status IN ('Applied', 'Interview', 'Rejected', 'Offer')) DEFAULT 'Applied',
                date_applied TEXT DEFAULT (date('now')),
                notes TEXT
            )
            ''')

sql.execute("""
INSERT INTO jobs (company, role, status, date_applied, notes)
VALUES ('OpenAI', 'Software Engineer', 'Applied', '2025-08-16', 'Excited about this role');
""")

conn.commit()
sql.close()
conn.close()