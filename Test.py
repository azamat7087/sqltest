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


def delete_db():
    sql.execute(f'DELETE FROM users WHERE login = "{user_login}"')
    db.commit()

    print("Account is deleted")

def casino():
    global user_login
    user_login = input("Log in: ")
    number = randint(1, 2)

    for i in sql.execute(f"SELECT cash FROM users WHERE login='{user_login}'"):
        balance = i[0]

    sql.execute(f'SELECT login FROM users WHERE login="{user_login}"')
    if sql.fetchone() is None:
        print("You are not registrated")
        answer = input("Do you want to registrate? Y/N: ")
        if answer == 'Y' or answer == 'y':
            reg()
        else:
            print("Ok")
    else:
        user_password = input("Enter password: ")#

        if sql.execute(f"SELECT login FROM users WHERE password = '{user_password}'")!= sql.execute(f"SELECT login FROM users WHERE login= '{user_login}'"):
            print()
            print("Not correct")
        else:
            print("Playing game...")
            for i in range(1, 4):
                print(i)
                time.sleep(1)

            if number == 1:
                prise_money = randint(0,100)
                print("You won {} $!".format(prise_money))
                sql.execute(f'UPDATE users SET cash = {prise_money + balance} WHERE login = "{user_login}"')
                db.commit()
            else:
                print("You lose!")

                answer = input("Do you want to delete your account? Y/N: ")
                if answer == "Y":
                    delete_db()
                else:
                    print("Ok")


casino()