import sqlite3
from random import randint
global db
global sql
import  time
db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE  IF NOT EXISTS users (
                login TEXT,
                password TEXT,
                cash INT                
            )""")

db.commit()
def reg():
    users_login = input("Login: ")
    users_password = input("Password: ")

    sql.execute(f"SELECT login FROM users WHERE login = '{users_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES(?, ?, ?)", (users_login, users_password, randint(0, 120)))
        db.commit()
        print("Registration complete!")
        answer = input("Do you want to play casino? Y/N: ")
        if answer == 'Y':
            print("Good luck!")
            casino()
        else:
            print("Ok")
    else:
        print("This person is aready registrated ")

        for value in sql.execute("SELECT * FROM users"):
            print(value[0])

def casino():
    user_login = input("Log in: ")
    number = randint(1, 2)

    sql.execute(f'SELECT login FROM users WHERE login="{user_login}"')
    if sql.fetchone() is None:
        print("You are not registrated")
        answer = input("Do you want to registrate? Y/N: ")
        if answer == 'Y':
            reg()
        else:
            print("Ok")
    else:
        user_password = input("Enter password: ")#
        sql.execute(f"SELECT password,login FROM users WHERE login='{user_login}', password = '{user_password}'")#\
        if sql.fetchone() is None:
            print("Not correct")
        else:
            print("Playing game...")
            for i in range(1, 4):
                print(i)
                time.sleep(1)

            if number == 1:
                prise_money = randint(0,100)
                print("You won {} $!".format(prise_money))
                sql.execute(f'UPDATE users SET cash = {prise_money} WHERE login = "{user_login}"')
                db.commit()
            else:
                print("You lose!")

casino()