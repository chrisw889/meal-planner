import sqlite3

database = sqlite3.connect('meal_planning.db')
c = database.cursor()

version = 0

# Create tables
c.execute('''CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY,
                name TEXT,
                servings INTEGER,
                calories REAL,
                protein REAL,
                carbs REAL,
                fats REAL
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY,
                name TEXT
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS recipe_ingredients (
                recipe_id INTEGER,
                ingredient_id INTEGER,
                quantity REAL,
                unit TEXT,
                FOREIGN KEY (recipe_id) REFERENCES recipes(id),
                FOREIGN KEY (ingredient_id) REFERENCES ingredients(id),
                PRIMARY KEY (recipe_id, ingredient_id)
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS meal_plans (
                day TEXT,
                meal_type TEXT,
                recipe_id INTEGER,
                servings INTEGER,
                FOREIGN KEY (recipe_id) REFERENCES recipes(id)
            )''')

database.close()