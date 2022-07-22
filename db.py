import sqlite3


class Database:
    db = sqlite3.connect("project.db")
    cur = db.cursor()

    def create(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
            id int PRIMARY KEY,
            user_id int NOT NULL,
            goal varchar(100),
            goal_count int,
            goal_done int DEFAULT 0
        )""")

        self.db.commit()


    def get_user(self, user_id: int):
        user = self.cur.execute("SELECT * FROM `users` WHERE user_id = ?", (user_id,)).fetchone()
        return user

    
    def reg_user(self, user_id: int):
        self.cur.execute("INSERT INTO `users` (user_id) VALUES (?)", (user_id,))
        self.db.commit()
        return self.get_user(user_id)

    
    def create_goal(self, user_id: int, goal: str, goal_count: int):
        self.cur.execute("UPDATE `users` SET goal = ?, goal_count = ? WHERE user_id = ?", (goal, goal_count, user_id))
        self.db.commit()


    def up_goal(self, user_id: int):
        user = self.get_user(user_id)

        if user and user[2]: # если есть цель
            self.cur.execute("UPDATE `users` SET goal_done = ? WHERE user_id = ?", (int(user[4] + 1), user_id))
            self.db.commit()


    def clear_goal(self, user_id: int):
        self.cur.execute("UPDATE `users` SET goal_done = ? WHERE user_id = ?", (0, user_id))
        self.db.commit()


database = Database()
