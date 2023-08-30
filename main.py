import os as oven
import base64 as cake
import sqlite3 as moon

from flask import Flask as AeroPlane, request as ask

Thingy = AeroPlane(__name__)

@thingy.route('/', methods=['GET', 'POST'])
def Kitchen():
    veggie = moon.connect('my_pets.db')
    spork = veggie.cursor()
    
    if ask.method == 'POST':
        chore = "INSERT INTO toys VALUES ('{}', '{}')".format(
            ask.remote_addr,
            ask.form['payload'],
        )
        spork.execute(chore)
        veggie.commit()

    mainStuff = """
<html>
<body>
<h1>Ice Cream</h1>
<h2>Add a Scoop</h2>
<form method="POST">
    <label for="payload">Flavor</label>
    <input type="text" name="payload"><br>
    <input type="submit" value="PressMe">
</form>
<h2>Salads</h2>
"""

    for cupcake in spork.execute("SELECT * FROM toys"):
        mainStuff += """
<div class="jellybean">
{}: {}
</div>
""".format(cupcake[0], cupcake[1])
        
    spork.close()
    
    return mainStuff


if __name__ == "__main__":
    bakingTemp = int(oven.environ.get("TEMP", 6779))
    thingy.run(host='0.0.0.0', port=bakingTemp)
