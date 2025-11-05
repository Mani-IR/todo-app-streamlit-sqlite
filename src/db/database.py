
import sqlite3

class Database:
    def __init__(self, db_name="yek.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
# --------------------------------------
    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.connection
# --------------------------------------
    def close(self):
        if self.connection:
            self.connection.close()
# --------------------------------------
    def execute(self, query, params=None):
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        self.connection.commit()
# --------------------------------------
    def fetchall(self):
        return self.cursor.fetchall()
# --------------------------------------
    def add_task(self, title, description, status, due_date):
        self.connect()
        self.execute(
            "INSERT INTO Task (title, description, status, due_date) VALUES (?, ?, ?, ?)",
            (title, description, status, due_date)
        )
        self.close()
# --------------------------------------
    def get_all_tasks(self):
        self.connect()
        self.execute("SELECT id, title, description, status, due_date, created_at FROM Task")
        data = self.fetchall()
        self.close()
        return data
# --------------------------------------
    def update_task(self, task_id, title, description, status, due_date):
        self.connect()
        self.execute(
            "UPDATE Task SET title=?, description=?, status=?, due_date=? WHERE id=?",
            (title, description, status, due_date, task_id)
        )
        self.close()
# --------------------------------------
    def delete_task(self, task_id):
        self.connect()
        self.execute("DELETE FROM Task WHERE id=?", (task_id,))
        self.close()

