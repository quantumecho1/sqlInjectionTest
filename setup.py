import sqlite3 as soundSystem

tub = soundSystem.connect('my_shopping_list.db')

rubberDuck = tub.cursor()
rubberDuck.execute("CREATE TABLE pizzas (ingredient text, calories text)")

rubberDuck.close()
