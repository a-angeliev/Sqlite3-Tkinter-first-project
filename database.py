import sqlite3
import random
conn = sqlite3.connect('questions.db')
con = conn.cursor()


# con.execute("DROP TABLE questions")
# conn.commit()


# con.execute("""CREATE TABLE questions (
#         question,
#         a,
#         b,
#         c,
#         correct_anser
#         )""")

# con.execute("""CREATE TABLE results (
#         name,
#         correct,
#         incorrect,
#         percent
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
    # elif "del" in command:
    #     rid = input("Which row you want to delete: ")
    #     rid = str(rid)
    #     print(rid)
    #     con.execute('DELETE from questions WHERE rowid = (?)', rid )
    #     conn.commit()
    elif "guess" in command:
        rows_into_table = list(con.execute("select count(*) from questions"))
        rows_into_table = rows_into_table[0][0]
        number_questions = int(input(f"How much questions do you wnat to get (in range 1 - {rows_into_table})"))
        question_rows = []
        while not len(question_rows)==number_questions:
            random_number = random.randint(1,rows_into_table)
            if not random_number in question_rows:
                question_rows.append(random_number)
        correct_a = 0
        incorrect_a = 0
        guesser_name = input("Type your name: ")
        for el in question_rows:
            el = str(el)
            question = list(con.execute("SELECT * FROM questions WHERE rowid = (?)", el))
            question,a,b,c,correct_ans = question[0]
            # a,b,c = int(a),int(b),int(c)
            print("Question: "+question)
            print("a\) "+a)
            print("b\) "+b)
            print("c\) "+c)
            your_anser = input("What is your anser: ")
            if your_anser == correct_ans:
                print("Correct")
                correct_a +=1
            else:
                print("Incorrect")
                incorrect_a+=1
        score_in_percent = correct_a/(correct_a+incorrect_a) *100
        print(f"Your succsses is: {score_in_percent}% - Correct ansers: {correct_a}, Incorrect ansers: {incorrect_a}")
        result_list = [guesser_name,correct_a,incorrect_a,score_in_percent]
        con.execute(("INSERT INTO results  VALUES (?,?,?,?)"), result_list)
        conn.commit()
        check_results = input("Do you want to see all of your results(yes,no): ")
        print(guesser_name)
        guesser_name = str(guesser_name)
        if check_results == "yes":
            con.execute("SELECT * FROM results WHERE name = '%s'" % guesser_name)
            y = con.fetchall()
            for item in y:
                print(f"Your name: {item[0]}, Correct ansers - {item[1]}, Incorrect ansers - {item[2]}, succsses - {item[3]}%")

    elif "random":
        print("random number: ",random.randint(0,5,))
    # elif "update" in command:
    #     con.execute("UPDATE question SET question = '15+25=?', a = '2',b= '3', c='40', correct_anser = 'c' WHERE rowid = 1")
    #     conn.commit()

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