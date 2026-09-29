import csv, sqlite3
from datetime import datetime
from config import DB_FILE, CSV_FILE, ATTENDANCE_DIR

def init_database():
    DB_FILE.parent.mkdir(parents=True,exist_ok=True); ATTENDANCE_DIR.mkdir(parents=True,exist_ok=True)
    with sqlite3.connect(DB_FILE) as c:
        c.execute('''CREATE TABLE IF NOT EXISTS attendance (id INTEGER PRIMARY KEY AUTOINCREMENT, person_name TEXT NOT NULL, person_id TEXT, date TEXT NOT NULL, time TEXT NOT NULL, status TEXT NOT NULL, UNIQUE(person_name,date))''')
    if not CSV_FILE.exists():
        with open(CSV_FILE,'w',newline='',encoding='utf-8') as f: csv.writer(f).writerow(['Name','ID','Date','Time','Status'])

def mark_attendance(name,person_id=''):
    now=datetime.now(); d=now.strftime('%Y-%m-%d'); t=now.strftime('%H:%M:%S')
    with sqlite3.connect(DB_FILE) as c:
        cur=c.execute('INSERT OR IGNORE INTO attendance(person_name,person_id,date,time,status) VALUES(?,?,?,?,?)',(name,person_id,d,t,'Present')); inserted=cur.rowcount==1
    if inserted:
        with open(CSV_FILE,'a',newline='',encoding='utf-8') as f: csv.writer(f).writerow([name,person_id,d,t,'Present'])
    return inserted

def get_today():
    d=datetime.now().strftime('%Y-%m-%d')
    with sqlite3.connect(DB_FILE) as c: return c.execute('SELECT person_name,person_id,date,time,status FROM attendance WHERE date=? ORDER BY time DESC',(d,)).fetchall()
