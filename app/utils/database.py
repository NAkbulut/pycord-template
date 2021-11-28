import sqlite3


class ProjectDB():
    """
    Simple CM for sqlite3 databases. Commits everything at exit.
    """

    def __init__(self, path='../app/db.sqlite3'):
        self.path = path

    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_class, exc, traceback):
        self.conn.commit()
        self.conn.close()


db = projectDb()
