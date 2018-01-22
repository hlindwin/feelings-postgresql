from flask import Flask, render_template, request
import sqlite3, os
app = Flask(__name__)

#conn = sqlite3.connect(":memory:", check_same_thread = False)
conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()


# Make some fresh tables using executescript()
createtable = '''
CREATE TABLE IF NOT EXISTS feeling (
    --id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    feelings    TEXT,
    --url  TEXT UNIQUE,
        -- because I made this unique, it won't allow dupes later
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
'''
cur.executescript(createtable)

@app.route('/', methods=['GET','POST'])
def index():
    #return 'Hello, World!'  # This return is what the person sees
    # you can put css in the quotes
    text = {'input':'Hello, this page cares how you are feeling'
            ,'input2':'Please tell me how you are feeling'
            ,'input3':'I really want to know'}
    if request.method == "POST":
        feeling = request.form['feeling'] # this is the name of the field in the form.
        text ={}
        conn = sqlite3.connect('test.sqlite')
        cur = conn.cursor()
        try:
            cur.execute('''INSERT
            --  OR IGNORE
            INTO feeling (feelings )  --if two, add ', field2' and (? , ?)
                VALUES ( ?  )''', ( feeling,  ) )  # and (field1, field2, ...)
        except:
            pass
        conn.commit()
        cur.execute(""" Select feelings from feeling limit 1000 """)
        allfeelings = cur.fetchall()
        return render_template("index.html", feeling =feeling, text = text, allfeelings = allfeelings)
            # because the index.html has two variabls (feeling and text),
            # I have to pass both variables
    return render_template("index.html",text=text,allfeelings = '')


# if not in c9
#if __name__ == "__main__":  # This says only run the app if this is your main file
#    app.run(debug=True)


#if on c9: 
DATABASE = 'test.sqlite'  # this didn't work to get the command to work , app.logger.info("Database on: %s", app.config['DATABASE'])
if __name__ == "__main__":
    app.debug = True
    
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.logger.info("Starting flask app on %s:%s", host, port)
   # app.logger.info("Database on: %s", app.config['DATABASE'])
    
    app.run(host=host, port=port)




# testing the doc

print('sucks')

#this is how to use dictionaries
# keys have to be unique
text = {'input':'Hello, this is the first'
    ,'input2':'This is the second'
    ,'input3':'This is the thirdd'}
for k,v in text.items():
    print(k, v)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#cur.execute(""" Select rowid, name, url from Artist order by name limit 10 """)
cur.execute(""" Select * from feeling limit 10 """)
print(cur.fetchall())
