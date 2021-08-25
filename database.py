import sqlite3

conn = sqlite3.connect('questions.db')
con = conn.cursor()

# con.execute("""CREATE TABLE questions (
#         question,
#         a,
#         b,
#         c,
#         correct_anser
#         )""")

command = input("Type instruction(add, show, del, guess): ")
while not command == "end":
    if "add" in command:
        question = input("Type question: ")
        print("Now fill 3 choises, 2 incorrect and 1 correct")
        a = input("a): ")
        b = input("b): ")
        c = input("c): ")
        correct = input("Correct anser is (a, b, c ): ")
        con = conn.cursor()
        # add,question,a,b,c,correct= command.split()
        add_list = [question,a,b,c,correct]
        con.execute(("INSERT INTO questions  VALUES (?,?,?,?,?)"), add_list)
        conn.commit()
    elif "show" in command:
        con.execute("SELECT rowid, * FROM questions")
        a = con.fetchall()
        for item in a:
            print(item)
    elif "del" in command:
        rid = int(input("Which row you want to delete: "))
        print(rid)
        con.execute('DELETE from questions WHERE rowid= (?)',rid)
        conn.commit()
    elif "guess" in command:
        question = list(con.execute("SELECT * FROM questions WHERE rowid = 2"))
        question,a,b,c,correct_ans = question[0]
        # a,b,c = int(a),int(b),int(c)
        print("Question: "+question)
        print("a\) "+a)
        print("b\) "+b)
        print("c\) "+c)
        your_anser = input("What is your anser: ")
        if your_anser == correct_ans:
            print("Correct")
        else:
            print("Incorrect")


    command = input("Type instruction(add, show, del, guess): ")

#







# con.execute("INSERT INTO questions  VALUES (1, 2, 3, 4, 5)")

# con.execute("SELECT * FROM questions WHERE rowid=2")
# a = con.fetchall()
# print(a)
# c.execute("INSERT INTO blabla VALUES ('JsdON', 'Pesdsdsho')")
# conn.commit()
# c.execute("INSERT INTO blabla VALUES ('JOfssaN', 'Pesfsfho')")
# conn.commit()
# c.execute("INSERT INTO blabla VALUES ('JsagN', 'Peshgsgao')")
# conn.commit()
# c.execute("SELECT * FROM questions WHERE rowid = 1")
# a = c.fetchall()
# print(a)
# print(c)

# ss = list(c.execute("select count(*) from blabla"))
# print(ss[0][0])