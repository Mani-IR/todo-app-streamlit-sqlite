
from datetime import datetime
from db.database import Database


class Task:
    def __init__(self, db, title, description='', status='pending', created_at=None, task_id=None):
        self.db = db
        self.title = title
        self.description = description
        self.status = status
        self.db = Database()
        self.created_at = created_at
        self.id = task_id
# --------------------------------------
    def save(self):
        self.db.connect()
        query = "INSERT INTO Task (title, description, status, created_at) VALUES (?, ?, ?, datetime('now'))"
        self.db.execute(query, (self.title, self.description, self.status))
        self.db.close()
# --------------------------------------
    @staticmethod
    def get_all(db):
        db.connect()
        db.execute("SELECT * FROM Task ORDER BY id DESC")
        tasks = db.fetchall()
        db.close()
        return tasks
# --------------------------------------
    @staticmethod
    def update_status(self, task_id, new_title,new_description):
        self.db.connect()
        self.db.execute("UPDATE Task SET title = ?, description = ? WHERE id = ?", (new_title, new_description, task_id))
        self.db.close()
# --------------------------------------
    @staticmethod
    def delete(db, task_id):
        db.connect()
        db.execute("DELETE FROM Task WHERE id = ?", (task_id,))
        db.close()
# --------------------------------------
    @staticmethod
    def toggle_status(db, task_id):
        db.connect()
        db.execute("""
            UPDATE Task
            SET status = CASE
                WHEN status = 'pending' THEN 'done'
                ELSE 'pending'
            END
            WHERE id = ?
        """, (task_id,))
        db.close()






















