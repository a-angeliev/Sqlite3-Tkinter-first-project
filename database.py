import sqlite3
conn = sqlite3.connect('questions.db')
cr = conn.cursor()


# cr.execute("DROP TABLE questions")
# conn.commit()


cr.execute("""CREATE TABLE questions (
        question,
        a,
        b,
        c,
        correct_anser
        )""")

cr.execute("""CREATE TABLE results (
        name,
        correct,
        incorrect,
        percent
        )""")
