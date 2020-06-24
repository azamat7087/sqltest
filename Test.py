import sqlite3
from random import randint
global db
global sql
import  time
db = sqlite3.connect('server.db')
sql = db.cursor()

db_blacklist = sqlite3.connect('blacklist.db')
sql_blacklist = db_blacklist.cursor()
sql_blacklist.execute("""CREATE TABLE IF NOT EXISTS blacklist (
                        login TEXT,
                        in_blacklist INT
                    )""")
db_blacklist.commit()

sql.execute("""CREATE TABLE  IF NOT EXISTS users (
                login TEXT,
                password TEXT,
                cash INT                
            )""")

db.commit()
def reg():
    users_login = input("Login: ")
    users_password = input("Password: ")
    sql_blacklist.execute(f"SELECT in_blacklist FROM blacklist WHERE login='{user_login}'")
    count = sql_blacklist.fetchone()

    if count is None:
        sql.execute(f"SELECT login FROM users WHERE login = '{users_login}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES(?, ?, ?)", (users_login, users_password, 100))
            sql_blacklist.execute(f"INSERT INTO blacklist VALUES(?, ?)", (users_login,0))
            db_blacklist.commit()
            db.commit()
            print("Registration complete!")
            answer = input("Do you want to play casino? Y/N: ")
            if answer == 'Y':
                print("Good luck!")
                casino()
            else:
                print("Ok")
        else:
            print("This person is aready registrated")

            for value in sql.execute("SELECT * FROM users"):
                print(value[0])
    else:
        print("You are in blacklist!")


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


        sql.execute(f"SELECT login FROM users WHERE password = '{user_password}'")
        a = sql.fetchone()
        user_l = tuple([user_login])

        if a is None:
            print("Not correct!!")
        else:
            if a != user_l:
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

                    for i in sql.execute(f"SELECT cash FROM users WHERE login='{user_login}'"):
                        lose_money = i[0] - randint(0, i[0])
                    print("You lose {}$ !".format(lose_money))
                    sql.execute(f'UPDATE users SET cash = {balance - lose_money} WHERE login = "{user_login}"')
                    db.commit()

                    sql.execute(f"SELECT cash FROM users WHERE login='{user_login}'")
                    if sql.fetchone()[0] <= 0:
                        print("Your balance is 0$.Your account will be deleted")
                        sql_blacklist.execute(f'UPDATE blacklist SET in_blacklist = {1} WHERE login = "{user_login}"')
                        db_blacklist.commit()
                        delete_db()


casino()