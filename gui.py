import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import random

root = Tk()
root.title("first GUI")
root.geometry("400x475")
root.configure(bg='#EEECEB')

#Submit funcion for DataBase
def add_question_db():
    #Connect to database
    conn = sqlite3.connect('questions.db')
    #Create coursor
    cr = conn.cursor()

    #Insert into table
    cr.execute(("INSERT INTO questions  VALUES (:question, :a, :b, :c, :correct_anser)"),
               {
                   "question": question_input.get(),
                   "a": anser_a_input.get(),
                   "b": anser_b_input.get(),
                   "c": anser_c_input.get(),
                   "correct_anser": r.get()
               })
    # Commint changes
    conn.commit()
    # Close connection
    conn.close()

    #Clear the text boxes
    question_input.delete(0,END)
    anser_a_input.delete(0,END)
    anser_b_input.delete(0,END)
    anser_c_input.delete(0,END)

# Open new window with question DataBase information.
def show_question_db():
    top = Toplevel()
    top.title("Questions DataBase")
    top.configure(bg='#EEECEB')
    # Connect to database
    conn = sqlite3.connect('questions.db')
    # Create coursor
    cr = conn.cursor()
    cr.execute("SELECT rowid, * FROM questions")
    rows = cr.fetchall()
    frm = Frame(top,bg = '#EEECEB')
    frm.config(background = '#EEECEB')
    frm.pack()


    tv= ttk.Treeview(top, column = (1,2,3,4,5,6) ,show = "headings")
    tv.pack()

    tv.heading(1, text = "ID")
    tv.column(1, minwidth = 0, width = 25, stretch = NO)
    tv.heading(2, text = "Question")
    tv.column(2, minwidth=0, width= 400, stretch=NO)
    tv.heading(3, text = "Answer a")
    tv.column(3, minwidth=0, width=100, stretch=NO, anchor = CENTER)
    tv.heading(4, text = "Answer b")
    tv.column(4, minwidth=0, width=100, stretch=NO, anchor = CENTER)
    tv.heading(5, text = "Answer c")
    tv.column(5, minwidth=0, width=100, stretch=NO, anchor = CENTER)
    tv.heading(6, text = "Correct answer")
    tv.column(6, minwidth=0, width=50, stretch=NO, anchor = CENTER)

    for i in rows:
        tv.insert('','end',value = i)

def save_updates(rb):
    conn = sqlite3.connect('questions.db')
    # Create coursor
    cr = conn.cursor()
    rowid = ID_update_input.get()
    cr.execute("""UPDATE questions SET
        question = :question,
        a = :a,
        b = :b,
        c = :c,
        correct_anser = :correct_anser
        WHERE rowid = :rowid""",
        {
        'question': question_input_editor.get(),
        'a' : answer_a_input_editor.get(),
        'b' : answer_b_input_editor.get(),
        'c' : answer_c_input_editor.get(),
        'correct_anser' : rb,
        'rowid': rowid
        })
    conn.commit()
    conn.close()
    print(m.get())
    editor.destroy()
    ID_update_input.delete(0, END)

#
#Create update function. Update info at the give ID.
def id_update():
    global editor
    editor = Tk()
    editor.title("Editor")
    editor.geometry("400x250")
    editor.configure(bg='#EEECEB')

    conn = sqlite3.connect('questions.db')
    # Create coursor
    cr = conn.cursor()
    update_id = ID_update_input.get()
    cr.execute("SELECT * FROM questions WHERE rowid = " + update_id)
    question_information = cr.fetchall()


    # Create box lables!
    question_lable = Label(editor, text="Fill in your question:")
    question_lable.grid(row=0, column=0, columnspan=4)
    ansers_lable = Label(editor, text="Fill in the next three filds one correct and two incorrect answers:")
    ansers_lable.grid(row=3, column=1, columnspan=3)
    anser_a_lable = Label(editor, text="a:")
    anser_a_lable.grid(row=4, column=0)
    anser_b_lable = Label(editor, text="b:")
    anser_b_lable.grid(row=5, column=0)
    anser_c_lable = Label(editor, text="c:")
    anser_c_lable.grid(row=6, column=0)
    correct_anser_lable = Label(editor, text="Choose the correct answer:")
    correct_anser_lable.grid(row=7, column=1, columnspan=3)

    #Create globals
    global question_input_editor
    global answer_a_input_editor
    global answer_b_input_editor
    global answer_c_input_editor
    global m
    # Create box filds for DB inputs!
    question_input_editor = Entry(editor, width=60)
    question_input_editor.grid(row=1, column=0, columnspan=4, padx=11)
    answer_a_input_editor = Entry(editor, width=57)
    answer_a_input_editor.grid(row=4, column=1, columnspan=3)
    answer_b_input_editor = Entry(editor, width=57)
    answer_b_input_editor.grid(row=5, column=1, columnspan=3, padx=1, pady=10)
    answer_c_input_editor= Entry(editor, width=57)
    answer_c_input_editor.grid(row=6, column=1, columnspan=3)

    m = StringVar(editor)
    # Create Radio Buttons about update answers!

    Radiobutton(editor, text="a:", variable= m, value="a").grid(row=8, column=1, sticky=N)
    Radiobutton(editor, text="b:", variable= m, value="b").grid(row=8, column=2, sticky=N)
    Radiobutton(editor, text="c:", variable= m, value="c").grid(row=8, column=3, sticky=N)
    m.get()
    update_buttons_editor = Button(editor, text="Update ID", command=lambda: save_updates(m.get()))
    update_buttons_editor.grid(row=9, column=0, columnspan=5, ipadx=150, ipady=10, pady=5, sticky=E)

    for info in question_information:
        question_input_editor.insert(0, info[0])
        answer_a_input_editor.insert(0, info[1])
        answer_b_input_editor.insert(0, info[2])
        answer_c_input_editor.insert(0, info[3])
        m.set(info[4])

def start_test():
    global test
    test = Toplevel()
    test.title("test")
    test.configure(bg='#EEECEB')
    # test.geometry("300x300")
    conn = sqlite3.connect('questions.db')
    # Create coursor
    cr = conn.cursor()
    rows_into_table = list(cr.execute("select count(*) from questions"))
    rows_into_table = rows_into_table[0][0]
    global start_button
    global myLable
    global tests_number_box
    global guesser_name_box
    global myLable1
    myLable = Label(test, text = f"How much test you want to make in range(0 to {rows_into_table})")
    myLable.grid(row=0,column = 0)
    myLable.config(font =("Ariel", 13))
    tests_number_box = Entry(test, width = 10)
    tests_number_box.grid(row=1,column = 0, ipady = 7,pady = 5, padx = 5)

    myLable1 = Label(test, text="Fill in your name:")
    myLable1.grid(row=2, column=0)
    myLable1.config(font=("Ariel", 13))
    guesser_name_box = Entry(test, width=30)
    guesser_name_box.grid(row=3, column=0, ipady=7, pady=5, padx=5)

    start_button = Button(test, text = "button", command = click, state = 'normal')
    start_button.grid(row=4,column = 0, ipady = 10, ipadx = 40, pady = 5, padx = 5)




def click():
    global test_numbers
    global guesser_name
    test_numbers = int(tests_number_box.get())
    guesser_name =  guesser_name_box.get()
    start_button.destroy()
    myLable.destroy()
    myLable1.destroy()
    tests_number_box.destroy()
    guesser_name_box.destroy()
    tests_number_box.destroy()
    show_tests()

def show_tests():
    conn = sqlite3.connect('questions.db')
    # Create coursor
    cr = conn.cursor()
    rows_into_table = list(cr.execute("select count(*) from questions"))
    rows_into_table = int(rows_into_table[0][0])
    global question_rows
    question_rows = []
    while not len(question_rows) == test_numbers:
        random_number = random.randint(1, rows_into_table-1)
        if not random_number in question_rows:
            question_rows.append(random_number)
    print(question_rows)
    global names
    names = []
    name = 'a'
    for index in range(len(question_rows)):
        names.append(name)
        name+="a"
    print(names)

    i = 0
    m = 0
    for el in question_rows:
        el = str(el)
        print(el)
        question = list(cr.execute("SELECT * FROM questions WHERE rowid = %s" %el))
        question, a, b, c, correct_ans = question[0]
        question_lable = Label(test, text = question)
        question_lable.grid(row= i, column = 0, columnspan = 2 )
        answer_a = Label(test, text = "a: "+ a)
        answer_b = Label(test, text = "b: "+ b)
        answer_c = Label(test, text = "c: "+ c)
        answer_a.grid(row=i+1,column=1, sticky = W)
        answer_b.grid(row=i+2,column=1, sticky = W)
        answer_c.grid(row=i+3,column=1, sticky = W)
        names[m] = StringVar(test)
        Radiobutton(test, text=' ', variable=names[m], value='a').grid(row=i+1, column=0 , sticky = E)
        Radiobutton(test, text=' ', variable=names[m], value='b').grid(row=i+2, column=0 , sticky = E)
        Radiobutton(test, text=' ', variable=names[m], value='c').grid(row=i+3, column=0 , sticky = E)





        # a = StringVar(test)
        # Radiobutton(text, text='' , variable = )
        # check_button = Button(test, text = "next test",command = check_results)
        # check_button.grid(row=0, column =1)
        # if your_anser == correct_ans:
        #     print("Correct")
        #     correct_a += 1
        # else:
        #     print("Incorrect")
        #     incorrect_a += 1
        i+=6
        m+=1
    check_results_button = Button(test, text = "Submit and check results", command = submit_decision)
    check_results_button.grid(row=i+6, column = 0, columnspan = len(question_rows))


def submit_decision():
    conn = sqlite3.connect('questions.db')
    # Create coursor
    cr = conn.cursor()
    correct = 0
    incorrect = 0
    for index in range(len(names)):
        ri = question_rows[index]
        question = list(cr.execute("SELECT * FROM questions WHERE rowid = %s" %ri))
        print(question)
        question, a, b, c, correct_ans = question[0]
        given_answer = names[index].get()
        if given_answer == correct_ans:
            correct+=1
        else:
            incorrect +=1
    score_in_percent = correct / (correct + incorrect ) * 100
    formated_score_in_percent = round(score_in_percent,2)
    result_list = [guesser_name, correct, incorrect, formated_score_in_percent]
    cr.execute(("INSERT INTO results  VALUES (?,?,?,?)"), result_list)
    conn.commit()
    message_result =messagebox.askquestion("Results",f"Your correct answers are: {correct}\r\nYour inccorect answers are:{incorrect}\r\nDo you want to check all your results?")
    if message_result == "yes":
        cr.execute("SELECT * FROM results WHERE name = '%s'" % guesser_name)
        y = cr.fetchall()


        results_by_name = Toplevel()
        results_by_name.title("Results by name")
        results_by_name.configure(bg='#EEECEB')
        frm1 = Frame(results_by_name)
        frm1.pack(side=tk.LEFT, padx=0)

        tv = ttk.Treeview(results_by_name, column=(1, 2, 3, 4), show="headings")
        tv.pack()

        tv.heading(1, text="Name")
        tv.column(1, minwidth=0, width=100, stretch=NO, anchor = CENTER)
        tv.heading(2, text="Correct answers")
        tv.column(2, minwidth=0, width=100, stretch=NO, anchor = CENTER)
        tv.heading(3, text="Incorrect answers")
        tv.column(3, minwidth=0, width=100, stretch=NO, anchor=CENTER)
        tv.heading(4, text="Results in %")
        tv.column(4, minwidth=0, width=100, stretch=NO, anchor=CENTER)
        for i in y:
            tv.insert('', 'end', value=i)
    else:
        test.destroy()

def search_in_results1():
    global search_box
    global search_in_results
    search_in_results = Toplevel()
    search_in_results.title("Show results")
    search_in_results.configure(bg='#EEECEB')
    search_instruction_lable1 = Label(search_in_results, text = "For searching by name fill in the empty box with name.")
    search_instruction_lable2= Label(search_in_results, text = "For showing all DataBase results fill in the empty box with (*).")
    search_instruction_lable1.grid(row = 0,column = 0)
    search_instruction_lable2.grid(row=1, column = 0)
    search_box = Entry(search_in_results, width = 30)
    search_box.grid(row = 2, column = 0)
    search_box.insert(0,"*")
    search_button = Button(search_in_results, text = "Search", command = return_results)
    search_button.grid(row=3,column = 0)


def return_results():
    conn = sqlite3.connect('questions.db')
    # Create coursor
    cr = conn.cursor()
    searched_name = search_box.get()
    if searched_name == "*":
        cr.execute("SELECT * FROM results")
        y = cr.fetchall()
    else:
        cr.execute("SELECT * FROM results WHERE name = '%s'" % searched_name)
        y = cr.fetchall()
    search_in_results.destroy()
    search_in_results2 = Toplevel()
    search_in_results2.configure(bg='#EEECEB')
    search_in_results2.title("Show results")
    frm1 = Frame(search_in_results2)
    frm1.pack()

    tv = ttk.Treeview(search_in_results2, column=(1, 2, 3, 4), show="headings")
    tv.pack()

    tv.heading(1, text="Name")
    tv.column(1, minwidth=0, width=100, stretch=NO, anchor=CENTER)
    tv.heading(2, text="Correct answers")
    tv.column(2, minwidth=0, width=100, stretch=NO, anchor=CENTER)
    tv.heading(3, text="Incorrect answers")
    tv.column(3, minwidth=0, width=100, stretch=NO, anchor=CENTER)
    tv.heading(4, text="Results in %")
    tv.column(4, minwidth=0, width=100, stretch=NO, anchor=CENTER)
    for i in y:
        tv.insert('', 'end', value=i)










#Create box lables!
question_lable = Label(root, text = "Fill in your question:")
question_lable.grid(row= 0, column = 0, columnspan = 4)
ansers_lable = Label(root, text = "Fill in the next three filds one correct and two incorrect answers:")
ansers_lable.grid(row=3,column = 1,columnspan = 3)
anser_a_lable = Label(root, text = "a:")
anser_a_lable.grid(row = 4,column = 0)
anser_b_lable = Label(root, text = "b:")
anser_b_lable.grid(row = 5,column = 0)
anser_c_lable = Label(root, text = "c:")
anser_c_lable.grid(row = 6,column = 0)
correct_anser_lable = Label(root, text = "Choose the correct answer:")
correct_anser_lable.grid(row=7,column = 1,columnspan = 3)

ID_update_lable = Label(root, text= "ID")
ID_update_lable.grid(row = 11 , column = 0)

#Create box filds for DB inputs!
question_input = Entry(root, width = 60)
question_input.grid(row=1 ,column = 0,columnspan =4,padx = 11)
anser_a_input = Entry(root, width= 57)
anser_a_input.grid(row = 4 ,column = 1,columnspan =3)
anser_b_input = Entry(root, width= 57)
anser_b_input.grid(row = 5 ,column = 1, columnspan =3,padx = 1,pady = 10)
anser_c_input = Entry(root, width= 57)
anser_c_input.grid(row = 6 ,column = 1,columnspan =3)

ID_update_input = Entry(root, width = 5)
ID_update_input.grid(row = 11 , column =1, sticky = W)

#Give returning value type from Radio Buttons.
r = StringVar()
#Set default value for RB answers.
r.set("a")
#Create Radio Buttons about correct ansers!
Radiobutton(root, text = "a:",variable = r, value = "a").grid(row = 8,column = 1,sticky = N)
Radiobutton(root, text = "b:",variable = r, value = "b").grid(row = 8,column = 2,sticky = N)
Radiobutton(root, text = "c:",variable = r, value = "c").grid(row = 8,column = 3,sticky = N)

#Create Buttons!
add_buttons = Button(root, text = "Add to question DateBase!", command = add_question_db)
add_buttons.grid(row= 9, column = 0, columnspan = 4, ipadx = 110, ipady = 10, pady = 5, sticky = E)
show_question_button = Button(root,text = "Show question DataBase!", command = show_question_db)
show_question_button.grid(row = 10,column = 0, columnspan = 4, ipadx = 114, ipady = 10, pady = 5,sticky = E)
update_button = Button(root, text = "Change ID from question DB", command= id_update)
update_button.grid(row = 11, column=1 , columnspan  = 3, ipadx = 63, ipady = 10, pady = 5, sticky = E)
start_test_button = Button(root, text = "Start Test", command = start_test)
start_test_button.grid(row = 12, column = 1 , columnspan = 3, ipadx = 155, ipady = 10, pady = 5, sticky = E)
search_in_results = Button(root, text = "Search in results", command = search_in_results1)
search_in_results.grid(row = 13, column = 1 , columnspan = 3, ipadx = 137, ipady = 10, pady = 5, sticky = E)
root.mainloop()