import json
import random
import getpass

user = []
def info():
        print('''\n*************about coder*************
Project is done as an part of edyoda certification by Charan N (CRG)''')

def guide():
        print('''\n*************Guidelines***************
This project selects random question from stored data as part of quiz.
Each Question will have four option in which one will be correct.
There is no negative marking for a quiz.
Along all these to segregate between users we have register and login option.
''')

def register():
        print("\n********Register an Account***********")
        username = input("Give the user name in which account need to be created: ")
        password = getpass.getpass(prompt= 'Please enter your secutre password: ')
        with open('user.json', 'r+') as details:
                users = json.load(details)
                if username in users.keys():
                        print("User with given user name already exists please choose new one if you are the one \n please go to login page")
                else:
                        users[username] = [password, "Admin"]
                        details.seek(0)
                        json.dump(users, details)
                        details.truncate()
                        print("Registration compleated successfully!")


def login():
        print("\n************Enter Login Details******************")
        username = input("Enter the Usename: ")
        password = getpass.getpass(prompt= 'PASSWORD: ')
        with open('user.json', 'r') as login_details:
                users = json.load(login_details)
        if username not in users.keys():
                print("Invalid credentials please check it if account not created prior.\nPlease register your account First")
        elif username in users.keys():
                if users[username][0] != password:
                        print("Invalid Password.\nPlease try with valid password again.")
                elif users[username][0] == password:
                        print("Logged in successfully .\n")
                        user.append(username)
                        user.append(users[username][1])




def startquiz():
        print("\n***************** PLAY QUIZ ********************")
        score = 0
        with open("Ques.json", 'r+') as f:
                j = json.load(f)
                for i in range(10):
                        no_of_questions = len(j)
                        ch = random.randint(0, no_of_questions-1)
                        print(f'\nQ{i+1} {j[ch]["question"]}\n')
                        for option in j[ch]["options"]:
                                print(option)
                        answer = input("\nEnter your answer: ")
                        if j[ch]["answer"][0] == answer[0].upper():
                                print("\nYou are correct")
                                score+=1
                        else:
                                print("\nYou are incorrect")
                        del j[ch]
                print(f'\nFINAL SCORE: {score}')

def Addques():
        if len(user) == 0:
                print("You must first login before adding questions.")
        elif len(user) == 2:
                if user[1] == "ADMIN":
                        print('\n****************Please add new QUESTIONS*************\n')
                        ques = input("New question to be added:\n")
                        opt = []
                        print("Enter the options with initials (A, B, C, D)")
                        for _ in range(4):
                                opt.append(input())
                        ans = input("Correct option:\n")
                        with open("Ques1.json", 'r+') as Q:
                                questions = json.load(Q)
                                dic = {"question": ques, "options": opt, "answer": ans}
                                questions.append(dic)
                                Q.seek(0)
                                json.dump(questions, Q)
                                Q.truncate()
                                print("Question successfully added.")		
                else:
                        print("only Admins can add Ques")




def logout():
        global user
        if len(user) == 0:
                print("already logged out.")
        else:
                user = []
                print("Sucesfully Logged out.")


def show_topics():
    print("Topics are : ")
    with open("Ques1.json", 'r+') as f:
                j = json.load(f)
                print(j)

def del_Ques():
        QTE = input("Enter question to edit")
        with open("Ques1.json", 'r+') as f:
                j = json.load(f)
                print("question not found")


if __name__ == "__main__":
        f = open('Ques.json','r')
        content = f.read()
        di = json.loads(content)
        f.close()
        choice = 1
        while choice != 9:
                print('\n*****************Quiz Application************')
                print('********************************************')
                print('1. Quiz Info')
                print('2. Quiz Guidelines')
                print('3. Register an Account')
                print('4. Login to an account')
                print('5. Start Quiz')
                print('6. Questions Adding')
                print('7. Logout')
                print('8. Show quiz content')
                print("9. Delete question ")
                print("10. Exit")
                choice = int(input('ENTER YOUR CHOICE: '))
                if choice == 1:
                        info()
                elif choice == 2:
                        guide()
                elif choice == 3:
                        register()
                elif choice == 4:
                        login()
                elif choice == 5:
                        startquiz()
                elif choice == 6:
                        Addques()
                elif choice == 7:
                        logout()
                elif choice == 8:
                        show_topics()
                elif choice ==9:
                        del_Ques()       
                elif choice == 10:
                        print("Closing the program.....")
                        break
                else:
                        print('Invalid Input, Please Choose correct option')
