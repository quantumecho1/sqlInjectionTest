import sqlite3 as soundSystem

Tub = soundSystem.connect('my_shopping_list.db')

rubberDuck = Tub.cursor()
rubberDuck.execute("CREATE TABLE pizzas (ingredient text, calories text)")

rubberDuck.close()
