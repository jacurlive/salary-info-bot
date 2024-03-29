import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        """
            checks whether the user is in the database and returns a bool
        """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "users" WHERE "user_id" = ?', (user_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, user_id, name, last_name):
        """
            adds a new user to the Users table
        """
        with self.connection:
            return self.cursor.execute(
                'INSERT INTO "users" ("user_id", "name", "last_name") VALUES (?, ?, ?)',
                (user_id, name, last_name))

    def set_active(self, user_id, active):
        """
            changes the active field
        """
        with self.connection:
            return self.cursor.execute('UPDATE "users" SET "active" = ? WHERE "user_id" = ?', (active, user_id))

    def get_users(self):
        """
            get all users list
        """
        with self.connection:
            return self.cursor.execute('SELECT "user_id", "active", "name" FROM "users"').fetchall()

    def delete_user(self, user_id):
        """
            delete one user, with user_id
        """
        with self.connection:
            return self.cursor.execute('DELETE FROM "users" WHERE "user_id" = ?', (user_id,))
